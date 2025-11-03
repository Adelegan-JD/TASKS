print("Welcome to USSD Service!")
service_1 = "check account balance"
service_2= "check data balance"
service_3= "Confirm phone number"
service_4 = "Speak with agent"
service_5 = "Confirm your service provider"
service_6 = "Exit"
print(f"1. {service_1}\n2. {service_2}\n3. {service_3}\n4. {service_4}\n5. {service_5}\n6. {service_6}")
service = int(input("Please select the service you need: "))
if service == 1:
    print("Your airtime balance is #4500")
elif service ==2:
    print("Your data balance is 3.5GB")
elif service ==3:
    print("Your phone number is +2347023124576?" )
elif service == 4:
    print("Apologies, but there is no agent available to speak with you at the moment. Kindly try again later. Thank you")
elif service ==5:
    print(input("You are using Etisalat Service Provider"))
else:
    print("You've selected no service")   
