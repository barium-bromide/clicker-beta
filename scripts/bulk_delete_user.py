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
    exit()

os.system("cls")

datas = client.db.datas

if __name__ == "__main__":
    users = []

    while not users or users[-1] != "#":
        user = input("Enter username to delete (enter # to end): ")

        if user != "#" and not datas.find_one({
            "username": user
        }):
            print(f"User {user} does not exist")
            exit()

        else:
            users.append(user)

        
    print(f"Are you sure you want to delete these {len(users)} user(s)?", *users[:-1], sep="\n")


    if input("Type CONFIRM to confirm: ") != "CONFIRM":
        print("--ABORTED--")
        exit()

    datas.delete_many({
        "username": {
            "$in": users
        }
    })

    print("--DELETED--")
