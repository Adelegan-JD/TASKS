# collect personal_details 
try:
    name = list(input('What is your full name?: '))
except Exception as e:
    print("Error reading name:", e)
    name = []

try:
    age = int(input('How old are you?: '))
except Exception as e:
    print("Invalid age, defaulting to 0:", e)
    age = 0

try:
    gender = input('Are you a male or a female?: ')
except Exception as e:
    print("Error reading gender:", e)
    gender = "Not specified"

try:
    initials = (name[0][0], name[1][0])
except Exception as e:
    print("Could not extract initials:", e)
    initials = ("", "")

# academic scores
subjects = ('Economics', 'Accounting', 'Commerce')
scores = ()

for i in range(len(subjects)):
    try:
        score = float(input(f'What did you score in {i}?: '))
        scores += (score,)
    except Exception as e:
        print("Invalid score, defaulting to 0:", e)
        scores += (0.0,)

try:
    average_score = sum(scores) / len(scores)
except Exception as e:
    print("Could not compute average score:", e)
    average_score = 0.0

#Guardian information
try:
    guardian_name = input('What is the name of your guardian?: ')
except:
    guardian_name = "Unknown"

try:
    guardian_contact = input('What is your guardian\'s phone number?: ')
except:
    guardian_contact = "Unknown"

# Hobbies
try:
    hobbies = set(input('What are your hobbies? List the top three and separate them by comma: ').split(','))
except Exception as e:
    print("Error reading hobbies:", e)
    hobbies = set()

hobbies_list = list(hobbies)

# Student Profile
try:
    profile = {
        'Personal Details': {
            'Name': name,
            'Age': age,
            'Gender': gender,
            'Initials': initials
        },
        'Academics': {i: score for i, score in zip(subjects, scores)},
        'Guardian\'s Details ': {
            'Name': guardian_name,
            'Phone': guardian_contact
        },
        'Hobbies': {
            'Hobbies': hobbies_list,
            'Number of Hobbies': len(hobbies_list)
        }
    }
    profile['Academics']['Average'] = average_score
except Exception as e:
    print("Error building profile:", e)
    profile = {}

# Output Section
try:
    print("\n\t=== STUDENT PROFILE ===")
    print(f"Name:\t\t{profile['Personal Details']['Name']}")
    print(f"Age:\t\t{profile['Personal Details']['Age']}")
    print(f"Gender:\t\t{profile['Personal Details']['Gender']}")
    print(f"Initials:\t{profile['Personal Details']['Initials']}")

    print("\n--- Academic Scores ---")
    print(profile["Academics"])
    print(f"Average Score:\t{profile['Academics']['Average']:.2f}")

    print("\n--- Guardian Information ---")
    print(profile["Guardian's Details "])

    print("\n--- Hobbies ---")
    print(profile["Hobbies"])
except Exception as e:
    print("Error displaying profile:", e)
