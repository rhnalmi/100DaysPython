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

RPS = [rock,paper,scissors]
user_choose = int(input("What will you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))

computer_choice = random.randint(0,2)

#print(f"computer choose {computer_choice}")

if computer_choice > user_choose:
    print(RPS[user_choose])
    print("vs")
    print(RPS[computer_choice])
    print(f"computer choose {computer_choice}")
    print("You Lost!")
if computer_choice < user_choose:
    print(RPS[user_choose])
    print("vs")
    print(RPS[computer_choice])
    print(f"computer choose {computer_choice}")
    print("You Win!")
if computer_choice == user_choose:
    print(RPS[user_choose])
    print("vs")
    print(RPS[computer_choice])
    print(f"computer choose {computer_choice}")
    print("It's a draw")
