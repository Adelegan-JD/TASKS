# create a tuple for the weekdays
week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

#accept user input for the activities they would like to carry out
activities = (input('What would you like to do from Tuesday to Thursday? Please separate them by commas: ')).title().split()

# Join the activities with the specific days into dictionary using zip
activity_day = dict(zip(week_days[1:4], activities))

print(activity_day)





