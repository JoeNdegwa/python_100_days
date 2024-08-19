from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("bisque3")
"""Draw a square"""
for _ in range(4):
  tim.forward(100)
  tim.left(90)

"""Draw a dotted line"""
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


"""Draw different shapes"""
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "medium blue", "firebrick", "medium violet red"]
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

def draw_shape(no_of_sides):
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

"""Random walk"""
for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(20)
    tim.setheading(random.choice(directions))

"""Alternative way to generate color - RGB & Tuple"""
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))
  
screen.exitonclick()
