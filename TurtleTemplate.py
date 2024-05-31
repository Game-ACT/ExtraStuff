# Settings
import time
from turtle import *
speed(0)
color("Black")
width(1)
shape("turtle")
def terminateturtle():
    mainloop()
def terminate():
    exit()
def move_pen_to(x, y):
    penup()
    goto(x, y)
    pendown()
def reset():
    speed(0)
    color("Black")
    width(1)
    shape("turtle")
def terminateturtlewait(wait):
    mainloop()
    time.sleep(wait)
    exit()
# end
