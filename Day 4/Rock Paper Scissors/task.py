import random

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
game_choices = [rock,paper,scissors]
user_choice = int(input("use 0 for Rock,1 for  Paper, 2 for Scissors? \n"))

if user_choice < 0 or user_choice > 2:
    print("invalid choice")


computer_choice = random.randint(0,2)
print(f"you chose:{game_choices[user_choice]}")
print(f"computer chose:{game_choices[computer_choice]}")

if computer_choice == user_choice:
    print("It's a tie!")
elif user_choice > computer_choice:
    print("you Win!")
elif user_choice ==0 and computer_choice == 2:
    print("you win!")
elif user_choice == 2 and computer_choice == 0:
    print("you lose!")
elif user_choice < computer_choice:
    print("you lose!")







