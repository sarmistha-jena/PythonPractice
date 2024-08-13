#Create a dictionary (in your file) of names and birthdays. When you run your program 
# it should ask the user to enter a name, and return the birthday of that person back to them. 

birthday_dict={
    "Sarmistha": "1989/10/12",
    "Jena": "1995/05/15",
    "Madhav": "1986/10/14",
    "Mukti": "2018/01/08"
}

def get_birthday(name):
    if name in birthday_dict:
        return birthday_dict[name]
    else:
        return "Name not found in the dictionary."
    
def print_birthday():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in birthday_dict:
        print(name)
    name=input("Who's birthday do you want to look up? \n")
    print(f"The birthday of {name} is {get_birthday(name)}")

if __name__=="__main__":
    print_birthday()
