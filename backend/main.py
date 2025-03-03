from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/mydb")
client = MongoClient(MONGO_URI)
db = client.get_database()

@app.get("/")
def read_root():
    return {"message": "FastAPI Backend is Running!"}

@app.get("/items/")
def read_items():
    items = list(db.items.find({}, {"_id": 0}))  # Fetch items from MongoDB
    return {"items": items}
