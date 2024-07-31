# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common
#  between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,77,44,88,55]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,55]

c = []

a_set = set(a)
b_set = set(b)
c_set = a_set.intersection(b_set)

#c = list(c_set)
if len(a)<len(b):
    c = set(list(i for i in a if i in b))
else:
    c = set(list(i for i in b if i in a))
print(c)

#Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
import random

x=random.sample(range(1,30), 12)
y=random.sample(range(1, 40), 16)
common = [i for i in x if i in y]
print("First list is {}".format(x))
print("Second list is {}".format(y))
print("Common elements are {}".format(set(common)))