import turtle
#Define a function to draw a rectangle
def draw_rectangle (width, long, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(long)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

#Define a function to draw a isosceles triangle
def draw_triangle(length, color):
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.forward(length)
  turtle.left(120)
  turtle.forward(length)
  turtle.left(120)
  turtle.forward(length)
  turtle.left(120)
  turtle.end_fill()

#Define a function to draw a circle
def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

#Define a function to draw a square
def draw_square(length, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()

#Define a function to draw a elip
def draw_oval (radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    i = 0
    while i < 2:
        turtle.circle(radius, 90)
        turtle.circle(radius / 2, 90)
        i += 1
    turtle.end_fill()

#Define a function to draw a pentagon
def draw_pentagon(length, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(length)
        turtle.left(72)
    turtle.end_fill()

#Define a function to draw a pentagon
#Define a function to draw curve
def curve():
    turtle.speed(20)
    for i in range(200):
        # Defining step by step curve motion
        turtle.right(1)
        turtle.forward(1)

def draw_heart(color):
    turtle.speed(20)
    turtle.fillcolor(color)
    turtle.begin_fill()
    # Draw the left line
    turtle.left(140)
    turtle.forward(113)
    # Draw curve
    curve()
    turtle.left(120)
    # Draw curve
    curve()
    # Draw the right line
    turtle.forward(112)
    turtle.end_fill()

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
