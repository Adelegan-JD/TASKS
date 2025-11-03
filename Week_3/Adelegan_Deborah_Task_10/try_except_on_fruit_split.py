fruits = input("Kindly enter five fruits of your choice: ")
try:
    if fruits.count(',') < 4:
        raise ValueError("Sorry! Insufficient number of fruits provided.")
    split_fruits = fruits.split()
    fruits_list = set(split_fruits)
    print(fruits_list)
except ValueError as ve:
    print(ve)
    