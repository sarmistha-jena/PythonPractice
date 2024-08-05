# Write a function that takes an ordered list of numbers (a list where the elements are in order
#  from smallest to largest) and another number. The function decides whether or not the given number 
# is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

def search_number(list, num):
    if num in list:
        return True
    else:
        return False
    
def binary_search(list, num):
    l = len(list)
    if l == 0:
        return False
    else:
        mid = l//2
        if list[mid] == num:
            return True
        elif list[mid] < num:
            return binary_search(list[mid+1:], num)
        else:
            return binary_search(list[:mid], num)
import timeit        
    
if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num = int(input("Enter a number: "))
    print(binary_search(list, num))
    print(search_number(list, num))
    #get execution time for each function call.
    print(timeit.timeit(stmt="search_number(list, num)", setup="from __main__ import search_number, list, num", number=1000000))
    print(timeit.timeit(stmt="binary_search(list, num)", setup="from __main__ import binary_search, list, num", number=1000000))
    

