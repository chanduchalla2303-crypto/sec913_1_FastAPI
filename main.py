from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Products endpoint
@app.get("/products")
def get_products():
    return [
        {"name": "Laptop", "price": 99999},
        {"name": "Phone", "price": 70000},
        {"name": "Headphones", "price": 1999},
        {"name": "Tablet", "price": 29999}
    ]

# Login request model
class LoginRequest(BaseModel):
    username: str
    password: str

# Login endpoint
@app.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "admin123":
        return {"UserStatus": 1, "UserRole": "Admin", "UserPendingTask": 1}
    if data.username == "student" and data.password == "student123":
        return {"UserStatus": 1, "UserRole": "Student", "UserPendingTask": 1}
    if data.username == "staff" and data.password == "staff123":
        return {"UserStatus": 1, "UserRole": "Staff", "UserPendingTask": 1}
    raise HTTPException(status_code=401, detail="Invalid credentials")