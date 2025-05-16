import art
import game_data
import random

def get_data():
    set1 = random.choice(data) # obtaining a dictionary
    return set1
def comparision(s1,s2,choice):
    if choice == 'a' and s1['follower_count'] > s2 ['follower_count'] :
        return 1
    elif choice == 'b' and s1['follower_count'] < s2 ['follower_count'] :
        return 1
    else:
        return 0

print(art.logo)
score = 0
data = game_data.data

while( True): # run as long as break is not encountered
    com1 = get_data()
    com2 = get_data()
    print(f"Compare A: {com1['name']}, a {com1['description']}, from {com1['country']}")
    print(art.vs)
    print(f"Compare B: {com2['name']}, a {com2['description']}, from {com2['country']}")
    compare = input("Who has more followers: A or B: ").lower()[:1]## truncates to one letter.
    # print(compare)
    if comparision(com1,com2,compare) == 1:
        score+=1
    elif comparision(com1,com2,compare) == 0:
        print(art.logo)
        print(f"Sorry, that's wrong! Final score: {score}")
        break
    print(f"Your current scores: {score}\n")

