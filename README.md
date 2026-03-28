# dailyDo Todo App

A full-stack todo application built with FastAPI and Next.js, featuring user authentication and task management.

---

## Student Information

- - **Name:** Trinh Quang Hien
- **Student ID:** 23632591

---

## Project Overview

**dailyDo** is a modern todo application that allows users to register, log in, and manage their daily tasks. The project combines a RESTful FastAPI backend with a responsive Next.js frontend to deliver a clean task-management experience for desktop and mobile users.

The application is organized as a monorepo with separate `backend` and `frontend` services, plus Docker-based infrastructure for PostgreSQL and pgAdmin.

## Key Features

### Authentication and User Management
- User registration with username, email, and password
- Login using either username or email
- Secure password hashing with `passlib`
- JWT-based authentication for protected routes
- Authenticated profile lookup via `/auth/me`

### Todo Management
- Create new tasks
- Retrieve all tasks for the authenticated user
- Filter tasks by search term and completion status
- Retrieve a single task by ID
- Update task content and completion state
- Delete existing tasks

### User Interface
- Responsive layout built with Next.js and Tailwind CSS
- Dedicated login and registration screens
- Main dashboard for viewing and managing todos
- Modal and reusable UI components for task operations
- Toast notifications and interactive UI feedback

### API and Infrastructure
- RESTful backend powered by FastAPI
- Automatic OpenAPI documentation with Swagger UI and ReDoc
- PostgreSQL database integration through SQLModel
- Docker Compose setup for local multi-service development
- pgAdmin included for database inspection and management

## Technology Stack

### Backend
- **FastAPI** for the REST API
- **SQLModel** for ORM and schema modeling
- **PostgreSQL** as the relational database
- **Uvicorn** as the ASGI server
- **Python 3.12+**

### Frontend
- **Next.js 14** with the App Router
- **React 18**
- **TypeScript**
- **Tailwind CSS**
- **Radix UI**
- **React Hot Toast**

### Infrastructure
- **Docker**
- **Docker Compose**
- **pgAdmin**

## Project Structure

```text
FASTAPI/
|-- backend/                    # FastAPI application
|   |-- todo_app/
|   |   |-- main.py            # FastAPI app initialization
|   |   |-- routers/           # API route handlers
|   |   |   |-- auth.py        # Authentication endpoints
|   |   |   |-- todo.py        # Todo CRUD endpoints
|   |   |   `-- user.py        # User endpoints
|   |   |-- services/          # Business logic layer
|   |   |-- repositories/      # Data access layer
|   |   |-- schemas/           # SQLModel and request/response schemas
|   |   `-- db/                # Database configuration
|   |-- pyproject.toml
|   |-- requirements.txt
|   `-- Dockerfile
|-- frontend/                  # Next.js application
|   |-- src/
|   |   |-- app/               # App Router pages and layout
|   |   |-- actions/           # Server actions
|   |   |-- components/        # Reusable UI components
|   |   `-- lib/               # Shared utilities
|   |-- package.json
|   |-- tailwind.config.ts
|   `-- Dockerfile
|-- docker-compose.yml         # Multi-container local environment
`-- README.md
```

## Existing Features

### Authentication and User Management
- **User Registration** - Create a new user account with username and email
- **User Login** - Authenticate with username/email and password
- **Password Security** - Passwords are hashed using secure hashing algorithms
- **Token-Based Authentication** - JWT tokens for maintaining sessions
- **Get Current User** - Retrieve the authenticated user profile

### Todo Management
- **Create Tasks** - Add new tasks with content and completion status
- **List Tasks** - View all tasks for the authenticated user
- **View Single Task** - Retrieve a specific task by ID
- **Update Tasks** - Modify task content and completion status
- **Delete Tasks** - Remove tasks from the list
- **Filtering Support** - Filter by search text and completion status

### User Interface
- **Responsive Design** - Works on desktop and mobile devices
- **Login Page** - Clean login interface with username/email and password input
- **Registration Page** - Create new user accounts
- **Task Dashboard** - Main page displaying user tasks
- **Add Task Modal** - Dialog to add new tasks
- **Edit Task** - Update existing tasks
- **Logout Functionality** - Secure session termination

### API Features
- **CORS Enabled** - Configured for frontend communication
- **RESTful Design** - Standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
- **Error Handling** - Appropriate HTTP status codes and error messages
- **Interactive Documentation** - Swagger UI and ReDoc available out of the box

## Prerequisites

Install the following tools before running the project locally:

- **Python 3.12+**
- **Node.js 18+**
- **npm**
- **PostgreSQL 13+** for local database setup without Docker
- **Docker Desktop** and **Docker Compose** for containerized setup
- **Poetry** if you want to use the Poetry workflow for the backend

## Environment Variables

This project uses environment variables in two common ways:

- A root-level `.env` file for Docker Compose
- A `backend/.env` file when running the backend directly without Docker

### Root `.env` for Docker Compose

Create `.env` in the project root with values similar to:

```env
POSTGRES_USER=todouser
POSTGRES_PASSWORD=todopassword
POSTGRES_DB=dailydo
PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin
SECRET_KEY=your-super-secret-key
```

### `backend/.env` for Local Backend Development

Create `backend/.env` with:

```env
DATABASE_URL=postgresql://todouser:todopassword@localhost:5432/dailydo
TEST_DATABASE_URL=postgresql://todouser:todopassword@localhost:5432/test_db
SECRET_KEY=your-super-secret-key
```

### Optional Frontend Environment Variables

The frontend can run without a local `.env`, but it supports these variables:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
INTERNAL_API_URL=http://backend:8000
```

## Installation

### Option 1: Local Development Setup

#### Backend Setup

1. Clone the repository and move into the project folder.

```bash
git clone <repository-url>
cd FASTAPI
```

2. Create `backend/.env` using the example shown above.

3. Install backend dependencies.

Using Poetry:

```bash
cd backend
poetry install
```

Using `pip` and `requirements.txt`:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

4. Start the FastAPI development server.

Using Poetry:

```bash
poetry run uvicorn todo_app.main:app --reload
```

Using the virtual environment:

```bash
uvicorn todo_app.main:app --reload
```

The backend will be available at `http://localhost:8000`.

#### Frontend Setup

1. Open a new terminal and move into the frontend folder.

```bash
cd frontend
```

2. Install dependencies.

```bash
npm install
```

3. Start the frontend development server.

```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`.

### Option 2: Docker Setup

1. Create a root `.env` file using the Docker example above.

2. Start all services.

```bash
docker compose up --build
```

3. Open the applications:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- pgAdmin: `http://localhost:5050`

4. Stop the stack when finished.

```bash
docker compose down
```

## Usage

### Running the Project Locally

For a full local development workflow:

1. Start PostgreSQL locally or run the database through Docker.
2. Run the backend on port `8000`.
3. Run the frontend on port `3000`.
4. Open `http://localhost:3000` in the browser.
5. Register a user, log in, and begin managing todos.

### Running with Docker Compose

Docker Compose starts the following services:

- `postgres` on port `5432`
- `backend` on port `8000`
- `frontend` on port `3000`
- `pgadmin` on port `5050`

The backend service connects to PostgreSQL internally through the Docker network, and the frontend uses the backend container for server-side requests.

## Database Setup

### Using Docker Compose

This is the recommended option for development because the database and admin tools are provisioned automatically.

```bash
docker compose up --build
```

Included services:
- PostgreSQL database on port `5432`
- pgAdmin on port `5050`

pgAdmin login:
- Email: value from `PGADMIN_DEFAULT_EMAIL`
- Password: value from `PGADMIN_DEFAULT_PASSWORD`

### Manual PostgreSQL Setup

If you prefer not to use Docker:

1. Install PostgreSQL.
2. Create the development database.

```sql
CREATE DATABASE dailydo;
CREATE DATABASE test_db;
```

3. Update `backend/.env` with your local connection strings.
4. Start the FastAPI backend.

The application creates tables on startup through `create_tables()` in `backend/todo_app/db/connection.py`.

## API Reference

### Base URL

- Local backend: `http://localhost:8000`
- Docker backend: `http://localhost:8000`

### Documentation Endpoints

- Swagger UI: `GET /docs`
- ReDoc: `GET /redoc`
- Health-style welcome route: `GET /`

### Authentication

Protected endpoints require a bearer token in the `Authorization` header:

```http
Authorization: Bearer <access_token>
```

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate and receive a JWT token |
| GET | `/auth/me` | Get the current authenticated user |

### Todo Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/todos/` | Create a new todo |
| GET | `/todos/` | Get all todos for the current user |
| GET | `/todos/{id}` | Get a specific todo by ID |
| PUT | `/todos/{id}` | Update a todo |
| DELETE | `/todos/{id}` | Delete a todo |

Supported query parameters for `GET /todos/`:

| Parameter | Type | Description |
|-----------|------|-------------|
| `search` | string | Filters todos by content |
| `status` | string | Use `completed` or `pending` |

### User Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users/` | Create a new user |
| GET | `/users/` | Get all users |
| GET | `/users/{id}` | Get a specific user by ID |
| DELETE | `/users/{id}` | Delete a user |

## API Examples

### Register a User

```http
POST /auth/register
Content-Type: application/json
```

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

### Log In

You can authenticate with either `username` or `email`.

```http
POST /auth/login
Content-Type: application/json
```

```json
{
  "username": "john_doe",
  "password": "securepassword123"
}
```

Example response:

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

### Get Current User

```http
GET /auth/me
Authorization: Bearer <access_token>
```

### Create a Todo

```http
POST /todos/
Authorization: Bearer <access_token>
Content-Type: application/json
```

```json
{
  "content": "Buy groceries",
  "is_completed": false,
  "user_id": 0
}
```

`user_id` is reassigned on the server to the authenticated user.

### Filter Todos

```http
GET /todos/?search=groceries&status=pending
Authorization: Bearer <access_token>
```

## Docker Services

The `docker-compose.yml` file provisions the following containers:

| Service | Purpose | Port |
|---------|---------|------|
| `postgres` | PostgreSQL database | `5432` |
| `backend` | FastAPI API service | `8000` |
| `frontend` | Next.js UI | `3000` |
| `pgadmin` | Database management UI | `5050` |

### Docker Notes

- The backend container mounts `./backend` into `/app` for live development.
- The frontend container mounts `./frontend` into `/app` and keeps `node_modules` and `.next` in Docker volumes.
- The backend uses `postgres` as the database host inside Docker.
- The frontend uses `NEXT_PUBLIC_API_URL` for browser requests and `INTERNAL_API_URL` for server-side requests.

## Development Notes

- The backend enables CORS for `http://localhost:3000` and `http://frontend:3000`.
- SQLModel tables are created automatically on application startup.
- API documentation is available automatically through FastAPI.
- Both Poetry and `requirements.txt` are present in the backend, so choose one dependency workflow and keep it consistent for your environment.

## Troubleshooting

### Backend cannot connect to the database
- Verify that PostgreSQL is running.
- Confirm `DATABASE_URL` in `backend/.env` is correct.
- If using Docker, make sure `docker compose up` completed successfully and the `postgres` service is healthy.

### Frontend cannot reach the API
- Confirm the backend is running on port `8000`.
- Check `NEXT_PUBLIC_API_URL` if you changed the backend port or host.
- For Docker, ensure the frontend container starts after the backend service.

### Authentication fails
- Confirm `SECRET_KEY` is set.
- Make sure the token is included as a Bearer token in the `Authorization` header.
- Re-authenticate to generate a fresh token if needed.
