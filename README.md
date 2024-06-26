# Python Challenge: Secure Backend Service for MediaMarktSaturn


## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
    - [Register a New User](#register-a-new-user)
    - [Obtain a Token](#obtain-a-token)
    - [Test Access for Unauthenticated Users](#test-access-for-unauthenticated-users)
    - [Test Access for Authenticated Users](#test-access-for-authenticated-users)
4. [Docker Setup](#docker-setup)
5. [Testing](#testing)
    - [Test Setup](#test-setup)
    - [Test Cases](#test-cases)
        - [Test Access for Unauthenticated Users](#test-access-for-unauthenticated-users)
        - [Test Access for Authenticated Users](#test-access-for-authenticated-users)
6. [API Documentation](#api-documentation)
    - [Swagger UI](#swagger-ui)
    - [Redoc](#redoc)
7. [Cloud Deployment](#cloud-deployment)
8. [CI/CD Pipeline with GitHub Actions](#cicd-pipeline-with-github-actions)


## Introduction
TThis project is a backend service for managing security-related data, developed for MediaMarktSaturn. It provides a scalable and secure RESTful API for CRUD operations on security records. The service is implemented using Django and Django REST Framework and is designed to be deployable on ~~Kubernetes~~.

## Installation
To set up the project locally, follow these steps:
1. **Clone the repository from GitHub:** [Repository Link](https://github.com/nimodb/MediaMarktSaturn)

2. **Navigate to the project directory.**

3. **Create a virtual environment:**
    ```bash
     python -m venv env
    ```

4. **Activate the virtual environment:**
    
    On Windows:
    ```bash
    .\env\Scripts\activate
    ```
    On macOS and Linux:
    ```bash
    source env/bin/activate
    ```

5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
6. **Run migrations to apply database schema:**
    ```bash
    python manage.py migrate
    ```

7. **(Optional) Load initial data:**
    ```bash
    python manage.py loaddata initial_data.json
    ```

8. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

9. **Access the API Root at http://127.0.0.1:8000/api/**


## Usage

### Register a New User
To register a new user, send a POST request to the following endpoint:
  ```http
  POST http://127.0.0.1:8000/register/
  Content-Type: application/json

  {
    "username": "TestUser",
    "password": "TestPassword",
    "email": "testEmail@domain.com"
  }
  ```

### Obtain a Token
To obtain a token for authentication, send a POST request to the following endpoint:
  ```http
  POST http://127.0.0.1:8000/api-token-auth/
  Content-Type: application/json
  
  {
    "username": "TestUser",
    "password": "TestPassword"
  }
  ```

### Test Access for Unauthenticated Users

To test that unauthenticated users cannot list security records, send a GET request to the following endpoint:
  ```http
  GET http://127.0.0.1:8000/api/security-records/
  ```

To test that unauthenticated users cannot retrieve a security record by ID, send a GET request to the following endpoint:
  ```http
  GET http://127.0.0.1:8000/api/security-records/5/
  ```

To test that unauthenticated users cannot create a new security record, send a POST request to the following endpoint:
  ```http
  POST http://127.0.0.1:8000/api/security-records/
  Content-Type: application/json
  
  {
    "name": "New Security Record",
    "description": " Description of the new security record."
  }
  ```

To test that unauthenticated users cannot update a security record, send a PUT request to the following endpoint:
  ```http
  PUT http://127.0.0.1:8000/api/security-records/1/
  Content-Type: application/json
  
  {
    "name": "Updated Security Record",
    "description": "Updated description of the security record."
  }
  ```

To test that unauthenticated users cannot delete a security record, send a DELETE request to the following endpoint:
  ```http
  DELETE http://127.0.0.1:8000/api/security-records/1/
  ```


### Test Access for Authenticated Users
To test that authenticated users can list security records, send a GET request to the following endpoint with the authorization token:
  ```http
  GET http://127.0.0.1:8000/api/security-records/
  Authorization: Token <token>
  ```

To test that authenticated users can retrieve a security record by ID, send a GET request to the following endpoint with the authorization token:
  ```http
  PUT http://127.0.0.1:8000/api/security-records/1/
  Authorization: Token <token>
  ```

To test that authenticated users can create a new security record, send a POST request to the following endpoint with the authorization token:
  ```http
  POST http://127.0.0.1:8000/api/security-records/
  Content-Type: application/json
  Authorization: Token <token>
  
  {
    "name": "New Security Record",
    "description": " Description of the new security record."
  }
  ```

To test that authenticated users can update a security record, send a PUT request to the following endpoint with the authorization token:
  ```http
  PUT http://127.0.0.1:8000/api/security-records/1/
  Content-Type: application/json
  Authorization: Token <token>
  
  {
    "name": "Updated Security Record",
    "description": "Updated description of the security record."
  }
  ```

To test that authenticated users can delete a security record, send a DELETE request to the following endpoint with the authorization token:
  ```http
  DELETE http://127.0.0.1:8000/api/security-records/1/
  Authorization: Token <token>
  ```


## Docker Setup
To run the project using Docker, follow these steps:

1. **Install Docker and Docker Compose if you haven't already.**

2. **Clone the repository from GitHub:** [Repository Link](https://github.com/nimodb/MediaMarktSaturn)

3. Navigate to the project directory.

4. **Build the Docker image:**
   ```bash
   docker-compose build
   ```

5. **Run the Docker containers:**
    ```bash
   docker-compose up
   ```


## Testing
### Test Setup
The **'tests.py'** file contains test cases for the API endpoints defined in the Django application. These test cases are written using Django's testing framework and the Django REST Framework's **'APITestCase'**.

The **'setUp'** method is called before each test case to set up the necessary objects and configurations for testing. In this setup:

1. An instance of **'APIClient'** is created to simulate HTTP requests.
2. A test user is created using Django's **'User'** model.
3. An authentication token is generated for the test user using Django REST Framework's **'Token'** model.
4. A test security record is created using the application's **'SecurityRecord'** model.


### Test Cases
The test cases are organized into two main sections:
1. Test Access for *'Unauthenticated'* Users
2. Test Access for *'Authenticated'* Users

#### Test Access for Unauthenticated Users
These test cases ensure that unauthenticated users cannot perform certain actions (**CRUD**) on the API endpoints.

- `test_list_records_unauthenticated`: Checks that unauthenticated users cannot list security records.
- `test_retrieve_record_unauthenticated`: Checks that unauthenticated users cannot retrieve a security record by ID.
- `test_create_record_unauthenticated`: Checks that unauthenticated users cannot create a new security record.
- `test_update_record_unauthenticated`: Checks that unauthenticated users cannot update a security record.
- `test_delete_record_unauthenticated`: Checks that unauthenticated users cannot delete a security record.

*(5 Tests)*

#### Test Access for Authenticated Users
These test cases ensure that authenticated users can perform actions on the API endpoints after authentication.

- `test_list_records_authenticated`: Checks that authenticated users can list security records.
- `test_retrieve_record_authenticated`: Checks that authenticated users can retrieve a security record by ID.
- `test_create_record_authenticated`: Checks that authenticated users can create a new security record.
- `test_update_record_authenticated`: Checks that authenticated users can update a security record.
- `test_delete_record_authenticated`: Checks that authenticated users can delete a security record.

*(5 Tests)*

## API Documentation
The API endpoints are documented using *'drf-spectacular'*. You can access the API documentation in two format:

### Swagger UI
Swagger UI provides an interactive interface for exploring the API. You can access it at:
- [Swagger UI](http://127.0.0.1:8000/api/docs/swagger/)

### Redoc 
Redoc provides a different view of the API documentation. You can access it at:
- [Redoc](http://127.0.0.1:8000/api/docs/redoc/)

*Both interfaces allow you to explore the available endpoints, view request and response schemas, and interact with the API directly from the documentation.*


## Cloud Deployment

### ~~Kubernetes Deployment~~

To deploy this project on a Kubernetes: 

1. **For Google Cloud Platform (GKE)**
    ```bash

    ```

2. **For AWS (EKS)**
    ```bash

    ```

3. **For Microsoft Azure (AKS)**
    ```bash

    ```

4. **Verify the deployment and get the external IP of the service:**
  - Ensure you have *'kubectl'* installed and configured for your cloud provider.
  - Apply the Development and Service file
      ```bash
        kubectl apply -f development.yaml
        kubectl apply -f service.yaml
      ```
  - verify that the pods are running:
      ```bash
        kubectl get pods 
      ```
  - Get the external IP address of the service:
      ```bash
        kubectl get svc SERVICE_NAME
      ```
  
5. **Access the Django application using the external IP.**


## CI/CD Pipeline with GitHub Actions

This project uses GitHub Actions to automate CI process. The CI/CD pipeline is set up to run tests automatically whenever code changes are pushed to the `main` branch.