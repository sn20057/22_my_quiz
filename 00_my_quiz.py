import random
# functions here


def yes_no(question):
    valid = False
    while not valid:
        # ask user for input
        response = input(question).lower().strip()
        # if no the instructions are displayed
        if response == "no" or response == "n":
            response = "No"
            return response
        # if yes the program continues
        elif response == "yes" or response == "y":
            response = "Yes"
            return response
        else:
            print("please enter Yes or No")


# instructions function on how to play
def instructions():
    print("- - - *HOW TO PLAY* - - -")
    print()
    print("The rules of the game here")
    print()
    return""


# main routine here
print("Welcome to my quiz game")

print()
played_before = yes_no("Have you played this game before? ")

# if user hasn't played display the instructions
if played_before == "No":
    instructions()

rounds_played = 0


