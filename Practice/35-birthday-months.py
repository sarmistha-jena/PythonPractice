#Load that JSON file from disk, extract the months of all the birthdays, 
# and count how many scientists have a birthday in each month.

#Your program should output something like:

# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

def load_json(file_path):
    import json
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def convert_month(month_number):
    import calendar
    return calendar.month_name[int(month_number)]

def get_no_of_birthday_per_month(birthdays):
    month_user = {}
    for birthday in birthdays.values():
        month = birthday.split('/')[1]
        month_name = convert_month(month)
        if month_name in month_user:
            month_user[month_name] += 1
        else:
            month_user[month_name] = 1
    return month_user

import datetime

if __name__ == '__main__':
    birthdays = load_json('birthdays.json')
    month_user = get_no_of_birthday_per_month(birthdays)
    print(month_user)
    # print(datetime.date.today().year)
    # print(datetime.date.today().day)
    # print(datetime.date.today().month)