from flask import Flask, render_template, request
import sqlite3
import random


selected_cards = []
random_card = 0
player_cards = []
money = 2000
bot1_cards = []
public_cards = []
bot2_cards = []

# The following code is for creating a table called 'Money'
# This is for storage of varible - money
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# if the data.db is intialized, we need to add table
cursor.execute('''CREATE TABLE IF NOT EXISTS Money
(id INTEGER PRIMARY KEY, money INTEGER, won INTEGER)''')
conn.commit()

cursor.execute('''UPDATE Money SET money = ?, won = ?
WHERE id = ?''', (money, 0, 1))
if cursor.rowcount == 0:  # if the data.db is intialized, we need to add data
    cursor.execute('''INSERT INTO Money (id, money, won)
    VALUES (?, ?, ?)''', (1, money, 0))
conn.commit()

conn.close()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home1.html", title="home")


@app.route("/instruction")
def instruction():
    return render_template("instruction.html", title="instruction")


@app.route("/play", methods=["GET", "POST"])
def play():
    bot1_score = 0
    bot2_score = 0
    fold_status = 0
    if request.method == "POST":
        if "fold" in request.form:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            cursor.execute('''select Money.money, Money.won
            from Money where id=1''')
            game_status = cursor.fetchone()
            previous_winning_status = game_status[1]
            money = game_status[0]
            conn.close()
            # Player folds, Bot with the highest score wins
            # don't need to check for draw if player fold, player lose anyway
            if bot1_score > bot2_score:
                winning_status = "Bot 1 won!"
            else:
                winning_status = "Bot 2 won!"
            fold_status += 1
            money += 100  # Player get back half the bet, reward for folding
            if previous_winning_status == -1:
                money -= 200
            if previous_winning_status == 1:
                money -= 300
            if previous_winning_status == 2:
                money -= 600
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            cursor.execute('''UPDATE Money SET money = ?
            WHERE id = ?''', (money, 1))
            conn.commit()
            conn.close()

    player_cards = []
    bot1_cards = []
    bot2_cards = []
    public_cards = []
    selected_cards = []
    calculation_list = []
    player_numbers = []
    player_suits = []
    random_card = 0
    selected_cards = []
    bot1_numbers = []
    bot1_suits = []
    bot2_numbers = []
    bot2_suits = []
    public_numbers = []
    public_suits = []
    winning_status = "none"
    bet = 200
    bot1_score = 0
    bot2_score = 0
    fold_status = 0
    previous_winning_status = 0
    winning_info = 0

    # the following code is for extract data from table - "Money"
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("select Money.money from Money where id=1")
    moneylist = cursor.fetchone()
    money = moneylist[0]
    conn.close()
    money_before_bet = money
    money -= bet

    if money < 0:
        money = 2000
        # after update money, we need to update to the data.db
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE Money SET money = ?
                       WHERE id = ?''', (money, 1))
        conn.commit()
        conn.close()
        return render_template("restart.html", title="play")

    # player's cards extraction
    for i in range(1, 3):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        random_card = random.randint(1, 52)
        while selected_cards.count(random_card) >= 1:
            random_card = random.randint(1, 52)
        cursor.execute(f'''SELECT Card.id, Colour.colours, Number.numbers,
                    Card.name, Card.media
                       FROM Card JOIN Colour ON Card.colour = Colour.id
                       JOIN CardNumber ON Card.id = CardNumber.card_id
                       JOIN Number ON CardNumber.number_id = Number.id
                       WHERE Card.id = {random_card} ORDER BY Card.id''')
        cards = cursor.fetchone()
        selected_cards.append(cards[0])
        player_cards.append(cards)
        player_numbers.append(cards[2])
        player_suits.append(cards[1])
        conn.close()

        # Bot's cards extraction
    for i in range(1, 3):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        random_card = random.randint(1, 52)
        while selected_cards.count(random_card) >= 1:
            random_card = random.randint(1, 52)
        cursor.execute(f'''SELECT Card.id, Colour.colours, Number.numbers,
        Card.name, Card.media
                       FROM Card JOIN Colour ON Card.colour = Colour.id
                       JOIN CardNumber ON Card.id = CardNumber.card_id
                       JOIN Number ON CardNumber.number_id = Number.id
                       WHERE Card.id = {random_card} ORDER BY Card.id''')
        cards = cursor.fetchone()
        selected_cards.append(cards[0])
        bot1_cards.append(cards)
        bot1_numbers.append(cards[2])
        bot1_suits.append(cards[1])
        conn.close()

        # bot2's cards extraction
    for i in range(1, 3):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        random_card = random.randint(1, 52)
        while selected_cards.count(random_card) >= 1:
            random_card = random.randint(1, 52)
        cursor.execute(f'''SELECT Card.id, Colour.colours, Number.numbers,
        Card.name, Card.media FROM Card
                       JOIN Colour ON Card.colour = Colour.id
                       JOIN CardNumber ON Card.id = CardNumber.card_id
                       JOIN Number ON CardNumber.number_id = Number.id
                       WHERE Card.id = {random_card} ORDER BY Card.id''')
        cards = cursor.fetchone()
        selected_cards.append(cards[0])
        bot2_cards.append(cards)
        bot2_numbers.append(cards[2])
        bot2_suits.append(cards[1])
        conn.close()

        # public cards cards extraction
    for i in range(1, 6):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        random_card = random.randint(1, 52)
        while selected_cards.count(random_card) >= 1:
            random_card = random.randint(1, 52)
        cursor.execute(f'''SELECT Card.id, Colour.colours, Number.numbers,
        Card.name, Card.media
                       FROM Card JOIN Colour ON Card.colour = Colour.id
                       JOIN CardNumber ON Card.id = CardNumber.card_id
                       JOIN Number ON CardNumber.number_id = Number.id
                       WHERE Card.id = {random_card} ORDER BY Card.id''')
        cards = cursor.fetchone()
        selected_cards.append(cards[0])
        public_cards.append(cards)
        public_numbers.append(cards[2])
        public_suits.append(cards[1])
        conn.close()

    # The following code is for assess the cards of player
    previous_number = 0
    player_score = 0
    match_found = False
    player_largest = 0
    player_numbers.extend(public_numbers)
    player_suits.extend(public_suits)
    calculation_list.append(player_numbers)
    for i in calculation_list:
        i.sort()
        if len(i) != 7:
            print("wrong amount")
            exit()
        for current_number in i:
            try:
                current_number = int(current_number)
                if 2 <= current_number <= 14:
                    for rank_candidate in range(2, 15):
                        if i.count(rank_candidate) > 3:
                            match_found = True
                            player_largest = rank_candidate
                else:
                    print("wrong input")
                    exit()
            except ValueError:
                print("wrong")
                exit()
    if match_found is True:
        print("there is a four of a kind in here")
        player_score += 7
        # the code above is checking the 4 of a kind
    else:
        previous_number = 0
        match_found = False
        for i in calculation_list:
            i.sort()
            for rank_candidate in range(2, 15):
                if i.count(rank_candidate) > 2:
                    for secondary_rank in range(2, 15):
                        if secondary_rank != rank_candidate:
                            if i.count(secondary_rank) > 1:
                                match_found = True
                                player_largest = (
                                    rank_candidate + secondary_rank * 0.01
                                )
        if match_found is True:
            print("there is a full house in here")
            player_score += 6
            # the code above is checking full house
        else:
            previous_number = 0
            match_found = False
            player_suits.sort()
            player_suits.reverse()
            for suit_candidate in range(1, 5):
                if player_suits.count(suit_candidate) > 4:
                    for unique_number in range(0, 5):
                        match_found = True
                        player_largest = calculation_list[0][unique_number]
                        if player_suits[unique_number] != suit_candidate:
                            continue
            if match_found is True:
                previous_number = 0
                straight_counter = 0
                straight_found = False
                for i in calculation_list:
                    i.sort()
                    i.reverse()
                    for current_number in i:
                        try:
                            current_number = int(current_number)
                            if previous_number != 0:
                                if current_number-previous_number == -1:
                                    straight_counter = straight_counter+1
                                elif current_number-previous_number == 0:
                                    straight_counter = straight_counter
                                else:
                                    straight_counter = 0
                            previous_number = current_number
                            if straight_counter >= 4:
                                straight_found = True
                                player_largest = previous_number
                        except ValueError:
                            print("wrong")
                            exit()
                if straight_found is True:
                    print("it's a straight flush")
                    player_score += 10
                else:
                    print("there is a flush in here")
                    player_score += 5
            # the code above is checking flush and stright flush
            # because the 7 cards can not form full house and flush at once
            # the assess of stright flush can go after the full house
            else:
                previous_number = 0
                straight_counter = 0
                straight_found = False
                for i in calculation_list:
                    i.sort()
                    i.reverse()
                    for current_number in i:
                        try:
                            current_number = int(current_number)
                            if previous_number != 0:
                                if current_number-previous_number == -1:
                                    straight_counter = straight_counter+1
                                elif current_number-previous_number == 0:
                                    straight_counter = straight_counter
                                else:
                                    straight_counter = 0
                            previous_number = current_number
                            if straight_counter >= 4:
                                straight_found = True
                                player_largest = previous_number
                                break
                        except ValueError:
                            print("wrong")
                            exit()
                if straight_found is True:
                    print("it's a straight")
                    player_score += 4
                    # the code above is checking the straight_found
                else:
                    previous_number = 0
                    match_found = False
                    for i in calculation_list:
                        i.sort()
                        for rank_candidate in range(2, 15):
                            if i.count(rank_candidate) > 2:
                                match_found = True
                                player_largest = rank_candidate
                    if match_found is True:
                        print("there is a three of a kind in here")
                        player_score += 3
                        # the code above is checking the 3 of a kind
                    else:
                        pair = 0
                        previous_number = 0
                        for i in calculation_list:
                            i.sort()
                            for current_number in i:
                                current_number = int(current_number)
                                if previous_number != 0:
                                    if current_number == previous_number:
                                        pair = pair + 1
                                        if player_largest == 0:
                                            player_largest = current_number
                                        else:
                                            current_number *= 3
                                            player_largest += current_number
                                            current_number /= 3
                                previous_number = current_number
                            if pair > 2:
                                pair = 2
                            if pair != 0:
                                print(f"there is {pair} pairs in here")
                                player_score += pair
                            else:
                                print("Biggest player_largest")
                                player_score = 0
                                i.sort()
                                player_largest = calculation_list[0][6]
                            # the code above is checking pairs and Big pcard

    # The following code is for assess the cards of CPU
    previous_number = 0
    bot1_score = 0
    calculation_list = []
    match_found = False
    bot1_largest = 0
    bot1_numbers.extend(public_numbers)
    bot1_suits.extend(public_suits)
    calculation_list.append(bot1_numbers)
    calculation_list.sort()
    for i in calculation_list:
        i.sort()
        if len(i) != 7:
            print("wrong amount")
            exit()
        for current_number in i:
            try:
                current_number = int(current_number)
                if 2 <= current_number <= 14:
                    for rank_candidate in range(2, 15):
                        if i.count(rank_candidate) > 3:
                            match_found = True
                            bot1_largest = rank_candidate
                else:
                    print("wrong input")
                    exit()
            except ValueError:
                print("wrong")
                exit()
    if match_found is True:
        print("there is a four of a kind in here")
        bot1_score += 7
        # the code above is checking the 4 of a kind
    else:
        previous_number = 0
        match_found = False
        for i in calculation_list:
            i.sort()
            for rank_candidate in range(2, 15):
                if i.count(rank_candidate) > 2:
                    for secondary_rank in range(2, 15):
                        if secondary_rank != rank_candidate:
                            if i.count(secondary_rank) > 1:
                                match_found = True
                                bot1_largest = (
                                    rank_candidate + secondary_rank * 0.01
                                )
        if match_found is True:
            print("there is a full house in here")
            bot1_score += 6
            # the code above is checking full house
        else:
            previous_number = 0
            match_found = False
            bot1_suits.sort()
            bot1_suits.reverse()
            for suit_candidate in range(1, 5):
                if bot1_suits.count(suit_candidate) > 4:
                    for unique_number in range(0, 5):
                        match_found = True
                        bot1_largest = calculation_list[0][unique_number]
                        if bot1_suits[unique_number] != suit_candidate:
                            continue
            if match_found is True:
                previous_number = 0
                straight_counter = 0
                straight_found = False
                for i in calculation_list:
                    i.sort()
                    i.reverse()
                    for current_number in i:
                        try:
                            current_number = int(current_number)
                            if previous_number != 0:
                                if current_number-previous_number == -1:
                                    straight_counter = straight_counter+1
                                elif current_number-previous_number == 0:
                                    straight_counter = straight_counter
                                else:
                                    straight_counter = 0
                            previous_number = current_number
                            if straight_counter >= 4:
                                straight_found = True
                                bot1_largest = previous_number
                        except ValueError:
                            print("wrong")
                            exit()
                if straight_found is True:
                    print("it's a straight flush")
                    bot1_score += 10
                else:
                    print("there is a flush in here")
                    bot1_score += 5
            # the code above is checking flush and stright flush
            # because the 7 cards can not form full house and flush at once
            # the assess of stright flush can go after the full house
            else:
                previous_number = 0
                straight_counter = 0
                straight_found = False
                for i in calculation_list:
                    i.sort()
                    i.reverse()
                    for current_number in i:
                        try:
                            current_number = int(current_number)
                            if previous_number != 0:
                                if current_number-previous_number == -1:
                                    straight_counter = straight_counter+1
                                elif current_number-previous_number == 0:
                                    straight_counter = straight_counter
                                else:
                                    straight_counter = 0
                            previous_number = current_number
                            if straight_counter >= 4:
                                straight_found = True
                                bot1_largest = previous_number
                                break
                        except ValueError:
                            print("wrong")
                            exit()
                if straight_found is True:
                    print("it's a straight")
                    bot1_score += 4
                    # the code above is checking the straight_found
                else:
                    previous_number = 0
                    match_found = False
                    for i in calculation_list:
                        i.sort()
                        for rank_candidate in range(2, 15):
                            if i.count(rank_candidate) > 2:
                                match_found = True
                                bot1_largest = rank_candidate
                    if match_found is True:
                        print("there is a three of a kind in here")
                        bot1_score += 3
                        # the code above is checking the 3 of a kind
                    else:
                        pair = 0
                        previous_number = 0
                        for i in calculation_list:
                            i.sort()
                            for current_number in i:
                                current_number = int(current_number)
                                if previous_number != 0:
                                    if current_number == previous_number:
                                        pair = pair + 1
                                        if bot1_largest == 0:
                                            bot1_largest = current_number
                                        else:
                                            bot1_largest += current_number * 3
                                previous_number = current_number
                            if pair > 2:
                                pair = 2
                            if pair != 0:
                                print(f"there is {pair} pairs in here")
                                bot1_score += pair
                            else:
                                print("Biggest player_largest")
                                bot1_score = 0
                                i.sort()
                                bot1_largest = calculation_list[0][6]
                            # the code above is checking pairs and Big card

# The following code is for assess the cards of CPU2
    previous_number = 0
    bot2_score = 0
    calculation_list = []
    match_found = False
    bot2_largest = 0
    bot2_numbers.extend(public_numbers)
    bot2_suits.extend(public_suits)
    calculation_list.append(bot2_numbers)
    calculation_list.sort()
    for i in calculation_list:
        i.sort()
        if len(i) != 7:
            print("wrong amount")
            exit()
        for current_number in i:
            try:
                current_number = int(current_number)
                if 2 <= current_number <= 14:
                    for rank_candidate in range(2, 15):
                        if i.count(rank_candidate) > 3:
                            match_found = True
                            bot2_largest = rank_candidate
                else:
                    print("wrong input")
                    exit()
            except ValueError:
                print("wrong")
                exit()
    if match_found is True:
        print("there is a four of a kind in here")
        bot2_score += 7
        # the code above is checking the 4 of a kind
    else:
        previous_number = 0
        match_found = False
        for i in calculation_list:
            i.sort()
            for rank_candidate in range(2, 15):
                if i.count(rank_candidate) > 2:
                    for secondary_rank in range(2, 15):
                        if secondary_rank != rank_candidate:
                            if i.count(secondary_rank) > 1:
                                match_found = True
                                bot2_largest = (
                                    rank_candidate + secondary_rank * 0.01
                                )
        if match_found is True:
            print("there is a full house in here")
            bot2_score += 6
            # the code above is checking full house
        else:
            previous_number = 0
            match_found = False
            bot2_suits.sort()
            bot2_suits.reverse()
            for suit_candidate in range(1, 5):
                if bot2_suits.count(suit_candidate) > 4:
                    for unique_number in range(0, 5):
                        match_found = True
                        bot2_largest = calculation_list[0][unique_number]
                        if bot2_suits[unique_number] != suit_candidate:
                            continue
            if match_found is True:
                previous_number = 0
                straight_counter = 0
                straight_found = False
                for i in calculation_list:
                    i.sort()
                    i.reverse()
                    for current_number in i:
                        try:
                            current_number = int(current_number)
                            if previous_number != 0:
                                if current_number-previous_number == -1:
                                    straight_counter = straight_counter+1
                                elif current_number-previous_number == 0:
                                    straight_counter = straight_counter
                                else:
                                    straight_counter = 0
                            previous_number = current_number
                            if straight_counter >= 4:
                                straight_found = True
                                bot2_largest = previous_number
                        except ValueError:
                            print("wrong")
                if straight_found is True:
                    print("it's a straight flush")
                    bot2_score += 10
                else:
                    print("there is a flush in here")
                    bot2_score += 5
            # the code above is checking flush and stright flush
            # because the 7 cards can not form full house and flush at once
            # the assess of stright flush can go after the full house
            else:
                previous_number = 0
                straight_counter = 0
                straight_found = False
                for i in calculation_list:
                    i.sort()
                    i.reverse()
                    for current_number in i:
                        try:
                            current_number = int(current_number)
                            if previous_number != 0:
                                if current_number-previous_number == -1:
                                    straight_counter = straight_counter+1
                                elif current_number-previous_number == 0:
                                    straight_counter = straight_counter
                                else:
                                    straight_counter = 0
                            previous_number = current_number
                            if straight_counter >= 4:
                                straight_found = True
                                bot2_largest = previous_number
                                break
                        except ValueError:
                            print("wrong")
                            exit()
                if straight_found is True:
                    print("it's a straight")
                    bot2_score += 4
                    # the code above is checking the straight_found
                else:
                    previous_number = 0
                    match_found = False
                    for i in calculation_list:
                        i.sort()
                        for rank_candidate in range(2, 15):
                            if i.count(rank_candidate) > 2:
                                match_found = True
                                bot2_largest = rank_candidate
                    if match_found is True:
                        print("there is a three of a kind in here")
                        bot2_score += 3
                        # the code above is checking the 3 of a kind
                    else:
                        pair = 0
                        previous_number = 0
                        for i in calculation_list:
                            i.sort()
                            for current_number in i:
                                current_number = int(current_number)
                                if previous_number != 0:
                                    if current_number == previous_number:
                                        pair = pair + 1
                                        if bot2_largest == 0:
                                            bot2_largest = current_number
                                        else:
                                            bot2_largest += current_number * 3
                                previous_number = current_number
                            if pair > 2:
                                pair = 2
                            if pair != 0:
                                print(f"there is {pair} pairs in here")
                                bot2_score += pair
                            else:
                                print("Biggest player_largest")
                                bot2_score = 0
                                i.sort()
                                bot2_largest = calculation_list[0][6]
                            # the code above is checking pairs and Big card
    # the following code is for compare the cards
    if fold_status == 0:
        print(player_largest)
        print(bot1_largest)
        if player_score > bot1_score and player_score > bot2_score:
            winning_status = "You won 400!"
            winning_info = 1
        elif bot1_score > player_score and bot1_score > bot2_score:
            winning_status = "Bot 1 won, you lost 200!"
            winning_info = -1
        elif bot2_score > player_score and bot2_score > bot1_score:
            winning_status = "Bot 2 won, you lost 200!"
            winning_info = -1
        elif (player_score > bot1_score and player_score == bot2_score):
            if player_largest > bot2_largest:
                winning_status = "You won 400!"
                winning_info = 1
            elif bot2_largest > player_largest:
                winning_status = "Bot 2 won, you lost 200!"
                winning_info = -1
            else:
                winning_status = "It's a draw, you won 100!"
                winning_info = 0.5
        elif (player_score > bot2_score and player_score == bot1_score):
            if player_largest > bot1_largest:
                winning_status = "You won 400!"
                winning_info = 1
            elif bot1_largest > player_largest:
                winning_status = "Bot 1 won, you lost 200!"
                winning_info = -1
            else:
                winning_status = "It's a draw, you won 100!"
                winning_info = 0.5
        elif player_score < bot1_score:  # player lost anyway,no need to compar
            winning_status = "You lost 200!"
            winning_info = -1
        else:
            if player_largest > bot1_largest and player_largest > bot2_largest:
                winning_status = "You won 400!"
                winning_info = 1
            elif bot1_largest > player_largest and bot1_largest > bot2_largest:
                winning_status = "Bot 1 won, you lost 200!"
                winning_info = -1
            elif bot2_largest > player_largest and bot2_largest > bot1_largest:
                winning_status = "Bot 2 won, you lost 200!"
                winning_info = -1
            elif (player_largest == bot1_largest and
                  player_largest > bot2_largest):
                winning_status = "It's a draw, you won 100!"
                winning_info = 0.5
            elif (player_largest == bot2_largest and
                  player_largest > bot1_largest):
                winning_status = "It's a draw, you won 100!"
                winning_info = 0.5
            elif player_largest < bot1_largest:
                winning_status = "You lost 200!"
                winning_info = -1
            else:
                winning_status = "It's a draw, you lost nothing!"
        print("\n")

        if winning_info == 1:
            money += bet * 3
            previous_winning_status = 2
        if winning_info == 0.5:
            money += bet * 1.5
            previous_winning_status = 1
        if winning_info == 0:
            money += bet
            previous_winning_status = -1
        # if Bot win, player lose the bet money

    # after update money, we need to update to the data.db
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE Money SET money = ?, won = ?
    WHERE id = ?''', (money, previous_winning_status, 1))
    conn.commit()
    conn.close()

    return render_template("play.html",
                           title="play",
                           stat=previous_winning_status,
                           cards=player_cards,
                           cardsp=public_cards,
                           cards1=bot1_cards,
                           cards2=bot2_cards,
                           won=winning_status,
                           money=money,
                           money1=money_before_bet)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
