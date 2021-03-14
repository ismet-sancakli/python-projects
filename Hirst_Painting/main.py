"""
import colorgram
# This scripts for the color list.
rgb_colors = []
colors = colorgram.extract("image.jpg", 30)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""
import turtle as turtle_module
import random
turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(245, 246, 250), (252, 251, 247), (188, 74, 20), (56, 34, 13), (149, 26, 9), (237, 226, 77), (24, 31, 60), (113, 167, 210), (45, 85, 143), (227, 243, 238), (217, 154, 82), (34, 50, 124), (191, 144, 25), (26, 51, 29), (201, 93, 126), (242, 214, 6), (250, 244, 249), (119, 35, 51), (120, 187, 149), (55, 129, 74), (70, 82, 17), (36, 84, 40), (142, 51, 58), (74, 128, 200), (205, 86, 62), (82, 31, 44), (104, 180, 70), (148, 204, 223), (197, 120, 162), (23, 77, 100)]
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

screen = turtle_module.Screen()
screen.exitonclick()



