# dailyDo Todo App

A full-stack todo application built with FastAPI and Next.js, featuring user authentication and task management.

## Project Overview

**dailyDo** is a modern todo application that allows users to register, log in, and manage their daily tasks. The application features a RESTful API backend and a responsive Next.js frontend with a clean, user-friendly interface.

## Technologies Used

### Backend
- **FastAPI** - Modern Python web framework for building APIs
- **SQLModel** - Combines SQLAlchemy and Pydantic for database ORM
- **PostgreSQL** - Relational database
- **Uvicorn** - ASGI server for running FastAPI
- **Python 3.12+**

### Frontend
- **Next.js 14** - React framework for production
- **React 18** - User interface library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Radix UI** - Unstyled accessible components
- **React Hot Toast** - Toast notifications

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **pgAdmin** - PostgreSQL database management interface

## Project Structure

```
├── backend/                    # FastAPI application
│   ├── todo_app/
│   │   ├── main.py            # FastAPI app initialization
│   │   ├── routers/           # API route handlers
│   │   │   ├── auth.py        # Authentication endpoints
│   │   │   ├── todo.py        # Todo CRUD endpoints
│   │   │   └── user.py        # User endpoints
│   │   ├── services/          # Business logic
│   │   │   ├── auth_services.py
│   │   │   ├── todo_services.py
│   │   │   └── user_services.py
│   │   ├── repositories/      # Data access layer
│   │   │   ├── todo_repository.py
│   │   │   └── user_repository.py
│   │   ├── schemas/           # Pydantic schemas
│   │   │   ├── auth_schemas.py
│   │   │   ├── todo_schemas.py
│   │   │   └── user_schemas.py
│   │   └── db/                # Database configuration
│   │       ├── connection.py
│   │       └── setting.py
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── dockerfile
│
├── frontend/                   # Next.js application
│   ├── src/
│   │   ├── app/               # Pages and layout
│   │   │   ├── page.tsx       # Main todo page
│   │   │   ├── login/         # Login page
│   │   │   └── register/      # Registration page
│   │   ├── components/        # Reusable React components
│   │   │   ├── TodoTable.tsx
│   │   │   ├── AddTask.tsx
│   │   │   ├── EditTask.tsx
│   │   │   ├── Task.tsx
│   │   │   └── ui/            # UI components (Radix)
│   │   ├── actions/           # Server actions
│   │   └── lib/               # Utility functions
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   └── dockerfile
│
├── docker-compose.yml         # Docker Compose configuration
└── README.md
```

## Existing Features

### Authentication & User Management
- **User Registration** - Create new user account with username and email
- **User Login** - Authenticate with username/email and password
- **Password Security** - Passwords are hashed using secure hashing algorithms
- **Token-Based Authentication** - JWT tokens for maintaining sessions
- **Get Current User** - Retrieve authenticated user profile

### Todo Management
- **Create Tasks** - Add new tasks with content and completion status
- **List Tasks** - View all tasks for the authenticated user
- **View Single Task** - Retrieve a specific task by ID
- **Update Tasks** - Modify task content and completion status
- **Delete Tasks** - Remove tasks from the list

### User Interface
- **Responsive Design** - Works on desktop and mobile devices
- **Login Page** - Clean login interface with username/email and password input
- **Registration Page** - Register new user accounts
- **Task Dashboard** - Main page displaying all user tasks in a table format
- **Add Task Modal** - Dialog to add new tasks
- **Edit Task** - Inline or modal-based task editing
- **Logout Functionality** - Secure session termination

### API Features
- **CORS Enabled** - Cross-Origin Resource Sharing for frontend communication
- **RESTful Design** - Standard HTTP methods (GET, POST, PUT, DELETE)
- **Error Handling** - Appropriate HTTP status codes and error messages

## How to Run the Backend

### Prerequisites
- Python 3.12 or higher
- PostgreSQL 13 or higher
- Docker and Docker Compose (recommended)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. **Create environment file (.env)**
   ```bash
   # .env file in the backend directory
   DATABASE_URL=postgresql://user:password@localhost:5432/dailydo
   TEST_DATABASE_URL=postgresql://user:password@localhost:5432/dailydo_test
   ```

3. **Install dependencies using Poetry**
   ```bash
   pip install poetry
   poetry install
   ```

4. **Run the server**
   ```bash
   poetry run uvicorn todo_app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs` (Swagger UI)
   - Alternative Documentation: `http://localhost:8000/redoc` (ReDoc)

## How to Run the Frontend

### Prerequisites
- Node.js 18 or higher
- npm or yarn package manager

### Setup Steps

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run development server**
   ```bash
   npm run dev
   ```

   The application will be available at `http://localhost:3000`

4. **Build for production**
   ```bash
   npm run build
   npm start
   ```

## Database Setup

### Using Docker Compose (Recommended)

1. **Create .env file in the project root**
   ```bash
   POSTGRES_USER=todouser
   POSTGRES_PASSWORD=todopassword
   POSTGRES_DB=dailydo
   PGADMIN_DEFAULT_EMAIL=admin@example.com
   PGADMIN_DEFAULT_PASSWORD=admin
   ```

2. **Start services**
   ```bash
   docker-compose up -d
   ```

   This will start:
   - PostgreSQL database on port 5432
   - pgAdmin interface on port 5050

3. **Access pgAdmin**
   - URL: `http://localhost:5050`
   - Email: admin@example.com
   - Password: admin

### Manual Setup (Without Docker)

1. **Install PostgreSQL** from https://www.postgresql.org/download/

2. **Create database**
   ```sql
   CREATE DATABASE dailydo;
   ```

3. **Update .env file** with PostgreSQL connection details

4. **Tables are automatically created** when the FastAPI server starts (via `create_tables()` in connection.py)

## API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT token |
| GET | `/auth/me` | Get current authenticated user |

### Todo Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/todos/` | Create a new todo task |
| GET | `/todos/` | Get all todos for current user |
| GET | `/todos/{id}` | Get a specific todo by ID |
| PUT | `/todos/{id}` | Update a todo task |
| DELETE | `/todos/{id}` | Delete a todo task |

### User Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users/` | Create a new user |
| GET | `/users/` | Get all users |
| GET | `/users/{id}` | Get a specific user by ID |
| DELETE | `/users/{id}` | Delete a user |

### Request/Response Examples

**Register User**
```json
POST /auth/register
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Login**
```json
POST /auth/login
{
  "username": "john_doe",
  "password": "securepassword123"
}

Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Create Todo**
```json
POST /todos/
{
  "content": "Buy groceries",
  "is_completed": false
}
```

---

Built with ❤️ by Em-Aar
