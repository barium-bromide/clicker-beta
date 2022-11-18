from flask import Flask, jsonify, redirect, render_template, request, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()

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


if __name__ == "__main__":
    app.run(debug=True)