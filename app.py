from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home1.html", title="home")


@app.route("/play")
def play():
    return render_template("play.html", title="play")


if __name__ == "__main__":
    app.run(debug=True)