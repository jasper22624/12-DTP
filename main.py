import random
import time
while True:
    y = []
    y1 = []
    y2 = []
    yp = []
    for i in range(1, 3):
        y1.append(random.randint(2, 14))
    for i in range(1, 3):
        y2.append(random.randint(2, 14))
    for i in range(1, 6):
        yp.append(random.randint(2, 14))
    three = 0
    z = 0
    score = 0
    threes = False
# y.append(input("enter 7 nums,seperate with space, use 14 for A\n").split())
    sum = 0
    y1.extend(yp)
    y.append(y1)
    for i in y:
        i.sort()
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
        if threes is True:
            print("there is a full house in here")
            score += 6
            # the code above is checking full house
        else:
            z = 0
            T = 0
            ee = 0
            Straight = False
            for i in y:
                i.sort()
                i.reverse()
                print(i)
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
                            try:
                                ii = int(ii)
                                if 2 <= ii <= 14:
                                    if z != 0:
                                        if ii == z:
                                            pair = pair + 1
                                    z = ii
                                else:
                                    print("wrong input")
                                    break
                            except ValueError:
                                print("wrong")
                        if pair > 2:
                            pair = 2
                        if pair != 0:
                            print(f"there is {pair} pairs in here")
                            score += pair
                        else:
                            print("Biggest card")
                            score = 0
    three = 0
    z = 0
    score1 = 0
    y = []
    threes = False
# y.append(input("enter 7 nums,seperate with space, use 14 for A\n").split())
    sum = 0
    y2.extend(yp)
    y.append(y2)
    for i in y:
        i.sort()
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
        if threes is True:
            print("there is a full house in here")
            score1 += 6
            # the code above is checking full house
        else:
            z = 0
            T = 0
            ee = 0
            Straight = False
            for i in y:
                i.sort()
                i.reverse()
                print(i)
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
                            try:
                                ii = int(ii)
                                if 2 <= ii <= 14:
                                    if z != 0:
                                        if ii == z:
                                            pair = pair + 1
                                    z = ii
                                else:
                                    print("wrong input")
                                    break
                            except ValueError:
                                print("wrong")
                        if pair > 2:
                            pair = 2
                        if pair != 0:
                            print(f"there is {pair} pairs in here")
                            score1 += pair
                        else:
                            print("Biggest card")
                            score1 = 0
    if score > score1:
        print("player1 wins")
    elif score1 > score:
        print("player2 wins")
    else:
        print("it's a draw")
    time.sleep(10)
    print("\n")
