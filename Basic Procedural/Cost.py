print("Welcome to the tip calculator!")
total = float(input("What is your total bill? £"))
tip = int(input("How much would you like to tip? 10, 12, or 15? "))
split = int(input("How many people are splitting the bill? "))
percentage = tip/100
bill = float(total * (1 + percentage)/split)
pay = round(bill,2)
print(f"Each person should pay: £ {pay}")