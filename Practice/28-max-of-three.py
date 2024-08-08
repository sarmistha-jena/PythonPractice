# Implement a function that takes as input three variables, and returns the largest of the three. 
# Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us. 
# All you need is some variables and if statements!

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
    print(f"The largest number is {largest}.")
elif num2 >= num1 and num2 >= num3:
    largest = num2
    print(f"The largest number is {largest}.")
else:
    largest = num3
    print(f"The largest number is {largest}.")  
    