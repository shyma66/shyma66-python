from math import pi as PI
from math import pow
def area_of_a_rectangle(height,base):

    area = height * base
    return area

def area_of_a_triangle(height,base):

    area = 0.5 * height * base
    return area

def area_of_a_circle(radius):

    area = PI * pow(radius,2)
    return area


while True:
    question = print("Enter your figur :\n1 - rectangle\n2 - triangle\n3 - circle ")
    figure = input("-> ")
    if figure == "1":
        print("height")
        height = float(input("-> "))
        print("base")
        base = float(input("-> "))
        area = area_of_a_rectangle(height, base)
        print("area of a rectangle is",area)
    if figure == "2":
        print("height")
        height = float(input("-> "))
        print("base")
        base = float(input())
        area = area_of_a_triangle(height, base)
        print("area of a triangle is",area)
    if figure == "3":
        print("radius")
        radius = float(input("-> "))
        area = area_of_a_circle(radius)
        print("area of a circle is",area)