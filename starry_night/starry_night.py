# Import the turtle library as 't' and random functions from the random library
import turtle as t
from random import randint, random

# Define a function to draw a star
# 'points' is the number of points the star will have
# 'size' is how big the star will be
# 'col' is the color of the star
# 'x' and 'y' are the position where the star will be drawn on the screen
def draw_star(points, size, col, x, y):
    # Lift the pen so the turtle can move without drawing
    t.penup()
    # Move the turtle to the (x, y) position
    t.goto(x, y)
    # Put the pen down to start drawing
    t.pendown()
    
    # Calculate the angle to turn the turtle so the points of the star are evenly spaced
    angle = 180 - (180 / points)
    
    # Set the color of the star
    t.color(col)
    
    # Begin filling the star with the chosen color
    t.begin_fill()
    # Loop to draw each point of the star
    for i in range(points):
        # Move the turtle forward by the specified size
        t.forward(size)
        # Turn the turtle to create the next point of the star
        t.right(angle)
    # End filling the star with color
    t.end_fill()

# Main code
# Set the background color of the screen to dark blue
t.Screen().bgcolor('dark blue')

# Use a loop to keep drawing random stars on the screen
while True:
    # Generate a random number of points for the star (always odd, between 5 and 9 points)
    ranPts = randint(2, 5) * 2 + 1
    # Generate a random size for the star (between 10 and 50 units)
    ranSize = randint(10, 50)
    # Generate a random color for the star (using RGB values between 0 and 1)
    ranCol = (random(), random(), random())
    # Generate random x and y positions on the screen for the star
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    
    # Call the draw_star function to draw the star with the random values
    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
