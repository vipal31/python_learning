###Rock-paper-scissor-game

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

game_images = [rock, paper, scissors]

try:
    user_choice = int(input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

    if user_choice >= 3 or user_choice <0:
        print("You typed an invalid number, you loose, thanks for playing!")

    else:
        print(f"You Choose: {game_images[user_choice]}")
        computer_choice = random.randint(0,2)
        print(f"Computer Choose:  {game_images[computer_choice]}")

        if computer_choice == user_choice:
            print("Its'a draw!")
        elif user_choice == 0 and computer_choice == 2:
            print("You Win!")
        elif user_choice == 1 and computer_choice == 0:
            print("You Win!")
        elif user_choice == 2 and computer_choice == 1:
            print("You Win!")
        else:
            print("You loose!")

except ValueError:
    print("You typed an invalid number, you loose, thanks for playing!")
