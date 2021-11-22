#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

print("\n\033[32;1mArranging Four Numbers From Highest to Lowest\033[0m\n")

num1 = (float(input("\033[31;1mEnter your First Number\033[0m: ")))
num2 = (float(input("\033[31;1mEnter your Second Number\033[0m: ")))
num3 = (float(input("\033[31;1mEnter your Third Number\033[0m: ")))
num4 = (float(input("\033[31;1mEnter your Fourth Number\033[0m: ")))
num_1 = "{:g}".format(num1)
num_2 = "{:g}".format(num2)
num_3 = "{:g}".format(num3)
num_4 = "{:g}".format(num4)
def Num_1():
    if num1 >= num2 >= num3 >= num4:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_1}, {num_2}, {num_3}, {num_4})")
    elif num1 >= num4 >= num2 >= num3:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_1}, {num_4}, {num_2}, {num_3})")
    elif num1 >= num3 >= num4 >= num2:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_1}, {num_3}, {num_4}, {num_2})")
    elif num1 >= num3 >= num2 >= num4:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_1}, {num_3}, {num_2}, {num_4})")
    elif num1 >= num4 >= num3 >= num2:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_1}, {num_4}, {num_3}, {num_2})")
    elif num1 >= num2 >= num4 >= num3:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_1}, {num_2}, {num_4}, {num_3})")
def Num_2():
    if num2 >= num4 >= num3 >= num1:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_2}, {num_4}, {num_3}, {num_1})")
    elif num2 >= num4 >= num1 >= num3:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_2}, {num_4}, {num_1}, {num_3})")
    elif num2 >= num3 >= num4 >= num1:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_2}, {num_3}, {num_4}, {num_1})")
    elif num2 >= num3 >= num1 >= num4:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_2}, {num_3}, {num_1}, {num_4})")
    elif num2 >= num1 >= num4 >= num3:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_2}, {num_1}, {num_4}, {num_3})")
    elif num2 >= num1 >= num3 >= num4:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_2}, {num_1}, {num_3}, {num_4})")
def Num_3():
    if num3 >= num4 >= num2 >= num1:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_3}, {num_4}, {num_2}, {num_1})")
    elif num3 >= num4 >= num1 >= num2:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_3}, {num_4}, {num_1}, {num_2})")
    elif num3 >= num2 >= num4 >= num1:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_3}, {num_2}, {num_4}, {num_1})")
    elif num3 >= num2 >= num1 >= num4:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_3}, {num_2}, {num_1}, {num_4})")
    elif num3 >= num1 >= num2 >= num4:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_3}, {num_1}, {num_2}, {num_4})")
    elif num3 >= num1 >= num4 >= num2:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_3}, {num_1}, {num_4}, {num_2})")
def Num_4():
    if num4 >= num3 >= num2 >= num1:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_4}, {num_3}, {num_2} {num_1})")
    elif num4 >= num3 >= num1 >= num2:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_4}, {num_3}, {num_1}, {num_2})")
    elif num4 >= num2 >= num3 >= num1:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_4}, {num_2}, {num_3}, {num_1})")
    elif num4 >= num2 >= num1 >= num3:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_4}, {num_2}, {num_1}, {num_3})")
    elif num4 >= num1 >= num2 >= num3:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_4}, {num_1}, {num_2}, {num_3})")
    elif num4 >= num1 >= num3 >= num2:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num_4}, {num_1}, {num_3}, {num_2})")

Num_1()
Num_2()
Num_3()
Num_4()