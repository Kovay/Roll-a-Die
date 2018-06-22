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
        print("How many sides should the die have?")
        sides = int(input())
        print("How many dice do you want to roll?")
        die_num = int(input())
        for num_of_die in range(1, die_num + 1):
            print(random.randint(1, sides))
        command = input()

    # code for flipping a coin
    if command == "Flip a coin":
        print("How many coins do you want to flip?")
        coin_num = int(input())
        for num_of_coin in range(1, coin_num + 1):
            face = random.randint(1, 2)
            if face == 1:
                print("Heads")
            if face != 1:
                print("Tails")
        command = input()
