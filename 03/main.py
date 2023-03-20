from collections import Counter
import random

if __name__ == '__main__':
    #zadanie 1
    data = input("podaj liczby: ").split(",")
    max_number = data[0]
    min_number = data[0]
    for d in data:
        if max_number < d:
            max_number = d
        if min_number > d:
            min_number = d
    print(f"max number: {max_number}")
    print(f"min number: {min_number}")

    #zadanie 2
    cities = [
        "miasto 1",
        "miasto 2",
        "miasto 3",
        "miasto 4",
        "miasto 5",
        "miasto 6",
        "miasto 7",
        "miasto 8",
        "miasto 9",
        "miasto 10",
    ]
    not_to_use = []
    for i in range(1, 11):
        rand = random.randrange(10)
        while rand in not_to_use:
            rand = random.randrange(10)
        not_to_use.append(rand)
        print(f"Miaso {i}: {cities[rand]}")

    #zadanie 3
    rounds = int(input("rounds: "))
    mode = input("single/multi: ")
    score = []
    if mode == "multi":
        player1_name = input("player 1 name: ")
        player2_name = input("player 2 name: ")
        print("start")
        for i in range(rounds):
            rps1 = input(f"{player1_name}: ")
            rps2 = input(f"{player2_name}: ")
            if rps1 == rps2:
                print("no one won")
                score.append(0)
            elif rps1 == "rock" and rps2 == "scissors":
                print(f"{player1_name} won")
                score.append(1)
            elif rps1 == "paper" and rps2 == "rock":
                print(f"{player1_name} won")
                score.append(1)
            elif rps1 == "scissors" and rps2 == "paper":
                print(f"{player1_name} won")
                score.append(1)
            else:
                print(f"{player2_name} won")
                score.append(2)
    else:
        choices = ["rock", "paper", "scissors"]
        player1_name = choices[random.randrange(2)]
        player2_name = input("player 2 name: ")
        print("start")
        for i in range(rounds):
            rps1 = input("player 1: ")
            rps2 = input("player 2: ")
            if rps1 == rps2:
                print("no one won")
                score.append(0)
            elif rps1 == "rock" and rps2 == "scissors":
                print(f"{player1_name} won")
                score.append(1)
            elif rps1 == "paper" and rps2 == "rock":
                print(f"{player1_name} won")
                score.append(1)
            elif rps1 == "scissors" and rps2 == "paper":
                print(f"{player1_name} won")
                score.append(1)
            else:
                print(f"{player2_name} won")
                score.append(2)
    who_won = Counter(score).most_common()
    if who_won == 0:
        print("no one won")
    elif who_won == 1:
        print("player 1 won")
    elif who_won == 2:
        print("player 2 won")