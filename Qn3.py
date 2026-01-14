import turtle
import math

# [20] Using Python turtle library for graphics
tillu = turtle.Turtle()
tillu.speed(10)       # [8] Controlling turtle speed and screen updates
tillu.hideturtle() 

def i(length, depth):

    # [21] Recursive functions – function calling itself
    if depth == 0:
        # [22] Drawing polygons with turtle (forward())
        tillu.forward(length)
    else:
        # [23] Calculating segment lengths (division of line segments)
        part = length / 3
        i(part, depth - 1)
        
        # [24] Creating equilateral triangles programmatically
        tillu.left(60)
        i(part, depth - 1)

        tillu.right(120)
        i(part, depth - 1)

        tillu.left(60)
        i(part, depth - 1)

def p(sides, length, depth):
    
    # [25] Combining recursion with loops for repeated patterns
    # [26] Loops and iteration for drawing edges
    angle = 360 / sides   # [27] Equilateral polygon angles
    for _ in range(sides):
        i(length, depth)
        tillu.left(angle)

# [28] Taking user input using input()
sides = int(input('Enter the number of sides: '))
length = int(input('Enter the side length: '))
depth = int(input('Enter the recursion depth: '))

# [29] Controlling turtle position without drawing
tillu.penup()
tillu.pendown()
p(sides, length, depth)

turtle.done()

