import datetime 

name=input("Please enter your name ")
age=int(input("Please enter your age "))
print("****************************************")
print("Hello {}, your age is {}".format(name,age))
#Calculate the year when the user will be 100 years old
yearstoage100=100-age
currentyear=datetime.datetime.now().year
yearof100=currentyear+yearstoage100

print("{} will be 100 years old in the year {}".format(name,yearof100))