# personal_details 
name = list(input('What is your full name?: '))
age = int(input('How old are you?: '))
gender = input('Are you a male or a female?: ')
initials = (name[0][0], name[1][0])

# academic scores
subjects = ('Economics', 'Accounting', 'Commerce')
for i in range(len(subjects)):
    scores = tuple(float(input(f'What did you score in {i}?: ')))
average_score = sum(scores) / len(scores)

#Guardian information
guardian_name = input('What is the name of your guardian?: ')
guardian_contact = input('What is your guardian\'s phone number?: ')

# Hobbies
hobbies = set(input('What are your hobbies? List the top three and separate them by comma: ').split(','))
hobbies_list = list(hobbies)

# Student Profile
profile = {'Personal Details': {
                        'Name': name,
                        'Age': age,
                        'Gender': gender,
                        'Initials': initials},

            'Academics': {i: score for i, score in zip(subjects, scores)},
            'Guardian\'s Details ' : {'Name':guardian_name, 
                                      'Phone':guardian_contact},
            'Hobbies': {'Hobbies': hobbies_list,
                        'Number of Hobbies': len(hobbies_list)}}


# Output Section
print("\n\t=== STUDENT PROFILE ===")
print(f"Name:\t\t{profile['Personal Details']['Name']}")
print(f"Age:\t\t{profile['Personal Details']['Age']}")
print(f"Gender:\t\t{profile['Personal Details']['Gender']}")
print(f"Initials:\t{profile['Personal Details']['Initials']}")
print("\n--- Academic Scores ---")
print(profile["Academics"])
print(f"Average Score:\t{profile['Academics']['Average']:.2f}")
print("\n--- Guardian Information ---")
print(profile["Guardian's Details"])
print("\n--- Hobbies ---")
print(profile["Hobbies"])
