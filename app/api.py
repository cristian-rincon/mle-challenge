import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sklearn.impute import SimpleImputer

from app.settings import MODEL_PATH

# Initialize FastAPI
loans_api = FastAPI(
    title="Loan Approval Prediction API",
    description="API to predict loan approval using a Logistic Regression model",
    version="0.1",
)

# Load the saved model
model = joblib.load(MODEL_PATH)


# Define the request body using Pydantic
class LoanApplication(BaseModel):
    Age: float
    Annual_Income: float
    Credit_Score: float
    Loan_Amount: float
    Loan_Duration_Years: float
    Number_of_Open_Accounts: float
    Had_Past_Default: int  # Assuming this is a binary (0/1) feature
    Loan_Approval: int  # This field is not required for prediction


# Root endpoint
@loans_api.get("/")
def read_root():
    return RedirectResponse(url="/docs")


# Prediction endpoint
@loans_api.post("/predict")
def predict_loan(loan_app: LoanApplication):
    # Convert input data to DataFrame
    input_data = pd.DataFrame([loan_app.dict()])

    # Impute missing values (if any)
    imputer = SimpleImputer(fill_value=0)
    input_data_imputed = imputer.fit_transform(input_data)

    # Predict using the trained model
    prediction = model.predict(input_data_imputed)

    # Return the prediction result
    return {"Loan_Approval": int(prediction[0])}
