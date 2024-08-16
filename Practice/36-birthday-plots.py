#use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! 
# Because it would take a long time for you to input the months of various scientists

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

def draw_histogram(month_user):
    from bokeh.plotting import figure, show, output_file
    import math
    output_file("plot.html")

    categories = list(month_user.values())
    p = figure(x_range=categories, title="Scientists' Birthday Months")
    p.xaxis.major_label_orientation = math.pi/4
    p.vbar(x=month_user.keys(), top=month_user.values())

    show(p)


if __name__ == '__main__':
    birthdays = load_json('birthdays.json')
    month_user = get_no_of_birthday_per_month(birthdays)
    draw_histogram(month_user)