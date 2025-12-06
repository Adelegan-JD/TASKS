# personal_details 
name = list(input('What is your full name?: '))
if name == '':
    print('Please input your full name')
age = int(input('How old are you?: '))
gender = input('Are you a male or a female?: ')
initials = (name[0][0], name[1][0])

# academic scores
subjects = ('Economics', 'Accounting', 'Commerce')
scores = tuple(
    float(input(f"What did you score in {subj}: "))
    for subj in subjects)
average_score = sum(scores) / len(scores)

#Guardian information
guardian_name = input('\nWhat is the name of your guardian?: ')
guardian_contact = input('What is your guardian\'s phone number?: ')

# Hobbies
hobbies = input('\nWhat are your hobbies? List the top three and separate them by comma: ')
hobby_items = [h.strip() for h in hobbies.split(',') if h.strip()]
hobbies_list = list(dict.fromkeys(hobby_items))  # preserves order, removes duplicates
hobbies = set(hobbies_list)

# Student Profile
profile = {'Personal Details': {
                        'Name': name,
                        'Age': age,
                        'Gender': gender,
                        'Initials': initials},

            'Academics': {subject: score for subject, score in zip(subjects, scores)
},
            'Guardian Details' : {'Name':guardian_name, 
                                    'Phone':guardian_contact},
            'Hobbies': {'Hobbies': hobbies_list,
                        'Number of Hobbies': len(hobbies_list)}}



# Output Section
print("\n==============================")
print("       STUDENT PROFILE")
print("==============================")

print(f"Name:\t\t{profile['Personal Details']['Name']}")
print(f"Age:\t\t{profile['Personal Details']['Age']}")
print(f"Gender:\t\t{profile['Personal Details']['Gender']}")
print(f"Initials:\t{profile['Personal Details']['Initials']}")
print("\n--- Academic Scores ---")
print(profile["Academics"])
for subject, score in profile['Academics'].items():
    if subject != 'Average Score':
        print(f'{subject}: {score}')
profile['Academics']['Average'] = average_score
print(f"Average Score:\t{profile['Academics']['Average']:.2f}")
print("\n--- Guardian Information ---")
print(profile["Guardian Details"])
print("\n--- Hobbies ---")
print(profile["Hobbies"])