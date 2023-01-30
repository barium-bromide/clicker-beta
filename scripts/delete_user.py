import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

URI = os.getenv("uri")
client = MongoClient(URI, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")

datas = client.db.datas

if __name__ == "__main__":
    user = input("Enter username to delete: ")

    if not datas.find_one({
        "username": user
    }):
        print(f"User {user} does not exist")
        exit()

    if input("Type CONFIRM to confirm: ") != "CONFIRM":
        print("--ABORTED--")
        exit()

    datas.delete_many({
        "username": user
    })

    print("--DELETED--")
