# 🩺 Diabetes Prediction System (MLOps Project)

## Project Overview
This project is an end-to-end Machine Learning and MLOps system designed to predict diabetes based on patient medical data. It includes data preprocessing, model training, evaluation, and deployment using FastAPI.

The goal of this project is to demonstrate a complete ML pipeline from data to production-ready API.


## ⚙️ Tech Stack
- Python
- Pandas & NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib


## Workflow

### 1. Data Preprocessing
- Removed unnecessary columns (ID, No_Pation)
- Handled missing values
- Encoded categorical variables (Gender, Class)

### 2. Exploratory Data Analysis (EDA)
- Distribution analysis (Age, BMI)
- Relationship between features (HbA1c, BMI, Age)
- Visual insights using Matplotlib/Seaborn

### 3. Model Training
- Trained multiple models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - SVM
  - KNN
- Evaluated using Accuracy, Precision, Recall, and F1-score
- Selected the best performing model

### 4. Model Saving
- Saved trained model using `joblib`
- Stored feature columns for inference consistency

### 5. API Deployment (FastAPI)
- Created REST API using FastAPI
- Implemented Pydantic validation for input data
- Built `/predict` endpoint for real-time predictions


### How to Run Project

### Step 1: Install dependencies

pip install -r requirements.txt