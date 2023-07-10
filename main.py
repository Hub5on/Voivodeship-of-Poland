import turtle

screen = turtle.Screen()
screen.title("Poland Voivodeships Game")

image = "map.gif"
screen.addshape(image)
screen.setup(width=800, height=699)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer_voivodeship = screen.textinput(title="Guess the Voivodeship", prompt="What's another Voivodeship's name?")
answer_voivodeship = answer_voivodeship.lower()



screen.exitonclick()