# User Management API

This project is a simple **User Management API** built with **FastAPI** and **MongoDB**. It allows you to create, retrieve, update, and delete user data.

## Features
- Create a user
- Retrieve a user by ID
- List all users
- Update user details
- Delete a user

## Technologies Used
- **FastAPI**
- **MongoDB**
- **Uvicorn**

## Installation and Setup

1. **Clone the Repository**
   
bash
   git clone <repository_url>
   cd fastapi-mongodb-api


2. **Create a Virtual Environment**
   
bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate


3. **Install Dependencies**
   
bash
   pip install fastapi uvicorn pymongo


4. **Start MongoDB**
   Ensure MongoDB is running on your machine. The default connection URI is mongodb://localhost:27017. Update it in the main.py file if necessary.

5. **Run the Application**
   
bash
   uvicorn main:app --reload


6. **Access API Documentation**
   Open your browser and navigate to:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

### 1. Create User
**POST** /users/
- **Request Body (Postman Example):**
  
json
  {
    "name": "Rishitaa",
    "email": "rishit@gmail.com",
    "password": "1243@rishit"
  }

- **Response:**
  
json
  {
    "id": "<generated_id>",
    "message": "User created successfully"
  }


### 2. Retrieve User
**GET** /users/{user_id}
- **Response (Postman Example):**
  
json
  {
    "_id": "<user_id>",
    "name": "Rishitaa",
    "email": "rishit@gmail.com",
    "password": "1243@rishit"
  }


### 3. List All Users
**GET** /users/
- **Response (Postman Example):**
  
json
  [
    {
      "_id": "<user_id>",
      "name": "Rishitaa",
      "email": "rishit@gmail.com",
      "password": "1243@rishit"
    }
  ]


### 4. Update User
**PUT** /users/{user_id}
- **Request Body (Postman Example):**
  
json
  {
    "name": "Updated Name",
    "email": "updated.email@gmail.com"
  }

- **Response:**
  
json
  {
    "message": "User updated successfully"
  }


### 5. Delete User
**DELETE** /users/{user_id}
- **Response (Postman Example):**
  
json
  {
    "message": "User deleted successfully"
  }


## Testing the API

You can test the API endpoints using:

- **Postman**: Create requests for each endpoint and test them by sending the required data.
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
