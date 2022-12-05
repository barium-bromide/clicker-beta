from flask import Flask, jsonify, redirect, render_template, request, url_for, session, make_response
from flask_socketio import SocketIO, emit
from mongo import *
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()
socket = SocketIO(app)

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        form = request.form

        username = form["username"]
        password = form["password"]

        user = find(username=username, password=password)

        if user:
            return render_template("skeletal.html", username=username)
        else:
            # TODO: handle invalid username
            return "Invalid"

    return render_template("skeletal.html", username="")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

@app.route("/signup_validator", methods=["POST"])
def signup_validator():
    form = request.form
    username = form["username"]
    password = form["password"]

    # TODO: handle invalid username

    create_user(username, password)

    # TODO: redirect user

    return "Signed up!"

@app.route('/username_and_pass_api')
def rickroll():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
# Sockets

@socket.on("add")
def add(user, amount):
    # TODO: check apple amount
    add_apple(user, amount)

@socket.on("init")
def init(user):
    user_data = find(username=user)
    emit("apple", user_data["apple"])
    emit("inv", user_data["inventory"])
    emit("shop", SHOP)

@socket.on("buy")
def buy(user, item):
    print(user, item)
    user_data = find(username=user)
    price = SHOP[item] * 1.1 ** user_data["inventory"][item]
    apple = user_data["apple"]

    if apple >= price:
        add_apple(user, -price)
        add_item(user, item, 1)

        user_data["apple"] -= price
        user_data["inventory"][item] += 1

        emit("apple", user_data["apple"])
        emit("item", (item, user_data["inventory"][item]))
        emit("shop", SHOP)

    else:
        # TODO: handle not enough apple
        pass
        



if __name__ == "__main__":
    socket.run(app, debug=True)