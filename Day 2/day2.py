welcome_message = "Welcom to the tip calculator!\nWhat was the total bill? "
bill_amount = float(input(welcome_message))
tip_message = "How much tip would you like to give? 10, 12 or 15? "
tip_rate = int(input(tip_message))
split_message = "How many people to split the bill? "
split_count = int(input(split_message))
split_amount = round((bill_amount + (bill_amount*tip_rate/100))/split_count,2)
print(f"Each person should pay: ${split_amount}")