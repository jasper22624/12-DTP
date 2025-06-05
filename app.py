from flask import Flask, render_template
import sqlite3
import random
select = []
ran = 0
cardss = []
cardss1=[]
cardssp=[]


app = Flask(__name__)


@app.route("/")
def start():
    return render_template("start.html", title="starting")


@app.route("/home")
def home():
    return render_template("home1.html", title="home")


@app.route("/play")
def play():
    cardss=[]
    cardss1=[]
    cardssp=[]
    select=[]
        #player's\/
    for i in range(1,3):
        cursor = sqlite3.connect('data.db').cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'select Card.id,Colour.colours,Number.numbers,Card.name from Card join Colour on Card.colour = Colour.id join Number on Card.number = Number.id where Card.id = {ran} order by Card.id')
        cards = cursor.fetchall()
        select.append(cards[0][0])
        cardss.append(cards)
        sqlite3.connect('data.db').close()
        #bot's\/
    for i in range(1,3):
        cursor = sqlite3.connect('data.db').cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'select Card.id,Colour.colours,Number.numbers,Card.name from Card join Colour on Card.colour = Colour.id join Number on Card.number = Number.id where Card.id = {ran} order by Card.id')
        cards = cursor.fetchall()
        select.append(cards[0][0])
        cardss1.append(cards)
        sqlite3.connect('data.db').close()
        #public cards\/
    for i in range(1,6):
        cursor = sqlite3.connect('data.db').cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'select Card.id,Colour.colours,Number.numbers,Card.name from Card join Colour on Card.colour = Colour.id join Number on Card.number = Number.id where Card.id = {ran} order by Card.id')
        cards = cursor.fetchall()
        select.append(cards[0][0])
        cardssp.append(cards)
        sqlite3.connect('data.db').close()
        
    return render_template("play.html", title="play", cards=cardss, cardsp=cardssp)


if __name__ == "__main__":
    app.run(debug=True)