# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
# and print out the results to the screen. I have a .txt file for you, if you want to use it!

file_name='namelist.txt'
with open(file_name, 'r') as file:
    content = file.read()

name_count = {}

for name in content.split():
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

print(name_count)

for name, count in name_count.items():
    print("{} appears for: {} number of times".format(name, count))

#count how many of each “category” of each image there are. 
# This text file is actually a list of files corresponding to the SUN database scene recognition database, 
# and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, 
# it will be clear which part represents the scene category. 

file_name2='sun_catagory.txt'

with open(file_name2, 'r') as file:
    content2 = file.readlines() 

#/a/abbey/sun_aqswjsnjlrfzzhiz.jpg regular expression to get abbey

catagory_count = {}
for line in content2:
    catagory = line.split('/')[-2]
    if catagory in catagory_count:
        catagory_count[catagory] += 1
    else:
        catagory_count[catagory] = 1


for name, count in catagory_count.items():
    print("{} appears for: {} number of times".format(name, count))