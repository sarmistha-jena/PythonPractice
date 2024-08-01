# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.).
#  You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)  + 1):
        if num % i == 0:
            return True
        
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a not prime number.")
else:
    print(f"{num} is a prime number.")