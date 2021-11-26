#Program 2: Addition Quiz
#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)
print("\n\033[31;1mAnswer the 10 Questions\033[0m\n")
user = input("Enter your Name: ")
import random

score = 0

def questions1():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 1")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad1 = score + 1
        return ad1
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad1 = score
        return ad1

def question2():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 2")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad2 = score + 1
        return ad2
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad2 = score
        return ad2
    
def question3():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 3")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad3 = score + 1
        return ad3
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad3 = score
        return ad3
    
   
def question4():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 4")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad4 = score + 1
        return ad4
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad4 = score
        return ad4
    
def question5():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 5")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad5 = score + 1
        return ad5
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad5 = score
        return ad5
    
def question6():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 6")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad6 = score + 1
        return ad6
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad6 = score
        return ad6

def question7():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 7")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad7 = score + 1
        return ad7
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad7 = score
        return ad7

def question8():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 8")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad8 = score + 1
        return ad8
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad8 = score
        return ad8

def question9():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 9")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad9 = score + 1
        return ad9
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad9 = score
        return ad9

def question10():
    rand1 = random.randint(0,99)
    rand2 = random.randint(0,99)
    print("\nQuestion Number 10")
    print(f"What is {rand1} + {rand2}?")
    randAns = rand1 + rand2
    userAns = int(input("Enter your Answer: "))
    if randAns == userAns:
        print("Correct")
        ad10 = score + 1
        return ad10
    elif userAns != randAns:
        print(f"Incorrect, The Correct Answer is {randAns}.")
        ad10 = score
        return ad10
def scoring():
    num1 = questions1()
    num2 = question2()
    num3 = question3()
    num4 = question4()
    num5 = question5()
    num6 = question6()
    num7 = question7()
    num8 = question8()
    num9 = question9()
    num10 = question10()
    scores = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10)
    return scores
totalscore = scoring()
print(f"\n{user}, \033[32;1mYour Total Score is\033[0m {totalscore}/10.")