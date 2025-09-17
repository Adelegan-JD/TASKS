user_age = int(input("What is your age please?: "))   # This collects the name of the user
user_height = float(input("How tall are you in inches please?: "))   # This collects the height of the user
user_name = input("What is your name please?: ")    # This collects the name of the user
print(f"Your name is {user_name}. You are {user_age} years old and {user_height} inches tall.")   # This prints out the different variables, all as a single sentence

eligible_age = user_age <= 18 and user_age > 35
eligible_height = user_height > 7 and user_height < 10

if user_age == eligible_age:
    print("You are eligible for the next cohort of this program")







