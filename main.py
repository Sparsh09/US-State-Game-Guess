import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


state_data = pd.read_csv("50_states.csv")
state_name = state_data["state"]
state_name = state_name.to_list()
print(state_name)

score = 0
while score != len(state_name):
    answer_state = screen.textinput(title=f"{score} States Correct", prompt="What's the another name");
    if answer_state in state_name:
        # print("Yes")
        # print(score)
        text = turtle.Turtle()
        state_det = (state_data[state_data.state == answer_state])
        x = int(state_det.x)
        y = int(state_det.y)
        text.penup()
        text.hideturtle()
        text.goto(x , y)
        text.write(answer_state)

        score += 1


screen.exitonclick()
