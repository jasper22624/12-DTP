from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title="home")


@app.route("/pet_rocks/<int:id>")
def pet_rocks(id):
    return render_template("pet_rocks.html", id=id)


if __name__ == "__main__":
    app.run(debug=True)
