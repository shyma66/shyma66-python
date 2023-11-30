def rectangle_area():
    area = width * length
    return area

def triangle_area():
    area = base * height / 2
    return area

def circle_area():
    PI = 3.14
    area = PI * radius**2
    return area

question = input("which area do you need to know? \n(rectangle,triangle or circle) \n-> ")

if question == "rectangle" :
    width = float(input("Write your Width \n->"))
    length = float(input("Write your Length \n->"))
    print(rectangle_area())
elif question == "triangle" :
    base = float(input("Write your Base \n->"))
    height = float(input("Write your height \n->"))
    print(triangle_area())
elif question == "circle":
    radius = float(input("Write your Radius \n->"))
    print(circle_area())