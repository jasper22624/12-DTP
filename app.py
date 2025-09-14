from flask import Flask, render_template, request
import sqlite3
import random


select = []
ran = 0
cardss = []
money = 2000
money1 = money
cardss1=[]
cardssp=[]
score1=0
score2=0
cardss2=[]

#The following code is for creating a table called 'Money'
#This is for storage of varible - money
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

#if the data.db is intialized, we need to add table
cursor.execute("CREATE TABLE IF NOT EXISTS Money (id INTEGER PRIMARY KEY, money INTEGER, won INTEGER)")
conn.commit()

cursor.execute("UPDATE Money SET money = ?, won = ? WHERE id = ?", (money, 0, 1))
if cursor.rowcount == 0: #if the data.db is intialized, we need to add data
    cursor.execute("INSERT INTO Money (id, money, won) VALUES (?, ?, ?)", (1, money, 0))
conn.commit()

conn.close()


app = Flask(__name__)


@app.route("/")
def start():
    return render_template("start.html", title="starting")


@app.route("/home")
def home():
    return render_template("home1.html", title="home")


@app.route("/instruction")
def instruction():
    return render_template("instruction.html", title="instruction")


@app.route("/play", methods=["GET", "POST"])
def play():
    score1=0
    score2=0
    q=0
    if request.method == "POST":
        if "fold" in request.form:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            cursor.execute("select Money.money, Money.won from Money where id=1")
            statt = cursor.fetchall()
            stat = statt[0][1]
            money = statt[0][0]
            conn.close()
            # Player folds, Bot with the highest score wins
            # don't need to check for draw because if player fold, player lose anyway
            if score1 > score2:
                won = "Bot 1 won!"
            else:
                won = "Bot 2 won!"
            q += 1
            money += 100  # Player get back half the bet, reward for folding
            if stat == -1:
                money -= 200
            if stat == 1:
                money -= 300
            if stat == 2:
                money -= 600
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE Money SET money = ? WHERE id = ?", (money, 1))
            conn.commit()
            conn.close()
    
    
    cardss=[]
    cardss1=[]
    cardss2=[]
    cardssp=[]
    select=[]
    p = []
    p1 = []
    p2=[]
    y = []
    f = False
    y1 = []
    y1c = []
    ran = 0
    select = []
    y2 = []
    y2c = []
    y3=[]
    y3c=[]
    yp = []
    ypc = []
    won = "none"
    bet = 200
    score1 = 0
    score2 = 0
    q=0
    raise_amount = 0
    stat=0
    c=0


    #the following code is for extract data from table - "Money"
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("select Money.money from Money where id=1")
    moneyl = cursor.fetchall()
    money = moneyl[0][0]
    conn.close()
    money2 = money
    money -= bet


     #player's cards extraction
    for i in range(1,3):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'SELECT Card.id, Colour.colours, Number.numbers, Card.name, Card.media FROM Card JOIN Colour ON Card.colour = Colour.id JOIN CardNumber ON Card.id = CardNumber.card_id JOIN Number ON CardNumber.number_id = Number.id WHERE Card.id = {ran} ORDER BY Card.id')
        cards = cursor.fetchall()
        select.append(cards[0][0])
        cardss.append(cards)    
        y1.append(cards[0][2])
        y1c.append(cards[0][1])
        p.append(cards[0][3])
        conn.close()


        #Bot's cards extraction
    for i in range(1,3):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'SELECT Card.id, Colour.colours, Number.numbers, Card.name, Card.media FROM Card JOIN Colour ON Card.colour = Colour.id JOIN CardNumber ON Card.id = CardNumber.card_id JOIN Number ON CardNumber.number_id = Number.id WHERE Card.id = {ran} ORDER BY Card.id')
        cards = cursor.fetchall()
        select.append(cards[0][0])
        cardss1.append(cards)
        y2.append(cards[0][2])
        y2c.append(cards[0][1])
        p1.append(cards[0][3])
        conn.close()


        #bot2's cards extraction
    for i in range(1, 3):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'SELECT Card.id, Colour.colours, Number.numbers, Card.name, Card.media FROM Card JOIN Colour ON Card.colour = Colour.id JOIN CardNumber ON Card.id = CardNumber.card_id JOIN Number ON CardNumber.number_id = Number.id WHERE Card.id = {ran} ORDER BY Card.id')
        cards = cursor.fetchall()
        select.append(cards[0][0])
        cardss2.append(cards)
        y3.append(cards[0][2])
        y3c.append(cards[0][1])
        p2.append(cards[0][3])
        conn.close()


        #public cards cards extraction
    for i in range(1,6):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'SELECT Card.id, Colour.colours, Number.numbers, Card.name, Card.media FROM Card JOIN Colour ON Card.colour = Colour.id JOIN CardNumber ON Card.id = CardNumber.card_id JOIN Number ON CardNumber.number_id = Number.id WHERE Card.id = {ran} ORDER BY Card.id')
        cards = cursor.fetchall()
        select.append(cards[0][0])
        cardssp.append(cards)
        yp.append(cards[0][2])
        ypc.append(cards[0][1])
        p.append(cards[0][3])
        p1.append(cards[0][3])
        conn.close()


    #The following code is for assess the cards of player
    z = 0
    score = 0
    threes = False
    card = 0
    y1.extend(yp)
    y1c.extend(ypc)
    y.append(y1)
    for i in y:
        i.sort()
        p.sort()
        print(f"your card: {p}")
        if len(i) != 7:
            print("wrong amount")
            exit()
        for ii in i:
            try:
                ii = int(ii)
                if 2 <= ii <= 14:
                    for e in range(2, 15):
                        if i.count(e) > 3:
                            threes = True
                            card = e
                else:
                    print("wrong input")
                    exit()
            except ValueError:
                print("wrong")
                exit()
    if threes is True:
        print("there is a four of a kind in here")
        score += 7
        # the code above is checking the 4 of a kind
    else:
        z = 0
        threes = False
        for i in y:
            i.sort()
            for e in range(2, 15):
                if i.count(e) > 2:
                    for t in range(2, 15):
                        if t != e:
                            if i.count(t) > 1:
                                threes = True
                                card = e + t * 0.01
        if threes is True:
            print("there is a full house in here")
            score += 6
            # the code above is checking full house
        else:
            z = 0
            threes = False
            y1c.sort()
            y1c.reverse()
            for h in range(1, 5):
                if y1c.count(h) > 4:
                    for w in range(0, 5):
                        threes = True
                        card = y[0][w]
                        if y1c[w] != h:
                            continue
            if threes is True:
                z = 0
                T = 0
                ee = 0
                Straight = False
                for i in y:
                    i.sort()
                    i.reverse()
                    for ii in i:
                        try:
                            ii = int(ii)
                            if z != 0:
                                if ii-z == -1:
                                    T = T+1
                                elif ii-z == 0:
                                    T = T
                                else:
                                    T = 0
                            z = ii
                            if T >= 4:
                                Straight = True
                                card = z
                        except ValueError:
                            print("wrong")
                            exit()
                if Straight is True:
                    print("it's a straight flush")
                    score += 10
                else:
                    print("there is a flush in here")
                    score += 5
            # the code above is checking flush and stright flush
            # because the 7 cards can not form full house and flush at once
            # the assess of stright flush can go after the full house
            else:
                z = 0
                T = 0
                ee = 0
                Straight = False
                for i in y:
                    i.sort()
                    i.reverse()
                    for ii in i:
                        try:
                            ii = int(ii)
                            if z != 0:
                                if ii-z == -1:
                                    T = T+1
                                elif ii-z == 0:
                                    T = T
                                else:
                                    T = 0
                            z = ii
                            if T >= 4:
                                Straight = True
                                card = z
                                break
                        except ValueError:
                            print("wrong")
                            exit()
                if Straight is True:
                    print("it's a straight")
                    score += 4
                    # the code above is checking the Straight
                else:
                    z = 0
                    threes = False
                    for i in y:
                        i.sort()
                        for e in range(2, 15):
                            if i.count(e) > 2:
                                threes = True
                                card = e
                    if threes is True:
                        print("there is a three of a kind in here")
                        score += 3
                        # the code above is checking the 3 of a kind
                    else:
                        pair = 0
                        z = 0
                        for i in y:
                            i.sort()
                            for ii in i:
                                ii = int(ii)
                                if z != 0:
                                    if ii == z:
                                        pair = pair + 1
                                        if card == 0:
                                            card = ii
                                        else:
                                            card += ii * 3
                                z = ii
                            if pair > 2:
                                pair = 2
                            if pair != 0:
                                print(f"there is {pair} pairs in here")
                                score += pair
                            else:
                                print("Biggest card")
                                score = 0
                                i.sort()
                                card = y[0][6]
                            # the code above is checking pairs and Big card


    #The following code is for assess the cards of CPU
    z = 0
    score1 = 0
    y = []
    threes = False
    card1 = 0
    y2.extend(yp)
    y2c.extend(ypc)
    y.append(y2)
    y.sort()
    for i in y:
        i.sort()
        p1.sort()
        print(f"Bot 1's card {p1}")
        if len(i) != 7:
            print("wrong amount")
            exit()
        for ii in i:
            try:
                ii = int(ii)
                if 2 <= ii <= 14:
                    for e in range(2, 15):
                        if i.count(e) > 3:
                            threes = True
                            card1 = e
                else:
                    print("wrong input")
                    exit()
            except ValueError:
                print("wrong")
                exit()
    if threes is True:
        print("there is a four of a kind in here")
        score1 += 7
        # the code above is checking the 4 of a kind
    else:
        z = 0
        threes = False
        for i in y:
            i.sort()
            for e in range(2, 15):
                if i.count(e) > 2:
                    for t in range(2, 15):
                        if t != e:
                            if i.count(t) > 1:
                                threes = True
                                card1 = e + t * 0.01
        if threes is True:
            print("there is a full house in here")
            score1 += 6
            # the code above is checking full house
        else:
            z = 0
            threes = False
            y2c.sort()
            y2c.reverse()
            for h in range(1, 5):
                if y2c.count(h) > 4:
                    for w in range(0, 5):
                        threes = True
                        card1 = y[0][w]
                        if y2c[w] != h:
                            continue
            if threes is True:
                z = 0
                T = 0
                ee = 0
                Straight = False
                for i in y:
                    i.sort()
                    i.reverse()
                    for ii in i:
                        try:
                            ii = int(ii)
                            if z != 0:
                                if ii-z == -1:
                                    T = T+1
                                elif ii-z == 0:
                                    T = T
                                else:
                                    T = 0
                            z = ii
                            if T >= 4:
                                Straight = True
                                card1 = z
                        except ValueError:
                            print("wrong")
                            exit()
                if Straight is True:
                    print("it's a straight flush")
                    score1 += 10
                else:
                    print("there is a flush in here")
                    score1 += 5
            # the code above is checking flush and stright flush
            # because the 7 cards can not form full house and flush at once
            # the assess of stright flush can go after the full house
            else:
                z = 0
                T = 0
                ee = 0
                Straight = False
                for i in y:
                    i.sort()
                    i.reverse()
                    for ii in i:
                        try:
                            ii = int(ii)
                            if z != 0:
                                if ii-z == -1:
                                    T = T+1
                                elif ii-z == 0:
                                    T = T
                                else:
                                    T = 0
                            z = ii
                            if T >= 4:
                                Straight = True
                                card1 = z
                                break
                        except ValueError:
                            print("wrong")
                            exit()
                if Straight is True:
                    print("it's a straight")
                    score1 += 4
                    # the code above is checking the Straight
                else:
                    z = 0
                    threes = False
                    for i in y:
                        i.sort()
                        for e in range(2, 15):
                            if i.count(e) > 2:
                                threes = True
                                card1 = e
                    if threes is True:
                        print("there is a three of a kind in here")
                        score1 += 3
                        # the code above is checking the 3 of a kind
                    else:
                        pair = 0
                        z = 0
                        for i in y:
                            i.sort()
                            for ii in i:
                                ii = int(ii)
                                if z != 0:
                                    if ii == z:
                                        pair = pair + 1
                                        if card1 == 0:
                                            card1 = ii
                                        else:
                                            card1 += ii * 3
                                z = ii
                            if pair > 2:
                                pair = 2
                            if pair != 0:
                                print(f"there is {pair} pairs in here")
                                score1 += pair
                            else:
                                print("Biggest card")
                                score1 = 0
                                i.sort()
                                card1 = y[0][6]
                            # the code above is checking pairs and Big card


#The following code is for assess the cards of CPU2
    z = 0
    score2 = 0
    y = []
    threes = False
    card2 = 0
    y3.extend(yp)
    y3c.extend(ypc)
    y.append(y3)
    y.sort()
    for i in y:
        i.sort()
        p2.sort()
        print(f"Bot 1's card {p2}")
        if len(i) != 7:
            print("wrong amount")
            exit()
        for ii in i:
            try:
                ii = int(ii)
                if 2 <= ii <= 14:
                    for e in range(2, 15):
                        if i.count(e) > 3:
                            threes = True
                            card2 = e
                else:
                    print("wrong input")
                    exit()
            except ValueError:
                print("wrong")
                exit()
    if threes is True:
        print("there is a four of a kind in here")
        score2 += 7
        # the code above is checking the 4 of a kind
    else:
        z = 0
        threes = False
        for i in y:
            i.sort()
            for e in range(2, 15):
                if i.count(e) > 2:
                    for t in range(2, 15):
                        if t != e:
                            if i.count(t) > 1:
                                threes = True
                                card2 = e + t * 0.01
        if threes is True:
            print("there is a full house in here")
            score2 += 6
            # the code above is checking full house
        else:
            z = 0
            threes = False
            y3c.sort()
            y3c.reverse()
            for h in range(1, 5):
                if y3c.count(h) > 4:
                    for w in range(0, 5):
                        threes = True
                        card2 = y[0][w]
                        if y3c[w] != h:
                            continue
            if threes is True:
                z = 0
                T = 0
                ee = 0
                Straight = False
                for i in y:
                    i.sort()
                    i.reverse()
                    for ii in i:
                        try:
                            ii = int(ii)
                            if z != 0:
                                if ii-z == -1:
                                    T = T+1
                                elif ii-z == 0:
                                    T = T
                                else:
                                    T = 0
                            z = ii
                            if T >= 4:
                                Straight = True
                                card2 = z
                        except ValueError:
                            print("wrong")
                            exit()
                if Straight is True:
                    print("it's a straight flush")
                    score2 += 10
                else:
                    print("there is a flush in here")
                    score2 += 5
            # the code above is checking flush and stright flush
            # because the 7 cards can not form full house and flush at once
            # the assess of stright flush can go after the full house
            else:
                z = 0
                T = 0
                ee = 0
                Straight = False
                for i in y:
                    i.sort()
                    i.reverse()
                    for ii in i:
                        try:
                            ii = int(ii)
                            if z != 0:
                                if ii-z == -1:
                                    T = T+1
                                elif ii-z == 0:
                                    T = T
                                else:
                                    T = 0
                            z = ii
                            if T >= 4:
                                Straight = True
                                card2 = z
                                break
                        except ValueError:
                            print("wrong")
                            exit()
                if Straight is True:
                    print("it's a straight")
                    score2 += 4
                    # the code above is checking the Straight
                else:
                    z = 0
                    threes = False
                    for i in y:
                        i.sort()
                        for e in range(2, 15):
                            if i.count(e) > 2:
                                threes = True
                                card2 = e
                    if threes is True:
                        print("there is a three of a kind in here")
                        score2 += 3
                        # the code above is checking the 3 of a kind
                    else:
                        pair = 0
                        z = 0
                        for i in y:
                            i.sort()
                            for ii in i:
                                ii = int(ii)
                                if z != 0:
                                    if ii == z:
                                        pair = pair + 1
                                        if card2 == 0:
                                            card2 = ii
                                        else:
                                            card2 += ii * 3
                                z = ii
                            if pair > 2:
                                pair = 2
                            if pair != 0:
                                print(f"there is {pair} pairs in here")
                                score2 += pair
                            else:
                                print("Biggest card")
                                score2 = 0
                                i.sort()
                                card2 = y[0][6]
                            # the code above is checking pairs and Big card


    # the following code is for compare the cards
    print(card)
    print(card1)
    if score > score1 and score > score2:
        won = "You won!"
        c=1
    elif score1 > score and score1 > score2:
        won = "Bot 1 won!"
        c=-1
    elif score2 > score and score2 > score1:
        won = "Bot 2 won!"
        c=-1
    elif (score > score1 and score == score2):
        if card > card2:
            won = "You won!"
            c=1
        elif card2 > card:
            won = "Bot 2 won!"
            c=-1
        else:
            won = "It's a draw!"
            c=0.5
    elif (score > score2 and score == score1):
        if card > card1:
            won = "You won!"
            c=1
        elif card1 > card:
            won = "Bot 1 won!"
            c=-1
        else:
            won = "It's a draw!"
            c=0.5
    elif score < score1: # player lost anyway, no need to compare bots' card
        won = "You lost!"
        c=-1
    else:
        if card > card1 and card > card2:
            won = "You won!"
            c=1
        elif card1 > card and card1 > card2:
            won = "Bot 1 won!"
            c=-1
        elif card2 > card and card2 > card1:
            won = "Bot 2 won!"
            c=-1
        elif (card == card1 and card > card2) or (card == card2 and card > card1):
            won = "It's a draw!"
            c=0.5
        elif card < card1:
            won = "You lost!"
            c=-1
        else:
            won = "It's a draw!"
    print("\n")

    
    if q == 0:
        if c == 1:
            money += bet * 3
            stat=2
        if c == 0.5:
            money += bet * 1.5
            stat=1
        if c == 0:
            money += bet
            stat=-1
        # if Bot win, player lose the bet money


    # after update money, we need to update to the data.db
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Money SET money = ?, won = ? WHERE id = ?", (money,stat,1))
    conn.commit()
    conn.close()

        
    return render_template("play.html", title="play", stat=stat, cards=cardss, cardsp=cardssp, cards1=cardss1, cards2=cardss2, won=won, money=money, money1=money2)


if __name__ == "__main__":
    app.run(debug=True)