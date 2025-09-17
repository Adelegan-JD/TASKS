# TASK 3: Tuple Operations

# Accept user's states
state_name = (input("Enter any five states that you know. Please separate them by commas: ").title())

# Split the list to have each item as a standalone
split_state = state_name.split(",")

# Store the split list into a tuple
tuple_state = tuple(split_state)

# Print the first and last states
print(tuple_state[0::4])

# Confirm if "Lagos" is in the states 
print("lagos" in split_state)

# Print the number of states entered
print(len(tuple_state))
















































































