# Flask-Project-0

## Overview

This project focuses on creating a Flask application that includes endpoints for:

1. Collecting user data.
2. Fetching all user data via `/users`.
3. Fetching specific user data via `/users/<id>`.

The primary goal is to build a functional backend with features such as data validation, error handling, and database interaction.

---

## Project Setup

### **1. Environment Setup**

To set up the environment, I started by installing Flask:

```bash
pip install flask
```

Additionally, I installed supporting libraries:

- **Flask-SQLAlchemy**: For managing the database using Python.
- **Flask-Marshmallow & Marshmallow-SQLAlchemy**: For serializing Python objects to JSON and vice versa.
- **Python-dotenv**: To manage environment variables.
- **Pytest**: For testing the application.

---

### **2. Project Structure**

```plaintext
flask_project/
├── app/
│   ├── __init__.py         # Initializes the app and sets up the application factory
│   ├── database.py         # Database setup and ORM integration
│   ├── models.py           # Defines the database models
│   ├── routes.py           # Contains route definitions for user endpoints
├── venv/                   # Virtual environment files
├── app.db                  # SQLite database file
├── config.py               # Application configuration settings
├── requirements.txt        # Project dependencies
├── run.py                  # Entry point for running the Flask app
└── README.md               # Project documentation
```

---

## Thought Process

### **Step 1: Setting Up the Database**

1. Initialized the database with the Flask app.
2. Created tables using SQLAlchemy models to define the structure.
3. Serialized database objects using Marshmallow schemas for JSON formatting.

### **Step 2: Implementing Models**

1. Defined the `User` model with attributes such as `id`, `username`, `email`, and `password`.
2. Wrote Marshmallow schema to handle serialization and deserialization of the `User` model.

### **Step 3: Building Routes**

- Created API endpoints to:

  - **Create a User**:
    - Validates input data.
    - Checks if the user already exists.
    - Hashes the password for security.
    - Adds the user to the database.
  - **Retrieve All Users**:

    - Fetches and returns all user data.

  - **Retrieve a Single User**:
    - Fetches user data by ID via `/users/<id>`.

### **Step 4: Handling Configurations**

- Used a `config.py` file to store environment variables and settings and deployment config

### **Step 5: Initializing the Application**

- Used the `__init__.py` file to:
  - Initialize the app.
  - Load configurations.
  - Register blueprints for modular routes.
  - Set the API prefix (e.g., `/api/v1`).

### **Step 6: Running the Application**

- Created `run.py` to serve as the entry point, running the `create_app()` function defined in `__init__.py`.

---

## Endpoints

### **1. Create a User**

- **Endpoint**: `/users`
- **Method**: POST
- **Description**: Accepts user data, validates it, hashes the password, and saves it to the database.
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "Password123!",
    "confirm_password": "Password123!"
  }
  ```

### **2. Fetch All Users**

- **Endpoint**: `/users`
- **Method**: GET
- **Description**: Retrieves all user records from the database.

### **3. Fetch a Single User**

- **Endpoint**: `/users/<id>`
- **Method**: GET
- **Description**: Retrieves a specific user's data by their ID.

---

## Error Handling

- **Database Rollback**:
  - Ensures database integrity by rolling back incomplete transactions in case of errors.
- **Validation Errors**:
  - Input validation is performed using helper functions.
- **Custom Error Responses**:
  - Returns user-friendly JSON responses with appropriate HTTP status codes.

<!-- ---

## Future Improvements

1. Add token-based authentication for securing endpoints.
2. Implement a frontend to interact with the API.
3. Use Flask-Migrate for managing database migrations.

--- -->

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flask_project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python3 run.py
   ```
4. Access the API at `https://flask-project-0.onrender.com/api/v1/users`.
