from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.reset()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="r", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
