import random
print(r'''              .__                                  __            __  .__                                           
__  _  __ ____ |  |   ____  ____   _____   ____   _/  |_ ____   _/  |_|  |__   ____      _________    _____   ____  
\ \/ \/ _/ __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __/  _ \  \   __|  |  \_/ __ \    / ___\__  \  /     \_/ __ \ 
 \     /\  ___/|  |_\  \__(  <_> |  Y Y  \  ___/   |  |(  <_> )  |  | |   Y  \  ___/   / /_/  / __ \|  Y Y  \  ___/ 
  \/\_/  \___  |____/\___  \____/|__|_|  /\___  >  |__| \____/   |__| |___|  /\___  >  \___  (____  |__|_|  /\___  >
             \/          \/            \/     \/                           \/     \/  /_____/     \/      \/     \/''')
print("Welcome to the number guessing game: ")
print("I am thinking of a number between 1 and 100.")

def game(turn,num):
    count = turn
    for x in range(turn):
        print(f"You have {count} chances left.")
        count -=1
        guess = int(input("Make a guess: "))
        if guess == num:
            return 1
        elif guess > num:
            print("Too high.")
            if count >0:
               print("Guess again!")
        elif guess < num:
            print("Too low.")
            if count > 0:
               print("Guess again!")
    print("You've run out of guesses. Try again!")


number = random.randint(1,100)
level = input("choose a level: easy or hard: ")
if level == 'easy':
    if game(10,number) == 1:
        print("You won!")

else:
    if game(5, number) == 1:
        print("You won!")
# print(number)
# if game(number) == 1:
#     print("You won!")

