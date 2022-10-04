# Made by u/dumbrandomkid or Draco Silver or Dominator

import random
import time

# Current difficulty 1 for playable 2 for unplayable
difficulty = "none"

# Required vairables
numbers = ["1", "2", "3", "4", "5", "6"]
p_isBatting = False
p_hasBatted = False
py_hasBatted = False
totalPlayerScore = 0
totalPythonScore = 0

# Funcition to toss
def tossBatorBall():
    global p_hasBatted
    global py_hasBatted
    global p_isBatting
    print("Selecting bat or ball for you....")
    tossResult = random.randint(0, 1)
    if tossResult == 0:
        p_isBatting = True
        p_hasBatted = False
        print("You got batting! Show this thing your luck.")
    else:
        p_isBatting = False
        p_hasBatted = False
        py_hasBatted = False
        print("You gotta throw some balls but in CLI.")


def game_playable():
    global totalPlayerScore
    global totalPythonScore
    global p_hasBatted
    global py_hasBatted
    global p_isBatting

    p_choosenNum = input("Enter anything from 1 to 6 :")

    choosenNum = random.choice(numbers)

    print(f"Your choice : {p_choosenNum}, Python's choice : {choosenNum}")
    over()
    print()
    print(f"python has batted? " + str(py_hasBatted))
    print(f"player has batted? " + str(p_hasBatted))
    print()

    if p_isBatting and p_hasBatted == False:
        if p_choosenNum.isdecimal() != True:
            print("Baka! enter only numbers!")

        elif float(p_choosenNum) > 6 or float(p_choosenNum) < 1:
            print("Bruh idiot!!!. Don't choose too big or small......")

        elif p_choosenNum == choosenNum and p_isBatting:
            print("Player Out!")
            print(f"Your score {totalPlayerScore}")
            p_hasBatted = True
            choosenNum = 0
            if py_hasBatted == False:
                p_isBatting = False
                choosenNum = 0
            # else:
            #     over()

        elif p_choosenNum != choosenNum and p_choosenNum.isdecimal() and p_isBatting:
            totalPlayerScore = float(p_choosenNum) + totalPlayerScore
            print(f"Your score {totalPlayerScore}")

        else:
            pass

    if py_hasBatted == False and p_isBatting == False:

        if p_choosenNum.isdecimal() != True:
            print("Baka! enter only numbers!")

        if float(p_choosenNum) > 6 or float(p_choosenNum) < 1:
            print("Bruh idiot!!!. Don't choose too big or small......")

        if p_choosenNum == choosenNum and p_isBatting == False:
            # print("Python Out!")
            py_hasBatted == True
            choosenNum = 0
            # print(f"Python score {totalPythonScore}")
            if p_hasBatted == False:
                print("Python Out!")
                py_hasBatted == True
                print(f"Python score {totalPythonScore}")
                p_isBatting = True
            else:
                over()

        elif p_choosenNum != choosenNum and p_choosenNum.isdecimal() and p_isBatting == False:
            totalPythonScore = float(choosenNum) + totalPythonScore
            print(f"Python score {totalPythonScore}")

        else:
            pass

def over():
    # if p_hasBatted == True and py_hasBatted == True:
    if totalPlayerScore > totalPythonScore and py_hasBatted:
        print(" OVER !")
        print("##################################")
        print()
        print(" You Won!")
        time.sleep(3)
        exit()

    if totalPlayerScore < totalPythonScore and p_hasBatted:
        print(" OVER !")
        print("##################################")
        print()
        print(" Python Won! Better luck next time.")
        time.sleep(3)
        exit()

    if totalPlayerScore == totalPlayerScore and py_hasBatted and p_hasBatted:
        print(" OVER !")
        print("##################################")
        print()
        print("Tie!!")
        time.sleep(3)
        exit()


# chooseDifficulty()
tossBatorBall()
while True:
    game_playable()


