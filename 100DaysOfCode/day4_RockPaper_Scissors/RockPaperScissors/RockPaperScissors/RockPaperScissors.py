
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to the Rock, Paper, Scissors game!")
player_choice = int(input("Select 0 for rock, 1 for paper, 2 for scissors: "))

computer_choice = random.randint(0,2)
winning_results = [-2, 1, 1] # Player choice - computer choice, as ints
game_options_list = [rock, paper, scissors]

print(f"You chose:{player_choice}  Computer chose:{computer_choice}\n")

if player_choice - computer_choice in winning_results:
  print(f"You chose:\n{game_options_list[player_choice]}\nComputer chose:{game_options_list[computer_choice]}\n")
  print("You win!")
elif player_choice - computer_choice != 0:
  print(f"You chose:\n{game_options_list[player_choice]}\nComputer chose:{game_options_list[computer_choice]}\n")
  print("You lose!")
else:
  print(f"You chose:\n{game_options_list[player_choice]}\nComputer chose:{game_options_list[computer_choice]}\n")
  print("It's a tie!")
