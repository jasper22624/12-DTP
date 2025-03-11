import random
import sqlite3
money = 2000
while True:
    money = money - 50
    print(f"your current money: ${money}, $50 paid for table fee")
    input("enter to continue")
    p = []
    p1 = []
    y = []
    f = False
    y1 = []
    y1c = []
    ran = 0
    select = []
    y2 = []
    y2c = []
    yp = []
    ypc = []
    for i in range(1, 3):
        cursor = sqlite3.connect('data.db').cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'select Card.id,Colour.colours,Number.numbers,Card.name from Card join Colour on Card.colour = Colour.id join Number on Card.number = Number.id where Card.id = {ran} order by Card.id')
        cards = cursor.fetchall()
        sqlite3.connect('data.db').close()
        select.append(cards[0][0])
        y1.append(cards[0][2])
        y1c.append(cards[0][1])
        p.append(cards[0][3])
        print(cards[0][3])
    if input("enter to continue, 'f' + enter to fold, $10 paid for table fee\n") == 'f':
        continue
    money = money - 10
    for i in range(1, 3):
        cursor = sqlite3.connect('data.db').cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'select Card.id,Colour.colours,Number.numbers,Card.name from Card join Colour on Card.colour = Colour.id join Number on Card.number = Number.id where Card.id = {ran} order by Card.id')
        cards = cursor.fetchall()
        sqlite3.connect('data.db').close()
        select.append(cards[0][0])
        y2.append(cards[0][2])
        y2c.append(cards[0][1])
        p1.append(cards[0][3])
    for i in range(1, 6):
        if i >= 4:
            if input("enter to continue, 'f' + enter to fold, $10 paid for table fee\n") == 'f':
                f = True
                break
            money = money - 10
        cursor = sqlite3.connect('data.db').cursor()
        ran = random.randint(1, 52)
        while select.count(ran) >= 1:
            ran = random.randint(1, 52)
        cursor.execute(f'select Card.id,Colour.colours,Number.numbers,Card.name from Card join Colour on Card.colour = Colour.id join Number on Card.number = Number.id where Card.id = {ran} order by Card.id')
        cards = cursor.fetchall()
        sqlite3.connect('data.db').close()
        select.append(cards[0][0])
        yp.append(cards[0][2])
        ypc.append(cards[0][1])
        p.append(cards[0][3])
        p1.append(cards[0][3])
        print(cards[0][3])
    if f == True:
        continue
    input("enter to continue")
    three = 0
    z = 0
    score = 0
    threes = False
    card = 0
# y.append(input("enter 7 nums,seperate with space, use 14 for A\n").split())
    sum = 0
    y1.extend(yp)
    y1c.extend(ypc)
    y.append(y1)
    for i in y:
        i.sort()
        p.sort()
        print(p)
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
        three = 0
        z = 0
        sum = 0
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
            three = 0
            z = 0
            sum = 0
            threes = False
            y1c.sort()
            for h in range(1, 5):
                if y1c.count(h) > 4:
                    threes = True
                    card = y[0][0]
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
                        except ValueError:
                            print("wrong")
                            exit()
                if Straight is True:
                    print("it's a straight")
                    score += 4
                    # the code above is checking the Straight
                else:
                    three = 0
                    z = 0
                    sum = 0
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
                            if len(i) != 7:
                                print("wrong amount")
                                break
                            for ii in i:
                                ii = int(ii)
                                if z != 0:
                                    if ii == z:
                                        pair = pair + 1
                                        card = ii
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
                                card = y[0][0]
    three = 0
    z = 0
    score1 = 0
    y = []
    threes = False
    card1 = 0
# y.append(input("enter 7 nums,seperate with space, use 14 for A\n").split())
    sum = 0
    y2.extend(yp)
    y2c.extend(ypc)
    y.append(y2)
    for i in y:
        i.sort()
        p1.sort()
        print(p1)
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
        three = 0
        z = 0
        sum = 0
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
            three = 0
            z = 0
            sum = 0
            threes = False
            y2c.sort()
            for h in range(1, 5):
                if y2c.count(h) > 4:
                    threes = True
                    card1 = y[0][0]
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
                        except ValueError:
                            print("wrong")
                            exit()
                if Straight is True:
                    print("it's a straight")
                    score1 += 4
                    # the code above is checking the Straight
                else:
                    three = 0
                    z = 0
                    sum = 0
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
                            if len(i) != 7:
                                print("wrong amount")
                                break
                            for ii in i:
                                ii = int(ii)
                                if z != 0:
                                    if ii == z:
                                        pair = pair + 1
                                        card1 = ii
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
                                card1 = y[0][0]
    if score > score1:
        print("you won")
        money += 180
    elif score1 > score:
        print("you lose")
        money -= 20
    else:
        if card > card1:
            print("you won")
            money += 180
        elif card1 > card:
            print("you lose")
            money -= 20
        else:
            print("it's a draw")
            money += 80
    input("enter to continue")
    print("\n")
