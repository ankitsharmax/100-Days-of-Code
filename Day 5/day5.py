import random

alphabets = 'abcdefghijklmnopqrstuvwxwz'
letters = [e for e in alphabets] + [e for e in alphabets.upper()]
numbers = [e for e in '1234567890']
special_char = [e for e in '~`!@#$%^&*()']
# print(letters)
# print(numbers)
# print(special_char)

welcome_message = """
Welcom to Password Generator
"""
letters_n = int(input("How many letters do you like in your password? "))
numbers_n = int(input("How many numbers do you like in your password? "))
special_char_n = int(input("How many special characters do you like in your password? "))

generated_password = []

for l in range(0,letters_n):
    generated_password.append(random.choice(letters))

for n in range(0,numbers_n):
    generated_password.append(random.choice(numbers))

for s in range(0,special_char_n):
    generated_password.append(random.choice(special_char))

print(''.join(generated_password))
random.shuffle(generated_password)
print(''.join(generated_password))