import os

import joblib
import pandas as pd
from loguru import logger
from settings import MODEL_PATH
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def load_data():
    # Load dataset
    df = pd.read_csv(os.path.join(os.getcwd(), "app", "data", "dataset.csv"))
    return df


def preprocess_data(df: pd.DataFrame):
    # Handling null values
    imputer = SimpleImputer(fill_value=0)
    df_imputed = df.copy()
    df_imputed[
        [
            "Age",
            "Annual_Income",
            "Credit_Score",
            "Loan_Amount",
            "Number_of_Open_Accounts",
        ]
    ] = imputer.fit_transform(
        df[
            [
                "Age",
                "Annual_Income",
                "Credit_Score",
                "Loan_Amount",
                "Number_of_Open_Accounts",
            ]
        ]
    )

    # Splitting the data into features and target
    X = df_imputed.drop("Loan_Approval", axis=1)
    y = df_imputed["Loan_Approval"]

    # Splitting the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.01, random_state=42
    )

    return X_train, X_test, y_train, y_test


def train_model(X_train, X_test, y_train, y_test):
    # Training the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model


def save_model(model):
    # Save the model
    joblib.dump(model, MODEL_PATH)
    logger.info(f"Model saved successfully at {MODEL_PATH}")


# # Predictions
# y_pred = model.predict(X_test)
# print(y_pred)


if __name__ == "__main__":
    logger.info("Model pipeline started...")
    logger.info("Loading data...")
    df = load_data()

    logger.info("Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess_data(df)

    logger.info("Training model...")
    model = train_model(X_train, X_test, y_train, y_test)

    logger.info("Saving model...")
    save_model(model)
