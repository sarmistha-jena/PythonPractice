#Write a program (function!) that takes a list and returns a new list that contains all the elements of 
# the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

def remove_duplicates_set(li):
    return list(set(li))

li=[7,5,5,5,2,1,1,2,3,4,4,4,1,1,3,6,6,6,6]
print("The original list is : {}".format(li))

print("Using loop and constructing a list : {}".format(remove_duplicates(li)))
print("Using sets : {}".format(remove_duplicates_set(li)))
