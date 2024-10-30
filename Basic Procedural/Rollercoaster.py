print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age <= 12:
        bill = 5
        print("Child tickets are £5")
    elif age < 18:
        bill = 7
        print("Teenager tickets are £7")
    elif age >= 45 and age <= 55:
        print("Seniors go free")
    else:
        bill = 12
        print("Adult tickets are £12")

    photo = input("Do you want a photo? Y or N: ")
    if photo == "Y":
        bill += 3

    print(f"Your final bil is £{bill}")
else:
    print("Grow up!!!")