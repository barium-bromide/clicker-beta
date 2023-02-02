import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

URI = os.getenv("uri")
client = MongoClient(URI, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
except:
    print("Unable to connect to the server.")
    exit()

os.system("cls")

datas = client.db.datas

if __name__ == "__main__":
    username = input("Enter username to add apple: ")
    user = datas.find_one({
        "username": username
    })

    if user:
        amount = float(input(f"Enter amount of apple to add to {username} (Negative to remove from user): "))
        datas.update_one({
            "username": username
        }, {
            "$inc": {
                "apple": amount
            }
        })

        print(f"Added {amount} apple(s) to {username}")

    else:
        print("User does not exist, try again")

