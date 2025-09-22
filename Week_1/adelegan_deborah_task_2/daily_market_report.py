# Daily Market Report

# Accept the name of the market
market_name = input("What is the name of the market please?: ")

# Collect the number of traders
number_of_traders = input("How many traders are in this market?: ")

# Accept the market revenue from user, saving it as an integer
market_revenue = int(input("How much do you make in this market daily?: "))

# Print the variables using fstring
print(f"According to the report from one of the traders in {market_name} market, the average amount made daily from sales is about {market_revenue:,} naira")