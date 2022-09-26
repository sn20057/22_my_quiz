import random

rounds = 15
lives = 3

for item in range(0, 15):
    math_num1 = random.randint(1, 12)
    math_num2 = random.randint(1, 12)

    # questions 1 to 15
    answer = math_num1 * math_num2
    question = int(input("What is {} x {} = ".format(math_num1, math_num2)))
    lives -= 1
    rounds -= 1

    # 5 questions within 1
    if question == answer:
        print("Correct\n")
        lives += 1
        print("Lives {} \n".format(lives))
        print("{}/15 Round's Remaining ".format(rounds))

    elif question != answer:
        print("Incorrect\n")
        print("Answer is {} \n".format(answer))
        print("Lives Remaining {} ".format(lives))
        print("{}/15 Round's Remaining \n".format(rounds))

    elif rounds == 0:
        print("Have Completed The Quiz Successfully")
        print("Your Remaining Lives Are{}".format(lives))

    elif lives == 0:
        print("you have run out of lives")




















