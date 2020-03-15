import turtle
import random

win = turtle.Screen()
tut = turtle.Turtle()
tut.speed(-1)
tut.shape('circle')
tut.width(10)

colors = ['red','green','blue','black','orange']

def dragging(x,y):
    tut.setheading(tut.towards(x,y))
    tut.goto(x,y)
    tut.ondrag(dragging)

def clickRight(x,y):
    tut.clear()

def up():
    tut.color(colors[random.randrange(len(colors))])

def main():
    turtle.listen()

    turtle.ondrag(dragging)
    turtle.onscreenclick(clickRight,3)
    turtle.onkey(up,'W')

    turtle.mainloop()


main()