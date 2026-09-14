from turtle import Turtle, colormode, Screen
import random

screen = Screen()
colormode(255)
timy_turtle = Turtle()
timy_turtle.speed("fastest")
timy_turtle.penup()
timy_turtle.hideturtle()
timy_turtle.setheading(225)
timy_turtle.forward(300)
timy_turtle.setheading(0)
number_of_dots = 100

color_list = [(222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (166, 207, 165)]

for i in range(1, number_of_dots + 1):
    timy_turtle.dot(20, random.choice(color_list))
    timy_turtle.forward(50)

    if i % 10 == 0:
        timy_turtle.setheading(90)
        timy_turtle.forward(50)
        timy_turtle.setheading(180)
        timy_turtle.forward(500)
        timy_turtle.setheading(0)


screen.exitonclick()

