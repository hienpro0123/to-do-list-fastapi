# DailyDo Todo App

## 📌 Overview

- DailyDo is a full-stack todo app built for people who want a simple way to manage personal tasks without mixing data across users.
- The project solves two practical problems at once: storing todos in a real database and protecting each user's task list behind authentication.
- It combines a FastAPI backend, a Next.js frontend, and PostgreSQL in one repo, so you can see the full flow from login to database-backed CRUD operations.
- This is a good project for learning or showcasing how a frontend and API work together in a clean, separated setup.

## ✨ Key Features

- User registration and login with JWT authentication.
- Login accepts either a username or an email address, which makes the sign-in flow more flexible.
- Passwords are hashed before storage instead of being saved as plain text.
- Every todo is tied to the authenticated user, so one user cannot read or edit another user's tasks.
- Task management includes create, list, update, and delete actions.
- The todo list supports `search` and `status` filters, making it easier to find pending or completed work quickly.
- The frontend includes dedicated login and register pages, a task dashboard, add/edit dialogs, and logout support.
- FastAPI automatically exposes Swagger UI and ReDoc, which makes the API easy to inspect and test during development.
- Docker Compose starts the frontend, backend, PostgreSQL, and pgAdmin together for a complete local environment.

## 🛠️ Tech Stack

- Backend: FastAPI, SQLModel, PostgreSQL, Psycopg, JWT (`python-jose`), Passlib
- Frontend: Next.js 14, React 18, TypeScript, Tailwind CSS
- UI helpers: Radix UI, Lucide React, React Hot Toast
- Dev tooling: Docker, Docker Compose, pgAdmin, Pytest

## 🗂️ Project Structure

- `backend/` - FastAPI app with routers, services, schemas, database config, and tests
- `frontend/` - Next.js app with pages, components, API helpers, and styling
- `docker-compose.yml` - local multi-service setup for app containers, PostgreSQL, and pgAdmin
- `.env` - shared environment variables for database access and the app secret key

## 🚀 Setup & Run

- Clone the repository and move into the project folder:

```bash
git clone <your-repo-url>
cd FASTAPI
```

- Create a root `.env` file if you do not already have one:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=todo_db
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin
DATABASE_URL=postgresql://admin:admin@localhost:5432/todo_db
TEST_DATABASE_URL=postgresql://admin:admin@localhost:5432/test_db
SECRET_KEY=your-secret-key
```

- Run everything with Docker:

```bash
docker compose up --build
```

- Open the app and tools:
  - Frontend: `http://localhost:3000`
  - Backend API: `http://localhost:8000`
  - Swagger docs: `http://localhost:8000/docs`
  - ReDoc: `http://localhost:8000/redoc`
  - pgAdmin: `http://localhost:5050`

- Run locally without Docker if needed:
  - Backend:

```bash
cd backend
pip install -r requirements.txt
uvicorn todo_app.main:app --reload
```

  - Frontend:

```bash
cd frontend
npm install
npm run dev
```

## 🔌 Main API

- `POST /auth/register` - create a new user account
- `POST /auth/login` - log in with username or email and receive a bearer token
- `GET /auth/me` - return the currently authenticated user
- `GET /todos/` - list the current user's todos, with optional `search` and `status` filters
- `POST /todos/` - create a new todo for the logged-in user
- `PUT /todos/{id}` - update a todo's content or completion state
- `DELETE /todos/{id}` - remove a todo
