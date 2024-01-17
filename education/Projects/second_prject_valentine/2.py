import turtle


def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_rectangle(color, width, height, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def move_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_unicorn():
    turtle.speed(2)

    # Draw the body
    draw_circle("purple", 100, 0, -100)

    # Draw the head
    draw_circle("purple", 60, 0, 40)

    # Draw the eyes
    draw_circle("white", 8, 10, 70)
    draw_circle("black", 4, 12, 72)

    # Draw the horn
    move_to(0, 90)
    turtle.goto(10, 150)
    turtle.goto(0, 120)
    turtle.goto(-10, 150)

    # Draw the mane
    move_to(-30, 60)
    turtle.right(20)
    for _ in range(4):
        draw_circle("blue", 25, turtle.xcor(), turtle.ycor())
        turtle.right(90)

    # Draw the legs
    draw_rectangle("purple", 15, 40, -25, -100)
    draw_rectangle("purple", 15, 40, 10, -100)

    # Hide the turtle
    turtle.hideturtle()


# Function to move the unicorn
def move_unicorn():
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()

    # Move the unicorn to the right
    for _ in range(4):
        turtle.forward(50)
        turtle.left(10)

    # Move the unicorn to the left
    for _ in range(4):
        turtle.backward(50)
        turtle.right(10)


# Call the function to draw the unicorn
draw_unicorn()

# Call the function to move the unicorn
move_unicorn()

# Keep the window open
turtle.done()
