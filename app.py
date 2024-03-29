from flask import Flask, jsonify, redirect, render_template, request, url_for, session, make_response
from flask_socketio import SocketIO, emit
from mongo import *
import secrets
from better_profanity import profanity
from timer import Timer

app = Flask(__name__)
app.secret_key = secrets.token_hex()
app.jinja_env.globals.update(enumerate=enumerate)

socket = SocketIO(app)

timer = Timer()

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
            session["login_error"] = "Incorrect username/password"
            return redirect("/login")

    return render_template("skeletal.html", username=session.get("username", ""))

@app.route("/login")
def login():
    return render_template("login.html", error=session.pop("login_error", ""))

@app.route("/signup")
def signup():
    return render_template("signup.html", error=session.pop("signup_error", ""))

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", top=get_top())

@app.route("/signup_validator", methods=["POST"])
def signup_validator():
    form = request.form
    username = form["username"]
    password = form["password"]
    confirm = form["confirm"]

    if 15 < len(username) < 3:
        session["signup_error"] = "Username too long or too short"

    elif find(username=username):
        session["signup_error"] = "Username used"

    elif profanity.contains_profanity(username):
        session["signup_error"] = "Inappropriate username"

    elif password != confirm:
        session["signup_error"] = "Please make sure the password match"

    else:
        create_user(username, password)
        session["username"] = username
        return redirect("/home")

    return redirect("/signup")


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

    if amount > 200:
        emit("warn", "You have been caught hacking, please do not hack!")
        return

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
    emit("apple", user_data["apple"] + amount)

@socket.on("init")
def init(user):
    user_data = find(username=user)
    emit("apple", user_data["apple"])
    emit("inv", user_data["inventory"])
    emit("shop", SHOP)

@socket.on("buy")
def buy(user, item):
    print(user, "bought", item)

    timer.start()
    user_data = find(username=user)
    timer.end("Get user data")

    price = SHOP[item] * 1.1 ** user_data["inventory"][item]
    apple = user_data["apple"]

    if apple >= price:
        timer.start()
        add_apple(user, -price)
        add_item(user, item, 1)
        timer.end("Change item value in database")

        user_data["apple"] -= price
        user_data["inventory"][item] += 1

        timer.start()
        emit("apple", user_data["apple"])
        emit("item", (item, user_data["inventory"][item]))
        emit("shop", SHOP)
        timer.end("Emit all item to socket")

    else:
        # TODO: handle not enough apple
        pass
        



if __name__ == "__main__":
    socket.run(app, debug=True)