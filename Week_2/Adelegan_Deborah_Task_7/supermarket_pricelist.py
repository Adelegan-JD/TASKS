
# Create an empty dictionary
pricelist = {}
# Collect the items to be bought in a list
item = ['Cheese', 'Milk', 'Butter', 'Bread', 'Cereals']

# Collect the price of the items in the list from the user
price = list(input("Please enter the price of each item and separate them by commas: "))

pricelist =  dict(zip(item, price))

for i, j in enumerate(pricelist.items()):
    print(f'{i : {j}}')