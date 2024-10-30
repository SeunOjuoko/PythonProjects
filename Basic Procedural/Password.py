import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','£','$','%','&',"(",")",'+','-','*','/','@']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters for your password? "))
nr_numbers = int(input("How many numbers for your password? "))
nr_symbols = int(input("How many symbols for your password? "))

password = ""

for character_letter in range (0,nr_letters):
    random_letter = random.choice(letters)
    password += random_letter

for character_number in range (0,nr_numbers):
    random_number = random.choice(numbers)
    password += random_number

for character_symbol in range (0,nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol

print(f"The easy password is: {password}")

password_list = []
for character_letter in range (0,nr_letters):
    password_list.append(random.choice(letters))

for character_number in range (0,nr_numbers):
    password_list.append(random.choice(numbers))

for character_symbol in range (0,nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password_string = ""
for char in password_list:
    password_string += char

print(f"The hard password is {password_string}")



