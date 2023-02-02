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

def default(prompt, val):
    return input(prompt).strip() or val

if __name__ == "__main__":

    print("--------------------------------------------------")
    print("Create user, enter = default value in bracket")

    datas.insert_one({
        "username": input("Username: "),
        "password": input("Password: "),
        "apple": float(default("Apple (0): ", 0)),
        "inventory": {
            "workers": int(default("Workers (0) : ", 0)),
            "farm": int(default("Farm (0) : ", 0)),
            "factory": int(default("Factory (0) : ", 0)),
            "store": int(default("Store (0) : ", 0)),
            "trucks": int(default("Trucks (0) : ", 0)),
            "ship": int(default("Ship (0) : ", 0)),
            "aeroplane": int(default("Aeroplane (0) : ", 0)),
            "tradeCenter": int(default("Trade Center (0) : ", 0)),
            "computer": int(default("Computer (0) : ", 0)),
            "rocketShip": int(default("Rocketship (0) : ", 0))
        }
    })