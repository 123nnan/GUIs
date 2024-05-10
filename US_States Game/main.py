import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
data = pd.read_csv('50_states.csv')
image = 'blank_states_img.gif'
screen.setup(width=725, height=491)
screen.addshape(image)
all_states = data.state.to_list()

turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    state_count = len(data['state'])
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{state_count}  States Correct", prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        not_in_list = [state for state in all_states if state not in guessed_states]

        df = pd.DataFrame(not_in_list)
        df.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        x = int(data[data.state == answer_state].x.iloc[0])
        y = int(data[data.state == answer_state].y.iloc[0])
        t.goto(x, y)
        t.write(answer_state)

#states_to_learn.csv
#generate contain just the name of state that aren't guessed by the user


screen.exitonclick()
