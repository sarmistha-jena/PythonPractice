# Write a password generator in Python. Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

def password_generator(length=10):
    import random
    import string
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    # print(characters)
    password = ''.join(random.choice(characters) for i in range(length))
    return password

weak = ['123', 'password', 'qwerty', 'abc']

# password_gen=input("Do you want a strong or weak password? (strong/weak) ")
# if password_gen == 'weak':
#     import random
#     print(random.choice(weak))
# else:
#     paswd = password_generator()
#     print(paswd)
#     print("Password generated successfully")

    
#Include your run-time code in a main method.
if __name__ == "__main__":
    print("Heyyyyyyyyyy I am in main....")
    print(password_generator(12))