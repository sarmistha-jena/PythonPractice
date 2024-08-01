# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence 
# is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci(num):
    fibonacci = [0, 1]
    for i in range(2, num):
        next_num = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_num)
    return fibonacci


num = int(input("How many Fibonacci numbers do you want to generate? "))
print(fibonacci(num))
