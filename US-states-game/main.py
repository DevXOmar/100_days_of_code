from turtle import Turtle,Screen
import pandas as pd
from more import More

data_1 = pd.read_csv("50_states.csv") ##

clean_data = data_1.copy()
clean_data["state"] = clean_data["state"].str.lower()
print(clean_data)

image = "blank_states_img.gif"
tims = Turtle()

screen = Screen()
screen.title("U.S States Game")

screen.addshape(image)## both the lines are complementary
tims.shape(image)##

score = 0

score_board = Turtle()
score_board.penup()
score_board.hideturtle()
score_board.goto(250,300)
score_board.write(f"Score : {score}",font = ("Arial",20,"normal"))

list1 = []

game_on = True
while(game_on):
    guess = screen.textinput("Guess the name: ","Enter the name of the state: ").lower()
    print(guess)

    if not (clean_data.state == guess).any():
        continue
    data_row = clean_data[clean_data.state == guess] ##Obtaining the data_row
    if guess not in list1:
       score +=1
    list1.append(guess)
    print(data_row)
    x_value = data_row.x.values[0] #
    y_value = data_row.y.values[0] #
    More(guess,x_value,y_value)
    score_board.clear()
    score_board.write(f"Score : {score}", font=("Arial", 20, "normal"))

# print(data_row.x.values[0])## accessing the clean value of x
# print(data_row.y.values[0])## accessing the clean value of y


screen.mainloop()