#Program 2: Addition Quiz
#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random

rand1 = random.randint(0,99)
rand2 = random.randint(0,99)

score = 10

def questions():
    print("Question Number 1")
    print(f"What is {rand1} + {rand2}")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer:"))
    if randAns == userAns:
        print("Correct")
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        score - 1
    print("Question Number 2")
    print(f"What is {rand1} + {rand2}")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer:"))
    if randAns == userAns:
        print("Correct")
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        score - 1
    print("Question Number 3")
    print(f"What is {rand1} + {rand2}")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer:"))
    if randAns == userAns:
        print("Correct")
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        score - 1
    
questions()
