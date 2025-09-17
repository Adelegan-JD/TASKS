student = {}
name  = input("Kindly input your name :")
age = int(input("Kindly enter your age: "))
student.update({"Name": {name}})
student.update({"Age": {age}})
student["Scores"]=[40, 30, 50, 60, 75, 90]
print(student)
ave_score = sum(student["Scores"])/len(student["Scores"])
student["passed"] = ave_score >= 50
teenager = age >= 13 and age <= 19
print(f"Student Record: \nName: {name}\nAge: {age}\nPassed: {student["passed"]}\nTeenager: {teenager}")















































