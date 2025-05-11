import random

welcome_message = """
Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.
"""

level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
if level == 'easy':
    health = 10
    print(f"You have {health} attempts remaining to guess the number.")
elif level == 'hard':
    health = 5
    print("You have {health} attempts remaining to guess the number.")
else:
    print("Invalid input!")

def guess_check(user_guess,random_choice):
    if user_guess == random_choice:
        return "You Win!"
    # Guess is lesser than random choice
    elif (user_guess - random_choice) <= -20:
        return "Too Low"
    elif (user_guess - random_choice) > -20 and (user_guess - random_choice) < 0:
        return "Low"
    # Guess is greater than random choice
    elif (user_guess - random_choice) >= 20:
        return "Too High"
    elif (user_guess - random_choice) < 20 and (user_guess - random_choice) > 0:
        return "High"

random_choice = random.randint(1,100)
flag = False
while not flag:
    user_guess = int(input("Make a guess: "))
    guess_results = guess_check(user_guess, random_choice)
    print(guess_results)
    if guess_results != "You Win!":
        health -= 1
        if health != 0:
            print("Guess again.")
    elif guess_results == "You Win!":
        break
    if health == 0:
        flag = True
        print("Game Over!")
    