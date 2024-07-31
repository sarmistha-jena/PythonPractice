# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

string = input("Enter a string: ")

def reverse(string):
    return string[::-1]

if string == reverse(string):
    print("The string {} is a palindrome".format(string))