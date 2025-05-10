print("Welcome to the secret auction program")
user_data = {}
flag = False

def find_winner(user_data):
    winner_name = ""
    winner_bid = 0
    for k in user_data:
        if user_data[k] > winner_bid:
            winner_name = k
            winner_bid = user_data[k]
    return winner_name, winner_bid

while not flag:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: "))
    print("Are there any other bidders? Type 'yes' or 'no'.")
    next_bidder = input()
    user_data[user_name] = user_bid
    if next_bidder == 'no':
        flag = True

winner_name, winner_bid = find_winner(user_data)
print(f"{winner_name} won the secret auction program with a bid of: {winner_bid}")