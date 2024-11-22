# Weather Data Application with Machine Learning

This Flask-based application leverages machine learning to predict rainfall amounts based on historical weather data. Users can input key weather attributes through a web interface, and the application predicts the expected rainfall using a trained Random Forest regression model. The application also provides a streamlined and intuitive UI for entering weather-related inputs.

---

## Features

- **Rainfall Prediction**: Predicts rainfall amounts based on weather features such as temperature, humidity, and pressure.
- **Interactive Input Form**: Users can input weather attributes using a web form with dropdowns for categorical inputs.
- **Pre-trained Model**: Utilizes a Random Forest regression model trained on historical weather data.

---

## Machine Learning Overview

### Model
- **Algorithm**: Random Forest Regressor
- **Purpose**: Predict the amount of rainfall (in mm) based on weather conditions.
- **Training Data**: The model was trained using a dataset containing weather observations such as temperature, humidity, pressure, and rain indicators.

---

## Model Training Process

### Data Preparation
1. **Load Dataset**:
   The dataset was loaded from a CSV file (`Weather Training Data.csv`).

2. **Handle Missing Values**:
   - Numerical columns were filled with their median values.
   - Categorical columns were filled with 'Unknown' for missing data.

3. **Drop Irrelevant Columns**:
   - The `row ID` column was removed, as it is not useful for prediction.

4. **Encode Categorical Variables**:
   - The `RainToday` column was binary-encoded (`Yes` → 1, `No` → 0).
   - Other categorical variables (`Location`, `WindGustDir`, `WindDir9am`, `WindDir3pm`) were one-hot encoded.

5. **Define Features and Target**:
   - Features (`X`): All columns except `RainTomorrow`.
   - Target (`y`): The `Rainfall` column.

### Model Training
- **Algorithm**: Random Forest Regressor
- **Training and Testing Split**:
   - Data was split into training (80%) and testing (20%) sets.
- **Model Training**:
   - A Random Forest Regressor was trained on the training data.

### Model Evaluation
- The model was evaluated using the testing set, achieving the following metrics:
   - **Mean Absolute Error (MAE)**: 0.0020
   - **Mean Squared Error (MSE)**: 0.0069
   - **R² Score**: 0.9999
---

## Workflow

1. **User Input**:
   - Users provide weather attributes via a web form.
   - Drop-down menus are used for categorical inputs (e.g., rain indicators).

2. **Data Preprocessing**:
   - The input data is aligned with the model's expected feature set.
   - Missing one-hot encoded features are defaulted to 0.

3. **Prediction**:
   - The user input is fed into the pre-trained model.
   - The model predicts the expected rainfall amount.

4. **Result Display**:
   - The predicted rainfall is rounded to two decimal places and displayed to the user.

---

## Routes

### `/predict` (Rainfall Prediction Route)
- **Method**: GET, POST
- **Description**:
   - **GET**: Displays the rainfall prediction form.
   - **POST**: Processes the user input and predicts rainfall.
- **Functionality**:
   - Loads the pre-trained Random Forest model.
   - Handles user input from the form.
   - Preprocesses data to match the model’s requirements.
   - Uses the model to predict the rainfall amount and returns the result.

---

## Testing

Testing was focused on the model. Dummy data is created and passed to the model:

```python
def generate_dummy_data(num_samples=10):
    dummy_data = {
        'MinTemp': np.random.uniform(-5, 40, num_samples),  # Temperatures between -5°C and 40°C
        'MaxTemp': np.random.uniform(0, 45, num_samples),  # Temperatures between 0°C and 45°C
        'Rainfall': np.random.uniform(0, 50, num_samples),  # Rainfall between 0mm and 50mm
        'Humidity9am': np.random.uniform(20, 100, num_samples),  # Humidity between 20% and 100%
        'Humidity3pm': np.random.uniform(20, 100, num_samples),  # Humidity between 20% and 100%
        'Pressure9am': np.random.uniform(1000, 1035, num_samples),  # Pressure between 1000hPa and 1035hPa
        'Pressure3pm': np.random.uniform(1000, 1035, num_samples),  # Pressure between 1000hPa and 1035hPa
        'Location': np.random.choice(locations, num_samples),  # Randomly select locations
        'WindGustDir': np.random.choice(wind_dirs, num_samples),  # Randomly select wind gust directions
        'WindDir9am': np.random.choice(wind_dirs, num_samples),  # Randomly select wind directions at 9am
        'WindDir3pm': np.random.choice(wind_dirs, num_samples),  # Randomly select wind directions at 3pm
        'RainToday': np.random.choice(rain_today_options, num_samples)  # Randomly select Yes/No for rain today
    }
    return pd.DataFrame(dummy_data)

# Generate dummy data
dummy_data = generate_dummy_data(100000)
```

Output:
```bash
MinTemp    MaxTemp   Rainfall  Humidity9am  Humidity3pm  Pressure9am  Pressure3pm  PredictedRainfall
0      29.700786  25.511482  31.043064    47.067020    83.905188  1031.305184  1018.957923             31.004
1      29.963384  28.704260  24.320929    68.645471    75.834913  1013.693891  1016.731943             24.400
2      38.867930  22.241834  39.695399    97.177539    31.630334  1000.964309  1034.308623             39.588
3       0.075350  35.606290  17.746646    55.767986    47.050963  1029.242885  1020.641967             17.800
4      35.878591  44.376725  26.576755    24.986591    63.676029  1024.641940  1006.667846             26.596
...          ...        ...        ...          ...          ...          ...          ...                ...
99995   5.399600  13.880925  30.017482    96.440857    69.866221  1021.000303  1019.352931             30.006
99996   2.093954   9.948146  26.267022    89.187579    27.937236  1010.975868  1021.133446             26.200
99997  33.161916  16.080922  34.761429    87.499870    43.554883  1019.855631  1007.072557             34.800
99998   7.581479  37.648384  41.495577    22.999616    58.598362  1033.872152  1033.097344             41.454
99999  29.542903  16.851645  35.873694    57.528733    72.695171  1006.445146  1014.347608             35.794

[100000 rows x 8 columns]
```

---

## Requirements

- Flask==3.0.3
- Flask-SQLAlchemy==3.1.1
- python-dateutil==2.9.0.post0
- SQLAlchemy==2.0.36
- scikit-learn==1.5.2
- joblib==1.4.2
- numpy==2.1.1
- pandas==2.2.3

---

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Load CSV into a DB:
    ```bash
    python import_csv.py
    ```

2. Train the model (optional, if the model is not pre-trained):
   ```bash
   python ml_model.py
   ```

3. Start the application:
   ```bash
   flask run
   ```

4. Navigate to `http://127.0.0.1:5000/predict` to access the rainfall prediction form.

---

## License

This project is licensed under the MIT License.
