import random

#Message that prints when program is started
print("Roll-a-Die")
print("\nTo roll a die, type \"Roll\"", end="")
print(" and then type the number of sides the die should have")
print("Or, if you want to flip a coin instead, type \"Flip a coin\"")
print("\nWhen you want to close this program, type \"Quit\"\n")

command = input()

closed = False

while closed == False:

#code that lets the user exit the program
    if command == "Quit":
        exit()

#code for rolling a die
    if command == "Roll":
        print("How many sides should the die have?")
        sides = int(input())
        print(random.randint(1, sides))
        command = input()

#code for flipping a coin
    if command == "Flip a coin":
        face = random.randint(1, 2)
        if face == 1:
            print("Heads")
            command = input()
        if face!= 1:
            print("Tails")
            command = input()

