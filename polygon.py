from turtle import *
screen = Screen()
screen.bgcolor("black")
pen = Turtle()
pen.speed(0)
pen.color("blue")
pen.ht()

def polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.fd(200/sides)
        turtle.rt(360/sides)
    turtle.end_fill()
    
name = Turtle()
name.speed(0)
name.color("blue")
name.ht()

while True:    
    sides = int(input("how many sides "))
    pen.clear()
    if sides == 3:
        polygon(pen, sides)
        name.write("triangle"),
    if sides == 4:
        print("Quadrilateral")
    parallel = input("How many pairs of parallel sides? (0, 1, 2): ")
    if parallel == "0":
        print("Irregular quadrilateral")
        t.penup()
        t.goto(-50, 50)
        t.pendown()
        t.begin_fill()
        t.forward(120)
        t.right(80)
        t.forward(90)
        t.right(40)
        t.forward(110)
        t.end_fill()
        name.penup()
        name.goto(0, 150)
        name.write("IRREGULAR QUADRILATERAL", font=("Times New Roman", 20))
    elif parallel == "1":
        print("Trapezoid")
        t.penup()
        t.goto(-50, 50)
        t.pendown()
        t.begin_fill()
        t.forward(120)
        t.right(60)
        t.forward(80)
        t.right(120)
        t.forward(200)
        t.end_fill()
        name.penup()
        name.goto(0, 150)
        name.write("TRAPEZOID", font=("Times New Roman", 20))
    elif parallel == "2":
        angles = input("Are all angles equal? (yes/no): ").lower()
        sides_equal = input("Are all sides equal? (yes/no): ").lower()
        if sides_equal == "yes" and angles == "yes":
            print("Square")
            t.penup()
            t.goto(-50, 50)
            t.pendown()
            draw_polygon(4, 100)
            name.penup()
            name.goto(0, 150)
            name.write("SQUARE", font=("Times New Roman", 20))
        elif angles == "yes" and sides_equal == "no":
            print("Rectangle")
            t.penup()
            t.goto(-50, 50)
            t.pendown()
            t.begin_fill()
            t.forward(150)
            t.right(90)
            t.forward(80)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(80)
            t.end_fill()
            name.penup()
            name.goto(0, 150)
            name.write("RECTANGLE", font=("Times New Roman", 20))
        else:
            print("Parallelogram")
            t.penup()
            t.goto(-50, 50)
            t.pendown()
            t.begin_fill()
            t.forward(120)
            t.right(60)
            t.forward(80)
            t.right(120)
            t.forward(120)
            t.right(60)
            t.forward(80)
            t.end_fill()
            name.penup()
            name.goto(0, 150)
            name.write("PARALLELOGRAM", font=("Times New Roman", 20))
    else:
        print("Invalid input")
    if sides == 5:
        polygon(pen, sides)
        name.write("pentagon"),
    if sides == 6:
        polygon(pen, sides)
        name.write("hexagon"),  
    if sides == 7:
        polygon(pen, sides)
        name.write("heptagon"),
    if sides == 8:
        polygon(pen, sides)
        name.write("octogon"),
    if sides == 9:
        polygon(pen, sides)
        name.write("nonagon"),
    if sides == 10:
        polygon(pen, sides)
        name.write("decagon"),     



screen.exitonclick()
