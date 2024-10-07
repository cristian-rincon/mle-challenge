import pytest
from fastapi.testclient import TestClient
from app.api import loans_api

# Initialize the test client
client = TestClient(loans_api)

# Test for the root endpoint (redirection to /docs)
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.url == "http://testserver/docs"

# Mock data for the loan application
valid_loan_application = {
    "Age": 35,
    "Annual_Income": 50000,
    "Credit_Score": 700,
    "Loan_Amount": 20000,
    "Loan_Duration_Years": 5,
    "Number_of_Open_Accounts": 3,
    "Had_Past_Default": 0,
    "Loan_Approval": 1  # Although this field is not required for prediction
}

# Test for valid prediction
def test_predict_valid_loan():
    response = client.post("/predict", json=valid_loan_application)
    assert response.status_code == 200
    assert "Loan_Approval" in response.json()
    assert isinstance(response.json()["Loan_Approval"], int)

# Test for missing field (should fail with validation error)
def test_predict_invalid_missing_field():
    invalid_application = valid_loan_application.copy()
    del invalid_application["Age"]  # Remove a required field

    response = client.post("/predict", json=invalid_application)
    assert response.status_code == 422  # 422 Unprocessable Entity for validation errors

# Test for invalid data types
def test_predict_invalid_data_type():
    invalid_application = valid_loan_application.copy()
    invalid_application["Age"] = "thirty-five"  # Invalid data type

    response = client.post("/predict", json=invalid_application)
    assert response.status_code == 422  # 422 Unprocessable Entity for validation errors
