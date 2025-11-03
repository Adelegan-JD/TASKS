ticket_number = set(range(1, 51))
user_number  = int(input("Welcome to the First season of the football match.\nKindly book a seat number to watch the match. \nSelect any number between 1 and 50: "))
if user_number not in ticket_number:
    print("Sorry, the seat number you selected is not available. Please choose a number between 1 and 50.")
else:
    remaining_ticket = ticket_number.remove(user_number)
    print(f"You have selected number {user_number}. \nThe remaining ticket numbers available are \n{ticket_number}")
