import questions
import random

welcome_message = """
||   ||    |||||    ||||||
||  ||     ||  ||   ||  
|| ||      ||  ||   ||  
||||       ||||     ||  
||  ||     ||  ||   ||
||   ||    ||  ||   ||
||    ||   |||||    ||||||

Welcom to Kaun Banega Corepati Game!
Main hun aapka host aur dost Python aur hm aaj khelenge Kaun Banega Corepati Game!
"""

print(welcome_message)

user_points = 0
game_over = False

questions = questions.questions
random.shuffle(questions)
# print(questions)

for q in questions:
    print(q["question"])
    for e in q["options"]:
        print(e)
    # print(q["correct_answer"])
    user_ans = input("Choose an option: ")
    print()
    if user_ans == q["correct_answer"]:
        user_points += 1
    else:
        print(f"Thanks for playing, you'll be taking away Rs. {user_points} Crore today!")
        game_over = True
        break

if game_over == False:
    print(f"Thanks for playing, you'll be taking away Rs. {user_points} Crore today!")

