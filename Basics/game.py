
# # snack water gun game

# import random
# def play_game(compchoice, userchoice):
#     print(f"Computer choice is {compchoice}")
#     if compchoice == userchoice:
#         print('Match Drow :|')
#     elif (compchoice== "s" and userchoice== "w" or compchoice == "w" and userchoice == "g" or compchoice =="g" and userchoice =="s" ):
#         print('You lose')
#     else:
#         print('You win')

# choices = ['s', 'w', 'g']
# # compchoice = random.choice(choices)
# while True:
#     print("========================================\n")
#     print("Welcome to snake water gun game :- \n")
#     print("Enter you choice s = snake, w = water, g = gun, e = exit :- ")
#     userchoice = input()
#     if userchoice not in choices and userchoice != 'e':
#         print("Invalid choice, please try again.")
#         continue
#     if userchoice == 'e':
#         break
#     compchoice = random.choice(choices)
#     play_game(compchoice, userchoice)

# solve this same game problem using matrix
# 0 = draw, 1 = user win, -1 = computer win 

import random

# Mapping choices to indices
choice_map = {'s': 0, 'w': 1, 'g': 2}

# Matrix representing game outcomes: matrix[user][computer]
# Rows represent User's choice: s (0), w (1), g (2)
# Columns represent Computer's choice: s (0), w (1), g (2)
# Outcomes: 0 = draw, 1 = user win, -1 = computer win
game_matrix = [
    [0, 1, -1],  # User plays 's' (snake drinks water -> 1, gun kills snake -> -1)
    [-1, 0, 1],  # User plays 'w' (snake drinks water -> -1, water rusts gun -> 1)
    [1, -1, 0]   # User plays 'g' (gun kills snake -> 1, water rusts gun -> -1)
]

def play_game_matrix(compchoice, userchoice):
    print(f"Computer choice is {compchoice}")
    
    user_idx = choice_map[userchoice]
    comp_idx = choice_map[compchoice]
    
    result = game_matrix[user_idx][comp_idx]
    
    if result == 0:
        print('Match Draw :|')
    elif result == 1:
        print('You win')
    elif result == -1:
        print('You lose')

choices = ['s', 'w', 'g']

if __name__ == "__main__":
    while True:
        print("========================================\n")
        print("Welcome to snake water gun game :- \n")
        print("Enter you choice s = snake, w = water, g = gun, e = exit :- ")
        userchoice = input().strip().lower()
        
        if userchoice == 'e':
            break
        if userchoice not in choices:
            print("Invalid choice, please try again.")
            continue
            
        compchoice = random.choice(choices)
        play_game_matrix(compchoice, userchoice)
