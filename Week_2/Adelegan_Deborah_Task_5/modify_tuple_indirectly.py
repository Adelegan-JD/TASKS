# Ask the user for three items they want to buy
items = input("Kindly enter three items you want to buy. Please separate them by commas: ").split(',')

# Store the items in a tuple
shopping_list = tuple(items)

# Convert it to a list
list_items = list(shopping_list)

# Ask for two more items
list_items.append(input("Please add one more item to your cart: "))
list_items.append(input("Please add one more item to your cart: "))


# Convert back to a tuple
new_list = tuple(list_items)

# Print updated list using join to display the items separated by "|"
print(" |" .join(new_list))