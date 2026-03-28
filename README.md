
# 📚Daily ToDo App

## 📌 Project Overview

This project was built to demonstrate a practical full-stack workflow: authentication, CRUD operations, database integration, and frontend-backend communication in one cohesive application. The backend exposes RESTful endpoints with FastAPI, while the frontend provides a clean task dashboard for creating, updating, filtering, and deleting todos.
This project focuses on the core pieces of a modern full-stack workflow:

- 🔐 Secure user authentication with registration, login, and token-based access
- ✅ Personal task management with create, read, update, and delete flows
- 🔎 Search and status filtering for a better task management experience
- 🌐 Clear frontend-backend separation with a shared local development setup
- 📘 Built-in API documentation through FastAPI Swagger and ReDoc

It is a solid GitHub portfolio example for demonstrating both backend API design and frontend application development.

## ✨ Key Features

- JWT-based authentication with protected routes
- Registration and login using username or email
- Secure password hashing
- Create, read, update, and delete todos
- Filter tasks by keyword and completion status
- Responsive UI for desktop and mobile
- Built-in API documentation with Swagger UI and ReDoc
- Docker Compose environment with PostgreSQL and pgAdmin
- JWT-style token authentication for protected routes
- User registration and login with username or email support
- Password hashing for secure credential storage
- Todo CRUD operations tied to the authenticated user
- Task filtering by keyword and completion status
- Responsive task dashboard with add, edit, delete, and logout flows
- Docker Compose setup with PostgreSQL and pgAdmin
- Automatic table creation on backend startup

## 🛠️ Tech Stack

- Tailwind CSS
- Radix UI

**Infrastructure**
**Dev Tools**
- Docker
- Docker Compose
- pgAdmin

```text
FASTAPI/
|-- backend/          # FastAPI app, routers, services, database
|-- frontend/         # Next.js app, pages, components, utilities
|-- docker-compose.yml
`-- README.md
├── backend/      # FastAPI app, routers, services, schemas, database config
├── frontend/     # Next.js app, pages, components, API helpers
├── docker-compose.yml
└── README.md
```

## 🚀 Setup & Run

### Option 1: Docker
### 🐳 Docker

Create a root `.env` file:

SECRET_KEY=your-super-secret-key
```

Start the stack:
Start the full stack:

```bash
docker compose up --build
```

Services:
Available services:

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- Swagger Docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- pgAdmin: `http://localhost:5050`

### Option 2: Local Development

**Backend**
### 💻 Local Development

Create `backend/.env`:
Backend:

```env
DATABASE_URL=postgresql://todouser:todopassword@localhost:5432/dailydo
TEST_DATABASE_URL=postgresql://todouser:todopassword@localhost:5432/test_db
SECRET_KEY=your-super-secret-key
```

Run:

```bash
cd backend
uvicorn todo_app.main:app --reload
```

**Frontend**
Frontend:

```bash
cd frontend

## 🔗 Main API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Log in and receive a token |
| GET | `/auth/me` | Get the current authenticated user |
| POST | `/todos/` | Create a todo |
| GET | `/todos/` | List todos for the current user |
| GET | `/todos/{id}` | Get a single todo |
| PUT | `/todos/{id}` | Update a todo |
| DELETE | `/todos/{id}` | Delete a todo |
| GET | `/users/` | List users |
| GET | `/users/{id}` | Get a user by ID |
| DELETE | `/users/{id}` | Delete a user |
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Log in and receive an access token |
| `GET` | `/auth/me` | Get the current authenticated user |
| `POST` | `/todos/` | Create a new todo |
| `GET` | `/todos/` | List the current user's todos |
| `GET` | `/todos/{id}` | Get a single todo by ID |
| `PUT` | `/todos/{id}` | Update a todo |
| `DELETE` | `/todos/{id}` | Delete a todo |
| `GET` | `/users/` | List users |
| `GET` | `/users/{id}` | Get a user by ID |
| `DELETE` | `/users/{id}` | Delete a user |

Supported query parameters for `GET /todos/`:
- `search` for filtering by content
- `status` with `completed` or `pending`
Todo list filtering supports:

## ✅ Notes
- 🔎 `search` to filter by task content
- ✅ `status=completed`
- ⏳ `status=pending`

- CORS is configured for the local frontend
- Database tables are created automatically on startup
- The frontend supports separate API URLs for browser-side and server-side requests
## 📎 Notes

This repository is a solid portfolio example of a modern full-stack CRUD app with authentication, clean API structure, and containerized development.
- CORS is configured for local frontend access
- The frontend uses separate browser-side and server-side API base URLs
- The repository is structured for easy local development and Docker-based demos