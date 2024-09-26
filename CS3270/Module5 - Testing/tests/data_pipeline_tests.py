import unittest
from unittest.mock import MagicMock
from src.data_load import DataLoader
from src.data_processing import DataProcessor
from src.data_storage import DataStorage
from src.data_pipeline import DataPipeLine

class DataPipeLineTestSuite(unittest.TestCase):
    def setUp(self):
        """Set up the test environment by creating mock instances for DataLoader,
        DataProcessor, and DataStorage, and initializing the DataPipeLine."""
        self.data_loader = MagicMock(spec=DataLoader)
        self.data_processor = MagicMock(spec=DataProcessor)
        self.data_storage = MagicMock(spec=DataStorage)

        # Initialize the DataPipeLine with the mock instances
        self.pipeline = DataPipeLine(self.data_loader, self.data_processor, self.data_storage)

    def test_run_pipeline_load_failure(self):
        """Test the scenario where loading data fails. The test simulates an
        exception when attempting to load data, ensuring that the data processing
        and storage steps are not executed."""
        # Simulate an exception during data loading
        self.data_loader.read_csv_chunks.side_effect = Exception("Load error")

        # Run the pipeline
        self.pipeline.run_pipeline()

        # Verify that process_data_frame was not called
        self.data_processor.process_data_frame.assert_not_called()

        # Verify that get_file_type was not called
        self.data_storage.get_file_type.assert_not_called()

    def test_run_pipeline_process_failure(self):
        """Test the scenario where data processing fails. This test simulates
        successful data loading but raises an exception during processing,
        ensuring that the storage step is not executed."""
        # Simulate successful loading but a failure in processing
        self.data_loader.read_csv_chunks.return_value = MagicMock()
        self.data_processor.process_data_frame.side_effect = Exception("Processing error")

        # Run the pipeline
        self.pipeline.run_pipeline()

        # Verify that get_file_type was not called
        self.data_storage.get_file_type.assert_not_called()

    def test_run_pipeline_storage_failure(self):
        """Test the scenario where data storage fails. This test simulates
        successful loading and processing of data, but raises an exception
        when attempting to store the data."""
        # Simulate successful loading and processing
        self.data_loader.read_csv_chunks.return_value = MagicMock()
        self.data_processor.process_data_frame.return_value = None
        self.data_storage.get_file_type.side_effect = Exception("Storage error")

        # Run the pipeline
        self.pipeline.run_pipeline()
        # No assertions needed here; we focus on ensuring the flow is correct.

if __name__ == '__main__':
    unittest.main()
