import turtle
import pandas as pd
from state_label import StateLabel

# def get_mouse_click_coor(x, y):
#     print(x,y)
df = pd.read_csv("50_states.csv")
# print(df.columns)
# print(df.head())


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{str(len(guessed_states))}/50 Guess the state", prompt="Name a state....")
    title_case = answer_state.title()
    print(f"User answered {title_case}")
    if title_case not in guessed_states and title_case in df.state.values:
        guessed_states.append(title_case)
        state_row_x = df[df["state"] == title_case].values[0][1]
        state_row_y = df[df["state"] == title_case].values[0][2]
        state_label = StateLabel()
        state_label.goto(state_row_x, state_row_y)
        state_label.write(title_case)

    else:
        pass

turtle.mainloop()

# screen.exitonclick()