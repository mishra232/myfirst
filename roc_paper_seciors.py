# import random 
# def select_computer_action():
#     possible_action = ["rock","paper","scissors"]
#     computer_action = random.choice(possible_action)
#     return computer_action
# def determine_winner(p_comuter_action,p_user_action):
#     if p_user_action == p_comuter_action:
#         print(f"Both player selcted {p_user_action}. It's tie!")
#     elif p_user_action == "rock":
#         if p_comuter_action == "scissors":
#             print("Rock samshes scissors! you win!")
#         else:
#             print("paper covers rock! you lose!")
#     elif p_user_action == "paper":
#         if p_comuter_action == "scissors":
#             print("scissors cuts paper! you lose!")
#         else:
#             print("paper covers rock! you win!")
#     elif p_user_action == "scissors":
#         if p_comuter_action == "paper":
#             print("scissors cuts paper! you win!")
#         else:
#             print("Rock samshes scissors! you lose!")
# while True:
#     user_action = input("Enter a choice {rock,paper,scissors}: ")
#     computer_action = select_computer_action
#     print(f"You chose {user_action}, computer chose{computer_action}")
#     determine_winner(computer_action,user_action)
#     play_again = input("Play again (Y/N)?")
#     if play_again !="Y":
#         break


