from fastapi import FastAPI
import platform

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Gerard's Python API"}

@app.get("/health")
def check_health():
    return {"status": "healthy"}

@app.get("/user/{name}")
def get_user(name: str):
    return {"user": name}

@app.get("/system")
def system_info():

    return {
        "System": platform.system(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }

