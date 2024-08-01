#Randomly generate two lists 
#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#  Make sure your program works on two lists of different sizes

import random

list1size=input("Please enter the size of the first list: ")
list2size=input("Please enter the size of the second list: ")
list1=set(random.sample(range(1,50), int(list1size)))
list2=set(random.sample(range(1, 50), int(list2size)))
if list1size < list2size:
    common = [i for i in list1 if i in list2]
else:
    common = [i for i in list2 if i in list1]
print("First list is {}".format(list1))
print("Second list is {}".format(list2))
print("Common elements are {}".format(set(common)))
