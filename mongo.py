import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

URI = os.getenv("uri")
client = MongoClient(URI)
datas = client.db.datas


SHOP = {
    "workers": 15,
    "farm": 100,
    "factory": 1000,
    "store": 2000,
    "trucks": 5000,
    "ship": 10000,
    "aeroplane": 30000,
    "tradeCenter": 50000,
    "computer": 100000,
    "rocketShip": 200000
}
 
def find(**filter):
    return datas.find_one(filter)

def create_user(username, password):
    if find(username=username):
        return False
    
    datas.insert_one({
        "username": username,
        "password": password,
        "apple": 0,
        "inventory": dict(zip(SHOP.keys(), [0] * len(SHOP)))
    })

    return True

def add_apple(username, amount):
    # TODO: check apple amount

    datas.update_one({ "username": username }, {
        "$inc": {
            "apple": amount
        }
    })
