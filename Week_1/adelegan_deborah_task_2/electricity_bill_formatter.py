name = input("Dear Customer, please write your full name here: ")   # This accepts the name of the user
unit_consumed = int(input("Kindly enter how many units you bought: "))  # This accepts the number of units the customer bought
cost_per_unit = float(input("How much did you purchase one unit?: "))   # This shows the amount one unit costs
total_bill = float(unit_consumed * cost_per_unit)   # This multiplies the cost of each unit by the total units purchased
print("Dear Mr. " + name + " . Here is your electricity bill receipt")   # This concatenates the name of the customer and introduces the utility bill receipt
print(f"\t\t\tUTILITY BILL RECEIPT\nName:\t\t      {name}\n\nUnits Purchased:      {unit_consumed} kW/hr\n\nYour total bill is:   {total_bill} Naira")