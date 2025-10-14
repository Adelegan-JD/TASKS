# - Store three names and their phone numbers in two separate tuples.
contact_names = ['Ade', 'Bola', 'Dayo']
contacts = tuple(contact_names)
phone_numbers = ('+2349042345672', '+2347082345632', '+2348054222707')

# Use zip() and dict() to combine tuples.
contact_dict = dict(zip(contacts, phone_numbers))

# Ask the user for a name and display the corresponding number (or an error message).
user_input = input('Whose name would you like to lookup?: ').title()

# Use .get() for safe retrieval.
if user_input in contact_dict:
    print(f'Great! {user_input}\'s phone number is {contact_dict.get(user_input)}. Thank you!')
else:
    print(('Oops I think you entered the wrong name, please try again. Thank you!'))





