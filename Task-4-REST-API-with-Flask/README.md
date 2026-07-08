# Elevate Labs - Task 4: REST API with Flask

## 📌 Objective
Build a REST API using Flask to manage user data with CRUD operations (Create, Read, Update, Delete).

## 🛠 Technologies Used
- Python
- Flask
- Postman

## 📂 Project Structure

```
Elevate-Labs-Task-4/
│
├── app.py
├── requirements.txt
└── README.md
```

## 🚀 API Endpoints

### GET /users
Returns all users.

### POST /users
Adds a new user.

Example:

```json
{
    "name": "Aisha",
    "age": 19
}
```

### PUT /users/<id>
Updates an existing user.

Example:

```json
{
    "name": "Aisha Khan",
    "age": 20
}
```

### DELETE /users/<id>
Deletes a user by ID.

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python app.py
```

3. Test the API using Postman.
