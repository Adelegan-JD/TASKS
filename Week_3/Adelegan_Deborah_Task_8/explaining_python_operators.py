# TASK 1
# Explain each output of the program below
# Give 3 use cases or scenarios where you can apply he program below
# Write the code for one of the three use cases

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")
# Output: 45 == 78 : False. The "==" sign is known as the equal to sign. This output means that the first number is not the same as the second number. If the first number is the same as the second number, the output will be True

print(f"{num1} != {num2} : {num1 != num2}")
# Output: True
# The "!=" sign means "Not Equal To". Thus, whhen it is used between two variables or numbers, it will generate a True statement if the numbers are not equal and a False statement if the numbers are equal

print(f"{num1} > {num2} : {num1 > num2}")
# Output: 8 > 7 : True
# This code is meant to generate a True statement if num1 is greater than num2, and a False  statement if num1 is not greater than num2

print(f"{num1} < {num2} : {num1< num2}")
# The output of this code will generate a True statement if the first number is less than the second number and a False statement if the first numbere is not less than the second number

# Three scenarios where this can be used:
# 1. Incrementing or decrementing value prices of goods
# 2. Getting percentage interest of payments made over time
# 3. Adding to the population of students in a class

# 2. Getting percentage interest of payments made over time
price = 20
price *= 1.1        # This is to increase the amount by 10%
print(price)































