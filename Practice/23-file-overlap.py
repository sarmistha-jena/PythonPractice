# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of
#  happy numbers up to 1000.

file_prime = 'primenumbers.txt'
file_happy = 'happynumbers.txt'
num_both = []
with open(file_prime, 'r') as file:
    prime = [int(line.strip()) for line in file]

with open(file_happy, 'r') as file:
    happy = [int(line.strip()) for line in file]

for num in prime:
    if num in happy:
        num_both.append(num)

print(num_both)