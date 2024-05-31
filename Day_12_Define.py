"""def name():
    print("Hello")

name()

def show_info():
    print("My name is game")
    print('im 12 years  old')

show_info()"""

"""def triangle_area():
    base = int((input("Input base : ")))
    high = int(input("Input high : "))
    area = (1/2)*base*high
    print("Area of triangle is ",area)
triangle_area()"""


def triangle_area(base, high):
    area = (1 / 2) * base * high
    print("Area of triangle is ", area)


x = int(input("Input base : "))
y = int(input("Input high : "))
triangle_area(x, y)
