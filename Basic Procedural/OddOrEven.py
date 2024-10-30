print("Welcome to the Odd or Even Game Show!")
Number = int(input("Pick a number: "))
print("Your number is...")
Result = Number % 2
if Result == 0:
    print("Even!!")
else:
    print("Odd!!!")
