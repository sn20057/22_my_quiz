import random
# functions here


def yes_no(question2):
    valid = False
    while not valid:
        # ask user for input
        response = input(question2).lower().strip()
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


# Checks for incorrect input and displays an error message if so
def num_check(question):
    error = "Please enter a whole digit"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print(error)


# main routine here
print("Welcome to my quiz\n")

played_before = yes_no("Have you played this game before? ")

# if user hasn't played display the instructions
if played_before == "No":
    instructions()

rounds_played = 0
rounds = 15
lives = 3

for item in range(0, 15):
    # Creates the random numbers for each multiplication from 1 to 12
    math_num1 = random.randint(1, 12)
    math_num2 = random.randint(1, 12)

    if rounds == 15:
        input("Press <Enter> to start playing...")

    # questions 1 to 1
    answer = math_num1 * math_num2

    lives -= 1
    rounds -= 1
    question = int(input("What is {} x {} = ".format(math_num1, math_num2)))

    # If user answer correct
    if question == answer:
        print("Correct\n")
        # They keep their life and displays how many they have left
        lives += 1
        print("Lives {} \n".format(lives))
        # Display's how many rounds are left in the quiz
        if rounds != 0:
            print("{}/15 Round's Remaining ".format(rounds))

    # If user is incorrect
    elif question != answer:
        print("Incorrect\n")
        # shows the right answer for the question
        print("Answer is {} \n".format(answer))
        # Display's remaining lives
        print("Lives Remaining {} ".format(lives))
        # Shows the rounds remaining
        print("{}/15 Round's Remaining \n".format(rounds))
        # Adds another round so user has to get answer correct to continue
        rounds += 1
        # If lives are equal to 0 the game ends and the user loses
        if lives == 0:
            print("you have run out of lives")
            break

    # If rounds are equal to 0 the game ends the user wins
    if rounds == 0:
        # Congratulations message
        print("You Have Completed The Quiz Successfully")
        # Shows how many the user has remaining
        print("Your Remaining Lives Are {}".format(lives))
        # A thankyou message
        print("Thank for playing my Quiz :)")
