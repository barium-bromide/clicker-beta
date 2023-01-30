from flask import Flask, jsonify, redirect, render_template, request, url_for, session, make_response
from flask_socketio import SocketIO, emit
from mongo import *
import secrets
from better_profanity import profanity

app = Flask(__name__)
app.secret_key = secrets.token_hex()
app.jinja_env.globals.update(enumerate=enumerate)

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
            return render_template("login.html")

    return render_template("skeletal.html", username="")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", top=get_top())

@app.route("/signup_validator", methods=["POST"])
def signup_validator():
    form = request.form
    username = form["username"]
    password = form["password"]
    if 15 < len(username) < 3:
        return "Username too long or too short"

    elif profanity.contains_profanity(username):
        return "inappropriate username"

    elif find(username=username):
        return  "Username used"
        
    else:
        create_user(username, password)
        return redirect("/home")


@app.route('/username_and_pass_api')
def rickroll():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@app.route("/buy", methods=["POST"])
def buy(user, item):
    # This is plan b (incase the optimizing on socket doenst work)
    print(user, item)
    user_data = find(username=user)
    price = SHOP[item] * 1.1 ** user_data["inventory"][item]
    apple = user_data["apple"]

    if apple >= price:
        add_apple(user, -price)
        add_item(user, item, 1)

        user_data["apple"] -= price
        user_data["inventory"][item] += 1

        # emit("apple", user_data["apple"])
        # emit("item", (item, user_data["inventory"][item]))
        # emit("shop", SHOP)

        response = jsonify({
            "apple": user_data["apple"],
            item: user_data["inventory"][item]
        })

    else:
        # TODO: handle not enough apple
        pass

# Sockets

@socket.on("add")
def add(user, amount):
    user_data = find(username=user)
    amount = (amount * ((user_data["inventory"]["workers"] * 100 + 
                       5 * user_data["inventory"]["trucks"] + 
                       10 * user_data["inventory"]["tradeCenter"]) / 100) + 
                       ((user_data["inventory"]["farm"] * 100 + 
                       2 * user_data["inventory"]["factory"] + 
                       5 * user_data["inventory"]["ship"] + 
                       10 * user_data["inventory"]["aeroplane"] + 
                       15 * user_data["inventory"]["computer"] + 
                       20 * user_data["inventory"]["rocketShip"]) / 100))
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