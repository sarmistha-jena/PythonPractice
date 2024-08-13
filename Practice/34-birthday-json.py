# Load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.
#Ask the user for another scientist’s name and birthday to add to the dictionary, 
# and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times
#  and keep adding new names, your JSON file should keep getting bigger and bigger.

def load_birthday_dict():
    import json
    with open("birthdays.json", "r") as f:
        birthday_dict = json.load(f)
    return birthday_dict

def write_birthday_dict(birthday_dict):
    import json
    with open("birthdays.json", "w") as f:
        json.dump(birthday_dict, f, indent=4)

def add_birthday():
    birthday_dict = load_birthday_dict()
    name = input("Enter the name of the person: ")
    birthday = input("Enter the birthday (YYYY-MM-DD): ")
    birthday_dict[name] = birthday
    write_birthday_dict(birthday_dict)
    print(f"{name}'s birthday has been added to the dictionary.")

def display_birthday():
    birthday_dict = load_birthday_dict()
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in birthday_dict:
        print(name)
    name = input("Enter the name of the person: ")
    if name in birthday_dict:
        print(f"{name}'s birthday is {birthday_dict[name]}.")
    else:
        print(f"{name} is not found in the dictionary.")

if __name__ == "__main__":
    while True:
        print("1. Add a birthday\n2. Display a birthday\n3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            add_birthday()
        elif choice == "2":
            display_birthday()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")