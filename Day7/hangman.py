import random

welcome_message = """
Welcome to the hangman game!
"""

word_list = ["apple","banana","orange","grapes"]
# Randomly choose a word to start the game
random_word = random.choice(word_list)
# print(random_word)

# Ask user to guess the number
print(welcome_message)

placeholder = ["_"]*len(random_word)
print(*placeholder)

game_over = False

wrong_guess_1 = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""

wrong_guess_2 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
"""

wrong_guess_3 = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""

wrong_guess_4 = """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
"""

wrong_guess_5 = """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
"""

wrong_guess_6 = """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""

health = 6

while not game_over:
    user_guess = input("\nGuess a letter: ").lower()
    print(user_guess)
    health_check = 0

    if user_guess in placeholder:
        print(f"\nAlready guessed: {user_guess}!")

    # Check the letter in the word
    for i in range(len(random_word)):
        if random_word[i] == user_guess:
            placeholder[i] = user_guess
            health_check = 1
    print(*placeholder)
    if health_check == 0:
        health -= 1

    if health == 5:
        print("-----------------------")
        print(wrong_guess_1)
    elif health == 4:
        print("-----------------------")
        print(wrong_guess_2)
    elif health == 3:
        print("-----------------------")
        print(wrong_guess_3)
    elif health == 2:
        print("-----------------------")
        print(wrong_guess_4)
    elif health == 1:
        print("-----------------------")
        print(wrong_guess_5)
    elif health == 0:
        print("-----------------------")
        print(wrong_guess_6)
        print("-----------------------")
        print(f"Chosen word was: {random_word}")
        print("\nYou lost!")
        break

    if "_" not in placeholder:
        game_over = True
        print("You win!")