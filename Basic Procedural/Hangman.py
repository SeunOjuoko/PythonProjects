import random
#Hangman list
word_list = ["sonic", "tails", "knuckles","shadow", "rouge","omega","amy","cream","big","espio","charmy","vector","eggman"]
#Hangman Stages
stages = ['xxxxxx','xxxxx','xxxx','xxx','xx','x',' ',]
#Use a loop to guess again
game = True
correct = []
#Create a variable called Lives, begins with 6
lives = 6
#Random choose a word from the word_list and assign it to a variable called chosen_word, then print it
chosen_word = random.choice(word_list)
print(chosen_word)
#Create a placeholder with the same number of blanks 
placeholder = ""
for character in chosen_word:
    placeholder += "_ "
print(placeholder)

while game:
    #Ask user to guess a letteer and assign their answer to a varibale called guess (lowercase)
    guess = input("Guess the letter: ").lower()
    print(guess)

    #Check if the guessed letter is one of the chosen words 
    display = ""
    for character in chosen_word:
        if guess == character:          #Remember that the comparison isnt that complicated
            display += character
            correct.append(guess)
        elif character in correct:
            display += character
        else:
            display += "_ "
    print(display)
    #print(stages[lives])
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game = False
            print("Game Over!")

#If guess word is not chosen, then -1 and game over when it reaches 0
    if "_" not in display:
        game = False
        print("You Win!")
#Present stages that correpsond to the current number of lives
    print(stages[lives])