import random
import art
def play_game():
    print(art.logo)
    def deal_cards():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] ### The cards
        return random.choice(cards)
    def calculate_score(list1):
        sum1 = sum(list1)
        return sum1
    def win_lose(sum1,sum2):
       if sum1 == 21 :
           return 4
       elif sum2 == 21:
           return 5
       elif sum1 >21 and sum2>21:
           return 6
       elif sum1 >21:
           return 1
       elif sum2 >21:
           return 0
       elif (sum1 > sum2):
           return 0
       elif (sum1 < sum2 ):
           return 1
       elif sum1 == sum2:
           return 3

    computer = []
    user = []

    for x in range(2): ## we got 2 cards now.
        computer.append(deal_cards())
        user.append(deal_cards())
    print("     Computer's first cards: ",computer[0])## only one card
    print("     User's cards: ",user," sum: ",calculate_score(user))
    print()
    sumc = calculate_score(computer)
    sumu = calculate_score(user)

    while sumc <17 : ## computer is obligated to hit until they reach 17.
            computer.append(deal_cards())
            sumc = calculate_score(computer)
    while sumu <21:
        consent = input("Enter if you want a gamble: y or n: ").lower()
        if consent != 'y':
            break
        user.append(deal_cards())
        sumu = calculate_score(user)
        print("     Computer's first cards: ", computer[0])
        print("     User's deck: ", user," sum: ",calculate_score(user))

    result = win_lose(sumc,sumu)

    print()
    print("     Computer's final deck: ",computer)
    print("     User's final deck: ",user," sum: ",calculate_score(user))
    # print(result)

    if result == 1:
        print("User won!")
    elif result == 0:
        print("Computer won!")
    elif result == 3 or result == 6:
        print("Draw.")
    elif result == 4:
        print("Lose, Opponent has a black jack!")
    elif result == 5:
        print("Win, you have a black jack!")

consent = input("Do you want to play the game? y or n: ").lower()
if consent == 'y':
    play_game()
else:
    print("Come again sometime.")
## The computer always . gambles again, chooses 3 cards regardless.
## No no it did not gamble like that, if <17 is the condition.