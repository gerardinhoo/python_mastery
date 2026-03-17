import platform

from fastapi import FastAPI

from api.models import User

app = FastAPI(
    title="Python Mastery API",
    description="A FastAPI project demonstrating API development skills",
    version="1.0.0",
)

# In-memory user storage
users: list[User] = []


@app.get("/")
def home():
    return {"message": "Welcome to Gerard's Python API"}


@app.get("/health")
def check_health():
    return {"status": "healthy"}


@app.get("/system")
def system_info():
    return {
        "system": platform.system(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }


@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created"}


@app.get("/users")
def get_users():
    return users


@app.get("/users/{name}")
def get_user(name: str):
    for user in users:
        if user.name == name:
            return user
    return {"error": "User not found"}
