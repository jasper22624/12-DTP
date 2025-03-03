from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title="home")


@app.route("/pet_rocks/<int:id>")
def pet_rocks(id):
    return render_template("pet_rocks.html", id=id)


@app.route("/all_pizza")
def all_pizzas():
    cursor = sqlite3.connect('first_flask/pizza.db').cursor()
    cursor.execute('select * from Pizza order by id')
    pizzas = cursor.fetchall()
    sqlite3.connect('first_flask/pizza.db').close()
    return render_template("all_pizza.html", pizzas=pizzas)


if __name__ == "__main__":
    app.run(debug=True)
