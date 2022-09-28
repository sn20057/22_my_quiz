import random

rounds = 15
lives = 3
error = "Please enter a whole digit"

for item in range(0, 15):
    # Creates the random numbers for each multiplication from 1 to 12
    math_num1 = random.randint(1, 12)
    math_num2 = random.randint(1, 12)

    # questions 1 to 15
    answer = math_num1 * math_num2
    question = int(input("What is {} x {} = ".format(math_num1, math_num2)))
    lives -= 1
    rounds -= 1

    # If user answer correct
    if question == answer:
        print("Correct\n")
        # They keep their life and displays how many they have left
        lives += 1
        print("Lives {} \n".format(lives))
        # Display's how many rounds are left in the quiz
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
