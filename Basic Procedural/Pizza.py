
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

Bill = 0

if size == 'S':
    Bill +=15
    if pepperoni == 'Y':
        Bill +=2
elif size == 'M':
    Bill +=20
    if pepperoni == 'Y':
        Bill +=3
else:
    Bill +=25
    if pepperoni == 'Y':
        Bill +=1
    
if extra_cheese == 'Y':
    Bill +=1