import random

# message that prints when program is started
print("Roll-a-Die")
print("\nTo roll a die, type \"Roll\"", end="")
print(" and then type the number of sides the die should have")
print("Or, if you want to flip a coin instead, type \"Flip a coin\"")
print("\nWhen you want to close this program, type \"Quit\"\n")

command = input()
running = "yes"

while running == "yes":

    # code that lets the user exit the program
    if command == "Quit":
        exit()

    # code for rolling a die
    if command == "Roll":
        # asks user how many sides the dice they are rolling should have
        print("How many sides should the die have?")
        sides = input()
        # checks if user input a number. if not, prints error message
        if sides.isnumeric() == False:
            print("Im not sure what you mean.")
            command = input()
            continue
        # asks user how many dice they want to roll
        print("How many dice do you want to roll?")
        die_num = input()
        # checks if user input a number. if not, prints error message
        if die_num.isnumeric() == False:
            print("Im not sure what you mean.")
            command = input()
            continue
        # prints a random number from 1, to the number of sides the user
        # selected, and loops for the number of dice the user decided to roll
        for num_of_dice in range(1, int(die_num) + 1):
            print(random.randint(1, int(sides)))
        command = input()
        continue

    # code for flipping a coin
    # asks user how many coins they want to flip
    if command == "Flip a coin":
        print("How many coins do you want to flip?")
        coin_num = input()
        # checks if user input a number. if not, prints error message
        if coin_num.isnumeric() == False:
            print("im not sure what you mean.")
            command = input()
            continue
        # prints wether the coin landed on heads or tails, for the number of
        # coins the user wanted to flip
        for coin in range(1, int(coin_num) + 1):
            face = random.randint(1, 2)
            if face == 1:
                print("Heads")
            if face == 2:
                print("Tails")
        command = input()
        continue

    # error message for when user inputs unknown command
    if command != "Flip a coin" or "Roll" or "Quit":
        print("Im not sure what you mean")
        command = input()
