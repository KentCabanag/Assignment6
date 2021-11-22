#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

print("\n\033[32;1mArranging Four Numbers From Highest to Lowest\033[0m\n")

num1 = "{:g}".format(float(input("\033[31;1mEnter your First Number\033[0m: ")))
num2 = "{:g}".format(float(input("\033[31;1mEnter your Second Number\033[0m: ")))
num3 = "{:g}".format(float(input("\033[31;1mEnter your Third Number\033[0m: ")))
num4 = "{:g}".format(float(input("\033[31;1mEnter your Fourth Number\033[0m: ")))

def Num_1():
    if num1 >= num2 >= num3 >= num4:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num1}, {num2}, {num3}, {num4}).")
    elif num1 >= num4 >= num2 >= num3:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num1}, {num4}, {num2}, {num3}).")
    elif num1 >= num3 >= num4 >= num2:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num1}, {num3}, {num4}, {num2}).")
    elif num1 >= num3 >= num2 >= num4:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num1}, {num3}, {num2}, {num4}).")
    elif num1 >= num4 >= num3 >= num2:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num1}, {num4}, {num3}, {num2}).")
    elif num1 >= num2 >= num4 >= num3:
        print(f"\033[34;4mHighest to Lowest\033[0m: ({num1}, {num2}, {num4}, {num3}).")

Num_1()