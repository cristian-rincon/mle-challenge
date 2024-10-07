# Machine Learning Engineering Assignment

[![CI for FastAPI Loan Approval API](https://github.com/cristian-rincon/mle-challenge/actions/workflows/ci.yaml/badge.svg)](https://github.com/cristian-rincon/mle-challenge/actions/workflows/ci.yaml)

- [Machine Learning Engineering Assignment](#machine-learning-engineering-assignment)
  - [Assignment](#assignment)
  - [Proposed Solution](#proposed-solution)
    - [FastAPI Loan Approval Prediction API](#fastapi-loan-approval-prediction-api)
      - [Features](#features)
    - [Project Structure](#project-structure)
    - [Requirements](#requirements)
    - [Building and Running the Application](#building-and-running-the-application)
      - [Steps to Trigger CI/CD](#steps-to-trigger-cicd)
      - [Pulling the Docker Image from GitHub Packages Registry](#pulling-the-docker-image-from-github-packages-registry)
      - [Authentication](#authentication)
      - [Running Tests](#running-tests)
      - [\[Running from local\] Option 1: Using Docker Compose (recommended)](#running-from-local-option-1-using-docker-compose-recommended)
      - [\[Running from local\] Option 2: Running with Docker directly](#running-from-local-option-2-running-with-docker-directly)
      - [\[Running from local\] Option 3: Running without Docker](#running-from-local-option-3-running-without-docker)
    - [Key Points in the Documentation](#key-points-in-the-documentation)
    - [API Endpoints](#api-endpoints)
    - [Notes](#notes)
    - [License](#license)
    - [Explanation](#explanation)

This assignment is expected to be completed by a Machine Learning Engineer within 3-4 hours.

## Assignment

Your teammate Mike gave you a Machine Learning Model that needs to be deployed, examine the model.py file.
Your task is to add the necessary components to get this model to production,
this model is crucial for the company's success, so it should be available receive and predict data upon request.
This model should work for any cloud provider. Also this is the model v1 of a series of versions to be deployed.
(Optional): you can come up with a better model pipeline if you think the one provided is not suitable for this case.

Add all the necessary files, code, docs, to improve this repository and make this model ready to be shipped.

Note: You can reach out to us through email at <marcos.soto@qubika.com> or <anibal.jasin@qubika.com> but since
you could be working off hours we suggest you can write down questions and assumptions you came across
and what decision you take e.g. “I’m gonna assume this project should have X because of Y” or
“I would ask about if there is some ACL for this model, so I would assume X”.

Some general considerations and guidance:

- It is expected that you include files, code, documentation, and any other resources you find useful in the new repository you create.
- A fully production-ready model deployed in the cloud is not required.
- You are not expected to spend money on cloud services, ensuring everything works locally is sufficient.
- It is acceptable if some aspects are not fully functional, our goal is to understand your approach to this problem.
- In case you don’t finish the assignment, you can add what other things you would do in the README.md.

---------------------------------------------------------------------------
version=0.0.3

---------------------------------------------------------------------------

## Proposed Solution

Here’s a `README.md` file that documents how to set up and run your FastAPI application using Docker and Docker Compose:

### FastAPI Loan Approval Prediction API

This project is a FastAPI-based application that predicts loan approval based on various user inputs. It uses machine learning (Logistic Regression) to provide predictions.

#### Features

- Predict loan approval based on input features such as age, annual income, credit score, loan amount, loan duration, and more.
- Containerized using Docker for easy deployment.
- Uses Poetry as the Python dependency manager.
- Offers flexibility to run with or without Docker Compose.

### Project Structure

```bash
.
├── app/                    # Application source code
│   ├── data/               # Dataset folder
│   ├── model.py            # Model training script
│   ├── settings.py         # Application Core Settings
│   └── api.py              # FastAPI application
├── Dockerfile              # Dockerfile for building the app
├── docker-compose.yml      # Docker Compose configuration
├── pyproject.toml          # Poetry configuration file
├── poetry.lock             # Poetry lock file
└── README.md               # Project documentation
```

### Requirements

- **Docker**: Install Docker from [here](https://docs.docker.com/get-docker/).
- **Docker Compose**: Install Docker Compose from [here](https://docs.docker.com/compose/install/).

### Building and Running the Application

If you want to build and upload the Docker image to GitHub Packages, use the GitHub Actions CI/CD pipeline provided in the `.github/workflows/cd.yml` file.

#### Steps to Trigger CI/CD

1. Make changes to your code and push them to the `main` branch.
2. The CI/CD pipeline will build the Docker image and save it as an artifact.

#### Pulling the Docker Image from GitHub Packages Registry

Once the image is built and pushed to the GitHub Packages Registry, you can pull it using the following command:

```bash
docker pull ghcr.io/cristian-rincon/loans-api:latest
```

#### Authentication

To pull images from the GitHub Packages Registry, you may need to authenticate using your GitHub Personal Access Token. You can log in using the following command:

```bash
echo <YOUR_PERSONAL_ACCESS_TOKEN> | docker login ghcr.io -u <YOUR_GITHUB_USERNAME> --password-stdin
```

Replace `<YOUR_PERSONAL_ACCESS_TOKEN>` with your actual token.

#### Running Tests

To run the tests for the API, use the following command:

```bash
poetry run pytest
```

#### [Running from local] Option 1: Using Docker Compose (recommended)

1. **Build and run the application using Docker Compose**:

   ```bash
   docker-compose up --build
   ```

2. **Access the API**:

   Open your browser or API tool (e.g., Postman) and navigate to:

   ```bash
   http://localhost:8000
   ```

   The FastAPI app will be running on port `8000`. You can also access the interactive Swagger documentation at:

   ```bash
   http://localhost:8000/docs
   ```

3. **Stop the application**:

   To stop the running containers, press `CTRL+C` or run:

   ```bash
   docker-compose down
   ```

#### [Running from local] Option 2: Running with Docker directly

1. **Build the Docker image**:

   ```bash
   docker build -t loans-api .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 8000:8000 loans-api
   ```

3. **Access the API**:

   Open your browser or API tool (e.g., Postman) and navigate to:

   ```bash
   http://localhost:8000
   ```

   The FastAPI app will be running on port `8000`. You can also access the interactive Swagger documentation at:

   ```bash
   http://localhost:8000/docs
   ```

4. **Stop the container**:

   Press `CTRL+C` in the terminal running the container or find the container ID with:

   ```bash
   docker ps
   ```

   Then stop the container:

   ```bash
   docker stop <container-id>
   ```

#### [Running from local] Option 3: Running without Docker

1. **Install dependencies**:

   This project uses [Poetry](https://python-poetry.org/) to manage dependencies. If you don't have Poetry installed, you can install it with:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   After installing Poetry, install the project dependencies:

   ```bash
   poetry install
   ```

2. **Run the model training script**:

   ```bash
   poetry run python app/model.py
   ```

3. **Run the FastAPI app**:

   ```bash
   poetry run uvicorn app.api:loans_api --reload
   ```

4. **Access the API**:

   Open your browser or API tool (e.g., Postman) and navigate to:

   ```bash
   http://localhost:8000
   ```

   The FastAPI app will be running on port `8000`. You can also access the interactive Swagger documentation at:

   ```bash
   http://localhost:8000/docs
   ```

### Key Points in the Documentation

- **Pulling the Docker Image**: Clear instructions on how to pull the Docker image from GitHub Packages, including the necessary commands.
  
- **Authentication**: Guidance on authenticating to GitHub Packages using a Personal Access Token, as this may be necessary to pull images.

- **Example Command**: Providing an example pull command helps clarify the process for users.

This additional documentation will help users understand how to access and use the Docker image from GitHub Packages Registry effectively. Let me know if you need any further adjustments!

### API Endpoints

- `GET /`: Redirects to `/docs`.
- `GET /docs`: OpenAPI interactive documentation for the API.
- `POST /predict`: Predict loan approval. Accepts the following input:

  ```json
  {
    "Age": 35,
    "Annual_Income": 50000,
    "Credit_Score": 700,
    "Loan_Amount": 20000,
    "Loan_Duration_Years": 5,
    "Number_of_Open_Accounts": 3,
    "Had_Past_Default": 0,
    "Loan_Approval": 0,
  }
  ```

  Example Response:

  ```json
  {
    "Loan_Approval": 1
  }
  ```

### Notes

- Ensure that the dataset is placed in the `./app/data` directory before running the application.
- The first run will train the model using the dataset provided, so it may take some time depending on the size of the data.

### License

This project is licensed under the MIT License.

### Explanation

1. **Introduction**: Provides an overview of the project and its features.
2. **Project Structure**: Displays the project layout for easy navigation.
3. **Requirements**: Lists necessary tools like Docker and Docker Compose.
4. **Running the Application**: Provides step-by-step instructions for running the app with Docker Compose, Docker, or without Docker.
5. **API Endpoints**: Describes the available API routes and provides example requests/responses.
6. **Notes**: Includes reminders about the dataset and model training time.

This `README.md` should provide all the necessary documentation for setting up, running, and using the FastAPI application.
