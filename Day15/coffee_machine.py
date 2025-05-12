from inventory import inventory
from menu import menu

def get_price(drink):
    return menu[drink]['price']

def stock_availability_check(drink):
    water = menu[drink]["ingredients"]["water"]
    coffee = menu[drink]["ingredients"]["coffee"]
    milk = menu[drink]["ingredients"]["milk"]

    if water <= inventory["water"]["quantity"] and coffee <= inventory["coffee"]["quantity"] \
        and milk <= inventory["milk"]["quantity"]:
        return True
    else:
        return False
    
def update_inventory(drink):
    for item in menu[drink]["ingredients"]:
        inventory[item]["quantity"] -= menu[drink]["ingredients"][item]

def add_to_inventory():
    water = int(input("Enter water quantity to add (in ml): "))
    coffee = int(input("Enter coffee quantity to add (in g): "))
    milk = int(input("Enter milk quantity to add (in ml): "))
    inventory["water"]["quantity"] += water
    inventory["coffee"]["quantity"] += coffee
    inventory["milk"]["quantity"] += milk
    print("Inventory re-stocked successfully!")

def check_inventory():
    print("Inventory Report:")
    for item in inventory:
        print(item, inventory[item])

def select_drink():
    while True:
        try:
            user_choice = int(input("Choose an option: "))
            if user_choice in [1,2,3]:
                return user_choice
            elif user_choice == 4:
                check_inventory()
                print("\n",home_screen)
            elif user_choice == 5:
                add_to_inventory()
                print("\n",home_screen)
            elif user_choice == 6:
                return user_choice
            else:
                print("Please enter a valid option: 1, 2, 3, 4, 5 or 6.")
        except ValueError:
            print("Please enter a valid option: 1, 2, 3, 4, 5 or 6.")

home_screen = """
Please select your preferred drink
1. Espresso
2. Latte
3. Cappuccino
4. Inventory Report
5. Add to Inventory
6. Switch off
"""

while True:
    print(home_screen)

    user_choice = select_drink()
    # print(menu[user_choice])

    if user_choice == 6:
        break

    # Check if inventory has sufficient ingrediants or not
    while True:
        stock_available = stock_availability_check(user_choice)
        if stock_available == True:
            break
        else:
            print(f"Ingredients insufficient to prepare {menu[user_choice]["name"]}!")
            print(home_screen)
            user_choice = select_drink()


    # Get payment from user
    amount = get_price(user_choice)
    print(f"Please pay ${amount} for the drink")

    total_paid = 0
    while total_paid < amount:
        try:
            payment = float(input("$: "))
            total_paid += payment
            if total_paid == amount:
                print("Payment Received please wait for your order to process!")
                update_inventory(user_choice)
                break
            elif total_paid < amount:
                print(f"Insufficient amount, please pay ${amount-total_paid} more for the drink!")
            elif total_paid > amount:
                print("Payment Received please wait for your order to process!")
                print(f"Please collect your change $:{total_paid-amount}")
                update_inventory(user_choice)
                break
        except ValueError:
            print("Please enter a valid number.")

    print()
    check_inventory()