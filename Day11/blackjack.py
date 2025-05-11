import random

print("Welcome to the game of Blackjack")
cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K"]

random.shuffle(cards)

computer_choice = [cards.pop(),cards.pop()]
user_choice = [cards.pop(), cards.pop()]

print(f"Computer's Cards: [{computer_choice[0]},?]")
print(f"User Cards: ",user_choice)

def score_calculate(cards):
    total_score = 0
    for card in cards:
        if card in ["K","Q","J"]:
            total_score += 10
        else:
            total_score += card
    if total_score < 21 and 1 in cards:
        total_score += 10
    if total_score > 21 and 1 in cards:
        total_score -= 10
    return total_score

def find_winner(computer_score, user_score):
    if user_score > 21 and computer_score > 21:
        print("No one Won!")
    elif user_score > 21:
        print("Computer Won!")
    elif computer_score > 21:
        print("User Won!")
    elif user_score == computer_score:
        print("Match Draw!")
    elif user_score > computer_score:
        print("User Won!")
    else:
        print("Computer Won!")

computer_score = score_calculate(computer_choice)
user_score = score_calculate(user_choice)

# print("Computer Score: ",computer_score)
print("User Score: ",user_score)

if user_score < 21:
    user_redraw = input("Do you want to draw another card? 'yes' or 'no': ")
    if user_redraw == 'yes':
        user_choice.append(cards.pop())
    print(f"User Cards: ",user_choice)
    user_score = score_calculate(user_choice)

if computer_score < 17:
    computer_choice.append(cards.pop())
    print(f"Computer Cards: ",computer_choice)
    computer_score = score_calculate(computer_choice)

print("Computer Score: ",computer_score)
print("User Score: ",user_score)

find_winner(computer_score, user_score)


