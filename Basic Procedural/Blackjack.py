import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    
def calculate_score(cards):
        return sum(cards)

def compare(pScore,cScore):
    if pScore == cScore:
        return "Draw"
    elif cScore == 0:
        return "Lose, Opponent got Blackjack"
    elif pScore == 0:
        return "Win! You got Blackjack"
    elif pScore > 21:
        return "Lose! You went bust"
    elif cScore > 21:
        return "Win! Oppoent went bust"
    else:
        return "You lose"

player_cards = []
computer_cards = []
computerScore = -1
playerScore = -1
game = True

#Deals cards
for pick in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())

while game == True:
    playerScore = calculate_score(player_cards)
    computerScore = calculate_score(computer_cards)
    
    print(f"Your cards: {player_cards}, current score: {playerScore}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if playerScore == 0 or computerScore == 0 or playerScore > 21:
        game = False
    else:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play == 'y':
             player_cards.append(deal_card())
        else:
            game = False
            
while computerScore != 0 and computerScore < 17:
    computer_cards.append(deal_card())
    computerScore = calculate_score(computer_cards)
    
print(f"Your final hand: {player_cards}, final score: {playerScore}")
print(f"Computer's final card: {computer_cards}, final score: {computerScore}")
print(compare(playerScore,computerScore))
    
        
