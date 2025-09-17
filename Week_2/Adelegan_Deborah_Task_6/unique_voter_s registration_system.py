# TASK 4: Create a unique Voter's Registration System


# # Create an empty set
voters_list = set()

# Accept first voter's name
voter1 = input("Kindly input your name for the registration: ")
voters_list.add(voter1)

# Accept second voter's name and ensure it's not the same as the first
voter2 = input("Kindly input your name for the registration: ")
if voter2 == voter1:
    print(f"Warning: {voter2} is in the registration file. You have previously registered.")
else:voters_list.add(voter2)

# Accept third voter's name and ensure it's not the same as the second
voter3 = input("Kindly input your name for the registration: ")
if voter3 == voter2 and voter3 == voter1:
    print(f"Warning: {voter3} is in the registration file. You have previously registered.")
else:voters_list.add(voter3)

# Accept fourth voter's name and ensure it's not the same as the first, second and third
voter4 = input("Kindly input your name for the registration: ")
if voter4 == voter1 and voter4 ==2 and voter1 == voter3:
    print(f"Warning: {voter4} is in the registration file. You have previously registered.")
else:voters_list.add(voter4)

print(f"The number of the registered voters is: {len(voters_list)}")


















