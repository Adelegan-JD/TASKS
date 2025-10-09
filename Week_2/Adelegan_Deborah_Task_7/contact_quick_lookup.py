# **Task5: Contact Quick Lookup**
# - Store three names and their phone numbers in two separate tuples.

#   - Create a dictionary from them using `dict(zip(...))`.

#   - Ask the user for a name and display the corresponding number (or an error message).

# - Requirements:

#   - Use `zip()` and d`ict()` to combine tuples.

#   - Use `.get()` for safe retrieval.

#   - No loops.





contact_names = ('Ade', 'Bola', 'Dayo')
phone_numbers = ('+2349042345672', '+2347082345632', '+2348054222707')

contact_dict = dict(zip(contact_names, phone_numbers))

user_input = input('Whose name would you like to lookup?: ')
if user_input in contact_dict:
    print(f'Great! {user_input}\'s phone number is {contact_dict.get(user_input)}. Thank you!')
else:
    print(('Oops I think you entered the wrong name, please try again. Thank you!'))





