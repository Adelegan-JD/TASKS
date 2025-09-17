# Collect personal details (name, age, gender)
name = input("What is your full name?: ").title().split()
student_name = list(name)
age = int(input("How old are you?: "))
gender = input("Are you a male or a female?: ").title()
initial1 = student_name[1]

# Collect academic scores for a fixed set of subjects
subjects = ("Maths", 'English', 'Science')
scores = tuple(float(input(f"What is your score for {subject}?: ")) for subject in subjects)
average_score = sum(scores) / len(scores)

# Collect guardian's details
guardian_name = input("What is the name of your guardian?: ").title()
guardian_number = input("What is your guardian's phone number?: ")

# Collect hobbies without duplicates
hobbies_list = input("What are your hobbies? Enter at least three of them: ").title()
hobbies = set(hobby.strip() for hobby in hobbies_list.split(','))

student_biodata = {
    "Personal Details": {
        "Name" : name,
        "Age " : age,
        "Gender": gender
    },
    "Academics": {subject: score for  subject, score in zip(subjects, scores)},
    "Guardian Information": {
        "Guardian's Name": guardian_name,
        "Guardian's Phone Number": guardian_number
    },
    "Hobbies": list(hobbies)

}

print(initial1)














