'''The code below is confirming the eligibility of applicants applying for a Federal Government Scholarship.
    The basic details of the applicant (name, age, and score) are first collected
    The first round of eligibility criteria involves age and score. If the applicant is less than 18 years AND also scored above 70%, then such applicant is eligible. If either criterion is met but the other is not, then the applicant is rendered ineligible.
'''



# name = input("Enter your name: ")       # This accepts the name of the candidate
# age = int(input("Enter your age: "))        # This accepts the age of the candidate
# score = int(input("Enter your test score: "))       # This accepts the test score of the candidate

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")



# Adapting it to a fuller concept
name = input("Enter your name: ")       # This accepts the name of the candidate
age = int(input("Enter your age: "))        # This accepts the age of the candidate
score = int(input("Enter your test score: "))       # This accepts the test score of the candidate
citizenship = input("What country are you from?: ")
studentship = input("Are you a full-time undergraduate studying in a recognised Nigerian university? ")
enrollment = input("What is the name of your school?")
other_scholarships = input("Are you currently receiving any other scholarship benefits from an entity in the Oil and Gas industry?: ")
academics = ''

eligibility = (age > 18) and (score > 70) and (citizenship == 'Nigeria') and (studentship == 'Yes') and (other_scholarships == 'No')
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
























































