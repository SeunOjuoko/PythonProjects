import random

number = random.randint(1, 100)
game = True
lives = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

if difficulty == 'easy':
    lives = 10

while game == True:
    print(f"You have {lives} attempts remaining to guess the number")
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        lives -= 1
        print("I was expecting a number silly")
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Guess Again: "))
    if guess > number:
        lives -= 1
        print("Too high.")
        print("Guess Again.")
    elif guess < number:
        lives -= 1
        print("Too low.")
        print("Guess Again.")
    elif guess == number:
        print(f"You got it! The answer was {number}")
        game = False
    
    if lives == 0:
        print("You have run out of guess, you lose!")
        game = False