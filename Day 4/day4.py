import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

game_images = [rock,paper,scissors]
game_text = ["rock","paper","scissors"]

welcome_message = """
Select your choice,
0: Rock
1: Paper
2: Scissors
"""

computer_choice = random.randint(0,2)

user_choice = int(input(welcome_message))
if user_choice >= 0 and user_choice <= 2:
    game_screen = f"""
-------------------------------------------
User Choice: {game_text[user_choice]}
{game_images[user_choice]}
-------------------------------------------
Computer Choice: {game_text[computer_choice]}
{game_images[computer_choice]}
-------------------------------------------
    """
    print(game_screen)

    if user_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("Draw!")
else:
    print("You selected a invalid option. You lose!")
    exit