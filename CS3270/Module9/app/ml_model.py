import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

# Load the dataset
data = pd.read_csv("../data/Weather Training Data.csv")

# Handle missing values
data.fillna(data.median(numeric_only=True), inplace=True)
data.fillna('Unknown', inplace=True)
data = data.drop(columns='row ID')

# Convert categorical variables
data['RainToday'] = data['RainToday'].map({'Yes': 1, 'No': 0})  # Binary encoding
data = pd.get_dummies(data, columns=['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm'], drop_first=True)

# Define features (X) and target (y)
X = data.drop(['RainTomorrow'], axis=1, errors='ignore')
y = data['Rainfall']  # Set Rainfall as the target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the regression model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f'MAE: {mean_absolute_error(y_test, y_pred)}')
print(f'MSE: {mean_squared_error(y_test, y_pred)}')
print(f'R² Score: {r2_score(y_test, y_pred)}')

# Save the model
with open('rainfall_predictor_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

#print(X.dtypes.to_string())
