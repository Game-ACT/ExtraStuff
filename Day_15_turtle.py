from turtle import *
import random
from random import choice, randint

random.seed(222)
my_turtle = Turtle()
my_turtle.speed(0)


def star(n_point, line_color, fill_color):
    angle = 180 - (180 / n_point)
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    for i in range(n_point):
        my_turtle.forward(50)
        my_turtle.right(angle)
    my_turtle.end_fill()


def move_pen_to(x, y):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()


def move_pen_forward(distance):
    my_turtle.penup()
    my_turtle.forward(distance)
    my_turtle.pendown()


possible_star_points = [5, 9, 7, 11, 13, 15, 17]
line_colors = ["#f36c60", "#9575cd", "#2baf2b"]
fill_colors = ["#212121", "#37474f", "#44140c", "#5d4037"]
for i in range(10):
    x = randint(-150, 150)
    y = randint(-150, 150)
    star_point = choice(possible_star_points)
    line_color = choice(line_colors)
    fill_color = choice(fill_colors)

    move_pen_to(x, y)
    star(star_point, line_color, fill_color)