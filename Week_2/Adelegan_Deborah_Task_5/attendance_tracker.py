# Save each day of the week in a tuple
week_days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')


# Save each month of the year in another tuple
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# Collect user's personal details
name = input("What is your name, please?: ").title()
gender = input("Are you a male or a female?: ").title()
course_track = input("What track are you? (AI Engineering or AI Development)").title()
current_month = int(input("What month are you currently? Please pick from 1 to 12: "))
current_day = int(input("What day are you currently? Please choose between 1 to 7: "))

# Save the month number into a variable
month_number = current_month - 1

# Save the week number into a variable
day_number = current_day - 1

# Print the attendance tracker
print(f"Hello, {name}!\nYou are a {gender}\nYou are in the {course_track} track\nYou are in the month of {months[month_number]} and today is {week_days[day_number]}")



















































