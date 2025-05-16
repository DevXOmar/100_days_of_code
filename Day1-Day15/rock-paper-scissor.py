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
x = int(input("Enter 0 for rock, 1 for paper and 2 for scissors: "))
num = random.randint(0,2)
#print(num)
if x == 0 and num == 0:
    print(rock)
    print("Computer choose")
    print(rock)
    print("Its a draw.")

elif x == 1 and num == 1:
    print(paper)
    print("Computer choose")
    print(paper)
    print("Its a draw.")
elif x == 2 and num == 2:
    print(scissors)
    print("Computer choose")
    print(scissors)
    print("Its a draw.")

if x == 0 and num == 1:
    print(rock)
    print("Computer choose")
    print(paper)
    print("Computer won.")
elif x == 0 and num == 2:
    print(rock)
    print("Computer choose")
    print(scissors)
    print("You won.")
if x == 1 and num == 0:
    print(paper)
    print("Computer choose")
    print(rock)
    print("You won.")
elif x == 1 and num == 2:
    print(paper)
    print("Computer choose")
    print(scissors)
    print("Computer won.")
if x == 2 and num == 0:
    print(scissors)
    print("Computer choose")
    print(rock)
    print("Computer won.")
elif x == 2 and num == 1:
    print(scissors)
    print("Computer choose")
    print(paper)
    print("You won.")