#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# If you don’t know what a divisor is, it is a number that divides evenly into another number.

num=int(input("Please enter a number : "))
divisors=[num]
halfofnum=int(num/2)+1
for i in range(1,halfofnum):
    if num%i==0:
        divisors.append(i)
divisors.sort()
print("List of divisors for {} are {}".format(num,divisors))

if len(divisors)>2:
    print("Number {} is not prime".format(num))
else:
    print("Number {} is prime".format(num)) 