# TASK 1: Fruit Collector


# Solution
# Step 1: Ask the user to input five choice fruits
# Step 2: Split the fruits
# Step 3: Store the spit fruits into a set

fruits = input("Kindly enter five fruits of your choice: ")
split_fruits = fruits.split()
fruits_list = set(split_fruits)
print(fruits_list)