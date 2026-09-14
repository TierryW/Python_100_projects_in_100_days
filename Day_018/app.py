from turtle import Turtle, Screen, colormode
import random

timmy_turtle = Turtle()
screen = Screen()
# timmy_turtle.shape("turtle")
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# direction = [0, 90, 180, 270]
# timmy_turtle.pensize(15)
timmy_turtle.speed("fastest")


# Draw a Square
# for i in range(4):
#     timmy_turtle.forward(100)
#     timmy_turtle.left(90)


# Draw a Dashed Line
# for i in range(15):
#     timmy_turtle.forward(10)
#     timmy_turtle.penup()
#     timmy_turtle.forward(10)
#     timmy_turtle.pendown()


# Drawing Different Shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         timmy_turtle.forward(100)
#         timmy_turtle.right(angle)

# for shape_side in range(3, 11):
#     timmy_turtle.color(random_color())
#     draw_shape(shape_side)


# Generate a Random Walk
# for i in range(200):
#     timmy_turtle.color(random_color())
#     timmy_turtle.forward(30)
#     timmy_turtle.setheading(random.choice(direction))


# Draw a Spirograph
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy_turtle.color(random_color())
        timmy_turtle.circle(100)
        timmy_turtle.setheading(timmy_turtle.heading() + size_of_gap)

draw_spirograph(5)


screen.exitonclick()

