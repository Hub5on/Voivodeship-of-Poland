import turtle
import pandas as pd

data = pd.read_csv("voivodeships.csv")
all_voivodeships = data.voivodeship.tolist()
image = "map.gif"
guessed_voivodeship = []

screen = turtle.Screen()
screen.title("Poland Voivodeships Game")
screen.addshape(image)
screen.setup(width=800, height=699)
turtle.shape(image)

while len(guessed_voivodeship) < len(all_voivodeships):
    answer_voivodeship = screen.textinput(title=f"{len(guessed_voivodeship)}/16 Voivodeships Correct", prompt="What's another Voivodeship's name?").lower()

    if answer_voivodeship in all_voivodeships:
        guessed_voivodeship.append(answer_voivodeship)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        voivodeship_data = data[data.voivodeship == answer_voivodeship]
        t.goto(int(voivodeship_data.x), int(voivodeship_data.y))
        t.write(answer_voivodeship, align="center", font=("Arial", 15, "normal"))


screen.exitonclick()