# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order

line = input("Enter a string: ")
def reverse_line(line):
    words = line.split()
    reverse_words = words[::-1]
    return " ".join(reverse_words)

print(reverse_line(line))