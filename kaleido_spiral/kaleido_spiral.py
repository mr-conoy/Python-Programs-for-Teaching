# Import the turtle library to draw, and itertools to cycle through colors
import turtle
from itertools import cycle

# Create a cycle of colors that the turtle will use when drawing
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# Define the function to draw a circle
# 'size' is the radius of the circle
# 'angle' is the angle the turtle turns after drawing the circle
# 'shift' is how far the turtle moves before drawing the next circle
# 'max_size' is the largest size the circles can get
def draw_circle(size, angle, shift, max_size):
    # Stop drawing if the size of the circle is bigger than the max size
    if size > max_size:  
        return
    # Change the pen color to the next one in the list of colors
    turtle.pencolor(next(colors))
    # Draw a circle with the given size
    turtle.circle(size)
    # Turn the turtle by the specified angle
    turtle.right(angle)
    # Move the turtle forward by the specified shift distance
    turtle.forward(shift)
    # Call the function again (this is recursion), with the size, angle, and shift getting a bit bigger each time
    draw_circle(size + 5, angle + 1, shift + 1, max_size)  

# Set the background color to black
turtle.bgcolor('black')
# Set the drawing speed to fast
turtle.speed('fast')
# Set the size of the pen that draws the circles
turtle.pensize(4)

# Start drawing circles with an initial size of 30, no initial angle, a small shift, and a maximum size of 200
draw_circle(30, 0, 1, 200)  

# Finish the drawing and keep the window open until the user closes it
turtle.done()
