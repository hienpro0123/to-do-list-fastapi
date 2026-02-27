from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
def root(request: Request) -> dict:
    return {
        "message": "Welcome To FastAPI CRUD"
    }


@app.get("/health")
def health_check(request: Request) -> dict:
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("root:app", host="0.0.0.0", port=8000, reload=True)