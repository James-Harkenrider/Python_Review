import turtle
import pandas
import time

screen = turtle.Screen()
screen.tracer(0)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.update()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
state_csv = pandas.read_csv("50_states.csv")
state_csv_dict = state_csv.to_dict()
state_dict = {}
for state_index in state_csv_dict['state']:
    state = state_csv_dict['state'][state_index]
    state_dict[state] = (state_csv_dict['x'][state_index], state_csv_dict['y'][state_index])

state_answers = []
score = 0
print(state_dict.keys())
while len(state_dict.keys()) > 0:
    screen.update()
    time.sleep(0.1)
    if answer_state.title() in state_dict.keys():
        answer = turtle.Turtle()
        answer.hideturtle()
        answer.penup()
        answer.goto(state_dict[answer_state.title()])
        answer.write(answer_state.title())
        state_answers.append(answer)
        score += 1
        state_dict.pop(answer_state.title())
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")


print(state_dict)

screen.exitonclick()
