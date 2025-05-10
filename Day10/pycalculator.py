welcome_message = """
 _____________________
|    PyCalculator     |
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

operations = "+ - * /"

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def get_results(num1, num2, operation):
    if operation == "+":
        results = add(num1,num2)
    elif operation == "-":
        results = sub(num1,num2)
    elif operation == "*":
        results = mul(num1,num2)
    elif operation == "/":
        results = div(num1,num2)
    
    if results == int(results): results = int(results)
    if num1 == int(num1): num1 = int(num1)
    if num2 == int(num2): num2 = int(num2)
    print(f"{num1} {operation} {num2} = {results}")
    return num2, results

first_num = float(input("What's the first number?: "))
flag = False

while not flag:
    print(operations)
    operation_type = input("Pick and operation: ")
    next_num = float(input("What's the next number?: "))
    next_num, first_num = get_results(first_num, next_num, operation_type)
    user_choice = input(f"Type 'y' to continue calculating with {first_num}, or type 'n' to start a new calculations: ")
    if user_choice == 'n':
        flag = True