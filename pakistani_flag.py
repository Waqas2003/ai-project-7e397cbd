import turtle

def draw_rectangle(color, width, height):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_crescent(color, radius, angle):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius, angle)
    turtle.end_fill()

def draw_star(color, radius, points):
    angle = 180 - (180 / points)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(points):
        turtle.forward(radius)
        turtle.right(angle)
    turtle.end_fill()

def draw_pakistani_flag():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()

    # Draw green portion
    draw_rectangle("green", 400, 200)

    # Draw white crescent
    turtle.penup()
    turtle.goto(-120, 50)
    turtle.pendown()
    draw_crescent("white", 100, 180)

    # Draw white star
    turtle.penup()
    turtle.goto(-100, 50)
    turtle.pendown()
    draw_star("white", 20, 5)

    turtle.done()

draw_pakistani_flag()