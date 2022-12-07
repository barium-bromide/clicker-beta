from flask import Flask, jsonify, redirect, render_template, request, url_for, session, make_response
from flask_socketio import SocketIO, emit
from mongo import *
import secrets

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
    return render_template("leaderboard.html", top=get_top())

@app.route("/signup_validator", methods=["POST"])
def signup_validator():
    form = request.form
    username = form["username"]
    password = form["password"]
    invalid_username = ["fuck","ass","dick","retard","shit","nigga","nigger","puss","bitch","hitler",
                        "nazi","gay","lesbian","transgender","queer","sex","jayyong","cisgender","piss",
                        "cum","cock","thot","penis","vagina","boob","slut","twat","cunt","bastard",
                        "geonocide","suicide","racist","sexist","bollocks","testis","foreskin","anal","incest",
                        "sperm","ovum","risingsunflag","japanwarflag","rape","rapist",
                        "raping","axispower","hirohito","hidekitojo","stalin","tit","japanesewarflag"]
    allowed_letters = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVwXYZ1234567890_. "]
    unban_word = ["documantary","document","documentation","cockadoodledoo"]
    ini_string = username
 
    k = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVwXYZ";
 
    getVals = list(filter(lambda x: x in k, ini_string))
    result = "".join(getVals)
    valid = 1
    for letters in username:
        if letters not in allowed_letters:
            valid = 0
            break
    for bad_word in invalid_username:
        if bad_word in result:
            valid = 0
            break
    for good_word in unban_word:
        if good_word in result:
            valid = 1
            break
    if valid == 1:
        create_user(username, password)
        return render_template("skeletal.html")
    else:
        #TODO window.aler("Your username is inapproriate")
        pass

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