store = {'Bottle': 15, 'Kettle': 10, 'Jug': 35, 'Plate': 5}
items = input("What item do you want to buy?: ").title()
amount = int(input("How many would you like to purchase?: "))
if items in store.keys():
    if store[items] >= amount:
        print(f'Before purchase : {store}')
        store[items] -=amount
        print(f'After purchase : {store}\nThanks for your patronage!')
    else:
        print('Sorry!', 'we do not have that amount of', items, 'currently, but we\'re restocking soon. Please check again another time.')
else:
    print('Sorry!', items, 'is currently not available in our store. Please check again another time.')
