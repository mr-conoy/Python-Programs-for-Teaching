# Import the turtle library to draw shapes
import turtle as t

# Define a function to draw rectangles
# It takes three inputs: the width (horizontal), height (vertical), and color of the rectangle
def rectangle(horizontal, vertical, color):
    # Put the turtle's pen down to start drawing
    t.pendown()
    # Set the pen size to 1 (so the lines are thin)
    t.pensize(1)
    # Set the pen color for the rectangle
    t.color(color)
    # Start filling the shape with the specified color
    t.begin_fill()
    # Repeat twice to draw the rectangle: two sides are horizontal, two are vertical
    for counter in range(1, 3):
        t.forward(horizontal)  # Move forward by the horizontal length
        t.right(90)            # Turn 90 degrees to the right (to draw the next side)
        t.forward(vertical)    # Move forward by the vertical length
        t.right(90)            # Turn again to complete the rectangle
    # Stop filling the shape with color
    t.end_fill()
    # Lift the pen so the turtle can move without drawing
    t.penup()

# Lift the pen so the turtle can move to the starting position
t.penup()
# Set the drawing speed to slow
t.speed('slow')
# Set the background color to 'Dodger blue' (a shade of blue)
t.bgcolor('Dodger blue')

# Draw the feet
t.goto(-100, -150)           # Move the turtle to the position of the first foot
rectangle(50, 20, 'blue')    # Draw the first foot (50 units wide, 20 units tall, blue color)
t.goto(-30, -150)            # Move to the position of the second foot
rectangle(50, 20, 'blue')    # Draw the second foot

# Draw the legs
t.goto(-25, -50)             # Move to the position of the first leg
rectangle(15, 100, 'grey')   # Draw the first leg (15 units wide, 100 units tall, grey color)
t.goto(-55, -50)             # Move to the position of the second leg
rectangle(-15, 100, 'grey')  # Draw the second leg (mirrored using negative width)

# Draw the body
t.goto(-90, 100)             # Move to the position for the body
rectangle(100, 150, 'red')   # Draw the body (100 units wide, 150 units tall, red color)

# Draw the arms
t.goto(-150, 70)             # Move to the position of the left arm
rectangle(60, 15, 'grey')    # Draw the left arm (60 units wide, 15 units tall, grey color)
t.goto(-150, 110)            # Move to the upper part of the left arm
rectangle(15, 40, 'grey')    # Draw the upper part of the left arm (15 units wide, 40 units tall)

t.goto(10, 70)               # Move to the position of the right arm
rectangle(60, 15, 'grey')    # Draw the right arm
t.goto(55, 110)              # Move to the upper part of the right arm
rectangle(15, 40, 'grey')    # Draw the upper part of the right arm

# Draw the neck
t.goto(-50, 120)             # Move to the position of the neck
rectangle(15, 20, 'grey')    # Draw the neck (15 units wide, 20 units tall)

# Draw the head
t.goto(-85, 170)             # Move to the position of the head
rectangle(80, 50, 'red')     # Draw the head (80 units wide, 50 units tall, red color)

# Draw the eyes
t.goto(-60, 160)             # Move to the position of the left eye
rectangle(30, 10, 'white')   # Draw the white part of the left eye (30 units wide, 10 units tall)
t.goto(-55, 155)             # Move to the position of the left pupil
rectangle(5, 5, 'black')     # Draw the left pupil (5 units wide, 5 units tall, black color)
t.goto(-40, 155)             # Move to the position of the right pupil
rectangle(5, 5, 'black')     # Draw the right pupil

# Draw the mouth
t.goto(-65, 135)             # Move to the position of the mouth
rectangle(40, 5, 'black')    # Draw the mouth (40 units wide, 5 units tall, black color)

# Hide the turtle so the final drawing looks clean
t.hideturtle()
