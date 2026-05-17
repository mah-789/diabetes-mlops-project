from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("diabetes_model.pkl")
columns = joblib.load("training_columns.pkl")

class PatientData(BaseModel):
    age: float
    urea: float
    cr: float
    hba1c: float
    chol: float
    tg: float
    hdl: float
    ldl: float
    vldl: float
    bmi: float
    gender: str

@app.get("/")
def home():
    return {"status": "API is running"}

@app.post("/predict")
def predict(data: PatientData):
    input_data = data.dict()

    input_data["Gender_M"] = 1 if input_data["gender"] == "M" else 0
    input_data.pop("gender")

    df = pd.DataFrame([input_data])

    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]

    return {"prediction": int(prediction)}