# Task Manager API

A secure, RESTful backend service built with **Python** and **Flask**. This API allows users to manage their personal tasks with full CRUD functionality, protected by **JWT (JSON Web Token)** authentication.

## 🚀 Features

* **User Authentication**: Secure Sign-up and Login system.
* **JWT Security**: Protected routes ensure users can only access their own data.
* **Task Management**: Full CRUD (Create, Read, Update, Delete) capabilities.
* **Filtering**: Fetch tasks by status (Completed/Pending) or category (Work, Personal, etc.).
* **Database Integration**: Lightweight and efficient data storage using SQLite.


## 🛠️ Tech Stack

| Technology | Purpose |
| --- | --- |
| **Python** | Primary Programming Language |
| **Flask** | Web Framework for API Development |
| **SQLite** | Relational Database |
| **Flask-JWT-Extended** | Authentication and Token Management |
| **SQLAlchemy** | ORM for Database Operations |


## 🚦 Getting Started

### Prerequisites

* Python 3.x installed.
* `uv` (Python package manager).

### Installation & Setup

1. **Clone the repository**:
```bash
git clone https://github.com/pheonix-coder/task-manager-api.git
cd task-manager-api
```


2. **Create a virtual environment**:
```bash
uv venv
```


3. **Install dependencies**:
```bash
uv sync
```


4. **Initialize the Database**:
```bash
python setup_db.py
```


5. **Run the application**:
```bash
flask run
```


The API will be available at `http://127.0.0.1:5000`.


## 📖 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/api/auth/signup` | Register a new user |
| `POST` | `/api/auth/login` | Login and receive a JWT token |

### Task Endpoints (Requires JWT)

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/tasks` | Get all tasks for the logged-in user |
| `POST` | `/api/tasks` | Create a new task |
| `GET` | `/api/tasks/<id>` | Get details of a specific task |
| `PUT` | `/api/tasks/<id>` | Update a task's title, description, or status |
| `DELETE` | `/api/tasks/<id>` | Remove a task |

---

## 📂 Database Schema

The API utilizes two main tables in SQLite:

1. **Users**: Stores `id`, `username`, and `password_hash`.
2. **Tasks**: Stores `id`, `title`, `description`, `category`, `status`, and `user_id` (Foreign Key).
