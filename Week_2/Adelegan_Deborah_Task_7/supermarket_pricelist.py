# Create an empty dictionary
pricelist = {}

# create items list and an empty list for prices
items = ['Milk', 'Cheese', 'Oats', 'Butter', 'Mayonnaise']
prices= []
for i in items:
    amount = input(f'Please enter the price of {i}: ')
    prices.append(amount)

#put both lists inside the dictionary
pricelist = dict(zip(items, prices))

# print each item and corresponding price in the dictionary
for key, value in pricelist.items():
    print(f'{key}:{value}')
  
# update the dictionary
pricelist.update({'Yoghurt': 900})  
print('Updated Dictionary\n')
for key, value in pricelist.items():
    print(f'{key}:{value}')

