welcome_message = """
Welcome to Treasure Island.
Your mission is to find the treasure
"""
def user_choice(message):
    return input(message)

choice = user_choice("Choose a direction, Left or Right? ")
if choice == "Right":
    print("Game Over")
    exit
elif choice == "Left":
    choice = user_choice("Do you want to Swim or Wait? ")
    if choice == "Swim":
        print("Game Over")
        exit
    elif choice == "Wait":
        choice = user_choice("Which door you want to enter, Red, Blue or Yellow? ")
        if choice == "Red":
            print("Game Over")
            exit
        elif choice == "Blue":
            print("Game Over")
            exit
        elif choice == "Yellow":
            print("You win!")