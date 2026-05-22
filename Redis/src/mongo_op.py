# Mongodb Operations
from pymongo import MongoClient

def mongo_operations():
    try:
        # connection check
        if MongoClient("mongodb://localhost:27017/").server_info():
            print("Connected to MongoDB successfully!")
        else:
            print("Failed to connect to MongoDB")

        mongo_client = MongoClient("mongodb://localhost:27017/")
        db = mongo_client["chai_db"]
        collection = db["chai_collection"]  
        # Insert a document
        document = {"name": "Tejas", "age": 24, "city": "Pune"}
        result = collection.insert_one(document)
        print(f"Document inserted with id: {result.inserted_id}")
        # Find a document
        find_doc = collection.find_one({"name": "Tejas"})
        print(f"Found document: {find_doc}")
    except Exception as e:
        print(f"Error while performing mongodb operations: {e}")

if __name__ == "__main__":
    mongo_operations()