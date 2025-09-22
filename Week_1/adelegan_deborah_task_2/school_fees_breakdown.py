school_name = input("What is the name of your school?: ")
capital_school_name = school_name.upper()
tuition_fee =  float(input("How much is your school fees?: "))
hostel_fee = float(input("How much is your hostel rent?: "))
feeding_fee = float(input("How much do you spend on feeding per month?: "))
total_fee = tuition_fee + hostel_fee + feeding_fee
print(f"\t\tSCHOOL FEES BREAKDOWN FOR {capital_school_name}\n Tuition Fee: \t{tuition_fee}\n Hostel Fee: \t{hostel_fee}\n Feeding Fee: \t{feeding_fee}\n\nYour total bill is {total_fee} million naira only.")
