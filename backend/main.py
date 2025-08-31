from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# -------------------------------
# MongoDB connection
# -------------------------------
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/mydb")
client = MongoClient(MONGO_URI)
db = client.get_database()

# -------------------------------
# CORS Configuration
# -------------------------------
origins = [
    "http://localhost",
    "http://localhost:80",
    "http://localhost:4200",   # Angular dev server
    "http://127.0.0.1",
    "http://127.0.0.1:4200",   # in case Angular runs on 127.0.0.1
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # change to ["*"] if still failing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Pydantic Model
# -------------------------------
class Item(BaseModel):
    name: str
    description: str = None

# -------------------------------
# Routes
# -------------------------------
@app.get("/")
def read_root():
    return {"message": "FastAPI Backend is Running!"}


@app.get("/items/")
def read_items():
    """Fetch all items from MongoDB (excluding _id)."""
    items = list(db.items.find({}, {"_id": 0}))
    return {"items": items}


@app.post("/items/")
def create_item(item: Item):
    """Insert a new item into MongoDB."""
    db.items.insert_one(item.dict())
    return {"message": "Item added successfully!", "item": item.dict()}
