"""Draw dots using random colors"""
import turtle as tim
import random
import colorgram

screen = tim.Screen()
# rgb_colors = []
# colors = colorgram.extract('dotted.png', 200)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim.colormode(255)
color_list = [(242, 242, 241), (217, 163, 56), (235, 215, 59), (234, 38, 79), (175, 29, 137), (228, 232, 239), (237, 79, 43), (78, 172, 77), (231, 246, 242), (6, 106, 178), (122, 184, 81), (201, 11, 99), (241, 212, 224), (7, 162, 80), (47, 48, 143), (18, 20, 21), (225, 165, 186), (225, 122, 167), (3, 158, 215), (124, 166, 207), (84, 76, 48), (147, 129, 77), (171, 211, 163), (96, 112, 176)]

tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen.exitonclick()
