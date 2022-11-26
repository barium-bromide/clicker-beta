from flask import Flask, jsonify, redirect, render_template, request, url_for, session, make_response
from flask_socketio import SocketIO
from mongo import *
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()
socket = SocketIO(app)

@app.route("/home")
def home():
    return render_template("skeletal.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

@socket.on("add")
def add(user, amount):
    add_apple(user, amount)

@socket.on("init")
def init(user):
    user_data = find(user)
    socket.emit("init", (user, user_data["apple"], user_data["inventory"], SHOP))

@socket.on("buy")
def buy(item):
    pass


if __name__ == "__main__":
    socket.run(app, debug=True)