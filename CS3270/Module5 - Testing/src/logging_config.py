import logging

def setup_logging():
    # Main logger for the pipeline
    logging.basicConfig(
        filename='./main_pipeline.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
