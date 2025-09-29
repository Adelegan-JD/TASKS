# Collect personal details (name, age, gender and courses)
name = input("What is your full name?: ").title()
age = int(input("How old are you?: "))
gender = input("Are you a male or a female?: ").title()
courses = list(input("Please enter the courses you're currently taking (Separate them by commas, e.g. English, Mathematics): ").title().split(','))

# Storing it in a dictionary
biodata = {'Name': name,
           'Age': age,
           'Gender': gender,
           'Courses': courses}

# Printing the output
print(f"\n********************STUDENT PROFILE********************\nName: \t\t{biodata['Name']}\nAge: \t\t{biodata['Age']}\nGender: \t{biodata['Gender']}\nCourses: \t{biodata['Courses']}")


