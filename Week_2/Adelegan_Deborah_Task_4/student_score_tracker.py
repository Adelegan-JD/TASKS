name_list = []
score_list = []

# Collect student names
name1 = input("Kindly enter the name of the first student: ")
name2 = input("Kindly enter the name of the second student: ")
name3 = input("Kindly enter the name of the third student: ")

# Collect student scores
score1 = int(input("What is the score of the first student?"))
score2 = int(input("What is the score of the second student?"))
score3 = int(input("What is the score of the third student?"))

# Append student names
name_list.append(name1)
name_list.append(name2)
name_list.append(name3)

# Append student scores
score_list.append(score1)
score_list.append(score1)
score_list.append(score1)

# Print formatted output
print(f"Name\tScore\n{name_list[0]}\t{score_list[0]}\n{name_list[1]}\t{score_list[1]}\n{name_list[2]}\t{score_list[2]}")









































