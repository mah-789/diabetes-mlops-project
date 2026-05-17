import joblib

model = joblib.load("diabetes_model.pkl")
print("Model loaded successfully")

cols = joblib.load("training_columns.pkl")
print(cols)