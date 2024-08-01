#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

def get_random_list(size):
    import random
    random_list = []
    for i in range(size):
        random_list.append(random.randint(1, 100))
    return random_list

#a = [5, 10, 15, 20, 25]
num = int(input("Enter the size of the list: "))
a = get_random_list(num)

print(a)
print(a[0])
print(a[-1])

new_list = [a[0], a[-1]]
print(new_list)