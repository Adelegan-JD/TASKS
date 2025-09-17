
# TASK 3: Simulate a football match ticket
# Step 1: Store the seat numbers 1- 50 in a set using the range
# Step 2: Ask users to book a seat by selecting any number between 1 and 50
# Step 3: Use the remove method to remove the selected number
# Step 4: Print the remaining numbers

ticket_number = set(range(1, 51))
user_number  = int(input("Welcome to the First season of the football match.\nKindly book a seat number to watch the match. \nSelect any number between 1 and 50: "))
remaining_ticket = ticket_number.remove(user_number)
print(f"You have selected number {user_number}. \nThe remaining ticket numbers available are \n{ticket_number}")
