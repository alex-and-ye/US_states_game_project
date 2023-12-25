import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(730, 496)
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")
guessed_states = []

n = 0
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{n}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        break
    for state in states.state:
        if state == answer_state and state not in guessed_states:
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(int(states.x[states.state == state]), int(states.y[states.state == state]))
            t.write(state)
            n += 1
            guessed_states.append(state)
    if n == 50:
        break
missing_states = [state for state in states.state if state not in guessed_states]
learn_data = pandas.DataFrame(missing_states)
learn_data.to_csv("states_to_learn.csv")
