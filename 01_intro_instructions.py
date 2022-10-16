# Functions go here
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
    print("HOW TO PLAY")
    print("The rules of the game here\n")
    print("There are 15 random multiplication questions")
    print("You have 3 lives, if you get one question wrong you\n"
          "Lose a life, you get one right you keep that life")
    print("If you lose your 3 lives you lose. If you\n"
          "Survive the 15 rounds you win\n")
    return""


# Main routine goes here

print("Welcome to my quiz game\n")

played_before = yes_no("Have you played this game before?\n ")

# if user hasn't played display the instructions
if played_before == "No":
    instructions()
    print("Program Continues")

else:
    print("Program Continues")
