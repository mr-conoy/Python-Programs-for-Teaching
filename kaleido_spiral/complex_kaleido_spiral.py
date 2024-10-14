# Import the turtle library and itertools to cycle through colors
import turtle
from itertools import cycle

# Create a cycle of colors that the turtles will use when drawing
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# Define the function to draw a circle with four turtles moving in opposite directions
# 'size' is the radius of the circle
# 'angle' is the angle the turtles turn after drawing the circle
# 'shift' is how far the turtles move before drawing the next circle
# 'max_size' is the largest size the circles can get
def draw_circle(pen1, pen2, pen3, pen4, size, angle, shift, max_size):
    # Stop drawing if the size of the circle is bigger than the max size
    if size > max_size:  
        return
    
    # Change the pen color to the next one in the list of colors
    pen1.pencolor(next(colors))
    pen2.pencolor(next(colors))
    pen3.pencolor(next(colors))
    pen4.pencolor(next(colors))

    # Draw a circle with the given size for all pens
    pen1.circle(size)
    pen2.circle(size)
    pen3.circle(size)
    pen4.circle(size)

    # Turn the turtles by the specified angle in opposite directions
    pen1.right(angle)
    pen2.right(angle)
    pen3.right(angle)
    pen4.right(angle)

    # Move the turtles forward by the specified shift distance
    pen1.forward(shift)
    pen2.forward(shift)
    pen3.forward(shift)
    pen4.forward(shift)

    # Call the function again (this is recursion), with the size, angle, and shift getting a bit bigger each time
    draw_circle(pen1, pen2, pen3, pen4, size + 5, angle + 1, shift + 1, max_size)

# Create screen object
screen = turtle.Screen()
screen.bgcolor('black')

# Create four turtle pens
pen1 = turtle.Turtle()  # This pen will go north
pen2 = turtle.Turtle()  # This pen will go east
pen3 = turtle.Turtle()  # This pen will go south
pen4 = turtle.Turtle()  # This pen will go west

# Set the drawing speed to fast
pen1.speed('fastest')
pen2.speed('fastest')
pen3.speed('fastest')
pen4.speed('fastest')

# Set the size of the pens
pen1.pensize(4)
pen2.pensize(4)
pen3.pensize(4)
pen4.pensize(4)

# Set the initial positions and headings of the turtles so they start from the same origin, but face different directions
pen1.penup()
pen1.goto(0, 0)  # Start at the origin
pen1.setheading(90)  # Pointing north
pen1.pendown()

pen2.penup()
pen2.goto(0, 0)  # Start at the origin
pen2.setheading(0)  # Pointing east
pen2.pendown()

pen3.penup()
pen3.goto(0, 0)  # Start at the origin
pen3.setheading(270)  # Pointing south
pen3.pendown()

pen4.penup()
pen4.goto(0, 0)  # Start at the origin
pen4.setheading(180)  # Pointing west
pen4.pendown()

# Start drawing circles with the four pens, with an initial size of 30, no initial angle, a small shift, and a maximum size of 200
draw_circle(pen1, pen2, pen3, pen4, 30, 0, 1, 200)

# Finish the drawing and keep the window open until the user closes it
turtle.done()
