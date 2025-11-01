# subject_scores = {'Mathematics': 60, 'English':60, 'Physics': 60, 'Chemistry':60, 'Biology':60}
# academic_eligibility = input('What is your score in maths')
# if academic_eligibility < subject_scores:
#     print('Sorry! You are not eligible')
# citizenship_eligibility = 'Nigeria'
# enrollment_eligibility = 'Yes'
# other_scholarships_eligibility = 'No'
# subjects = 
# subject_scores = {'Mathematics': 60, 'English':60, 'Physics': 60, 'Chemistry':60, 'Biology':60}
# academic_eligibility = 
# if subject_scores["Mathematics"] < 60:
#     print('Sorry! You are not eligible')
#collect name
name = input('What is your name?: ')

# collect citizenship status
citizenship = input('What country are you from?: ')

# collect name of university
enrollment = input('What is the name of your university?: ')

# collect student undergraduate level
level = input('What is your current level of study (e.g. 100, 200, 300, 400)?: ')

# collect information about other scholarships
other_scholarships = input("Are you currently receiving any other scholarship benefits from an entity in the Oil and Gas industry?: ")

# Collect scores for relevant subjects
courses = ['English', 'Mathematics', 'Physics', 'Geography', 'Biology']
scores = {}
for course in courses:
    score = int(input(f'What is your score in {course}?: '))
    scores[course] = score

# list of universities
university = ['	Babcock University', 'Igbinedion University', 'Madonna University', 'Bowen University', 'Covenant University', 'Afe Babalola University', 'Bells University of Technology', 'Ajayi Crowther University', 'Redeemer\'s University', 'Pan-Atlantic University', 'Lead City University', 'Nile University of Nigeria', 'American University of Nigeria', 'Veritas University', 'Caritas University', 'Chrisland University', 'Oduduwa University', 'Obong University', 'Wellspring University', 'Renaissance University', 'Novena University', 'Summit University', 'Micheal and Cecilia Ibru University', 'Clifford University', 'Joseph Ayo Babalola University', 'Kings University', 'Southwestern University', 'Temple University, Nigeria Campus', 'University of Mkar', 'Evangel University', 'Al-Qalam University', 'Federal University of Petroleum Resources Effurun', 'Nigerian Turkish Nile University', 'African University of Science and Technology', 'National Open University of Nigeria', 'Federal University of Technology Owerri', 'Federal University of Technology Akure', 'Federal University of Technology Minna', 'Federal University of Technology Yola', 'Federal University of Technology Lafia', 'Federal University of Technology Birnin Kebbi', 'Federal University of Technology Wukari', 'Federal University of Technology Dutse', 'Federal University of Technology Gusau', 'Federal University of Technology Akure', 'Al-Qalam University', 'Bingham University, New Karu', 'Caleb University, Lagos', 'Crawford University, Igbesa', 'Dominican University, Ibadan', 'Rhema University, Aba', 'Tansian University, Umunya', 'Wesley University of Science and Technology, Ondo', 'Western Delta University, Oghara', 'Lead City University, Ibadan', 'Achievers University, Owo', 'Admiralty University of Nigeria, Ibusa', 'All Nations University, Koforidua', 'Atlantic University, Uyo', 'Babcock University, Ilishan-Remo', 'Bells University of Technology, Ota', 'Benson Idahosa University, Benin City', 'Chrisland University, Abeokuta', 'Clifford University, Owerrinta', 'Covenant University, Ota', 'Dominican University, Ibadan', 'Evangel University, Akaeze', 'Federal University Oye-Ekiti', 'Godfrey Okoye University, Enugu', 'Igbinedion University, Okada', 'Joseph Ayo Babalola University, Ikeji-Arakeji', 'Kings University, Ode-Omu', 'Madonna University, Elele', 'Micheal and Cecilia Ibru University, Agbarha-Otor', 'Nile University of Nigeria, Abuja', 'Novena University, Ogume', 'Obong University, Obong Ntak', 'Pan-Atlantic University, Lagos', 'Redeemer\'s University, Ede', 'Renaissance University, Enugu', 'Summit University, Offa', 'Temple University Nigeria Campus, Abuja', 'Veritas University, Abuja', 'Wellspring University, Evbuobanosa']

# List of ubdergraduate levels
undergraduate_level = [100, 200, 300, 400, 500, 600]

# Eligibility requirements
if (score >= 60 for score in scores.values())  and (citizenship == 'Nigeria') and (enrollment in university) and (level in undergraduate_level) and (other_scholarships == 'No'):
        print(f'Congratulations {name}! You are eligible for the scholarship.')
else:
    print(f'Sorry {name}, you are not eligible to apply for this scholarship.')
