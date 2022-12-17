# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]
choose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))
comp_choose = random.randint(0, 2)
if choose >= 3 or choose < 0:
    print('Invalid number ! You lose !')
else:
    print(options[choose])
    print('Computer choose:')
    print(options[comp_choose])

    if choose == 0 and comp_choose == 2:
        print('You win!')
    elif comp_choose == 0  and choose == 2:
        print('You lose!')
    elif comp_choose > choose:
        print('You lose!')
    elif choose > comp_choose:
        print('You win!')
    elif comp_choose == choose:
        print('It\'s a draw')
