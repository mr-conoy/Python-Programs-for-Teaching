# Import the random library to use random numbers and turtle as 't' for drawing
import random
import turtle as t

# Function to ask the user for the length of the line
# It returns the length based on their choice
def get_line_length():
    # Ask the user to enter 'long', 'medium', or 'short' for the line length
    choice = input('Enter line length (long, medium, short): ')
    if choice == 'long':
        line_length = 250  # Set the length to 250 for long lines
    elif choice == 'medium':
        line_length = 200  # Set the length to 200 for medium lines
    else:
        line_length = 100  # Set the length to 100 for short lines
    return line_length  # Return the chosen line length

# Function to ask the user for the thickness of the line
# It returns the width based on their choice
def get_line_width():
    # Ask the user to enter 'superthick', 'thick', or 'thin' for the line width
    choice = input('Enter line width (superthick, thick, thin): ')
    if choice == 'superthick':
        line_width = 40  # Set the width to 40 for super thick lines
    elif choice == 'thick':
        line_width = 25  # Set the width to 25 for thick lines
    else:
        line_width = 10  # Set the width to 10 for thin lines
    return line_width  # Return the chosen line width

# Function to check if the turtle is still inside the window boundaries
def inside_window():
    # Define the limits of the window for left, right, top, and bottom
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    # Get the current position of the turtle
    (x, y) = t.pos()
    # Check if the turtle's position is inside the window
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside  # Return True if inside the window, False if not

# Function to move the turtle and draw lines
def move_turtle(line_length):
    # List of colors the turtle can use to draw lines
    pen_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    # Set the turtle's pen color to a random color from the list
    t.pencolor(random.choice(pen_colors))
    # Check if the turtle is still inside the window
    if inside_window():
        # If inside the window, turn the turtle by a random angle and move forward
        angle = random.randint(0, 180)
        t.right(angle)
        t.forward(line_length)
    else:
        # If the turtle is outside the window, move backward to stay inside
        t.backward(line_length)

# Ask the user for the line length and line width, using the functions we created
line_length = get_line_length()
line_width = get_line_width()

# Set up the turtle's appearance and drawing speed
t.shape('turtle')  # Make the turtle look like a turtle
t.fillcolor('green')  # Set the turtle's fill color to green
t.bgcolor('black')  # Set the background color to black
t.speed('fastest')  # Make the turtle draw as fast as possible
t.pensize(line_width)  # Set the pen size to the user's chosen line width

# Start drawing! The turtle will keep moving and drawing lines forever (until you stop the program)
while True:
    move_turtle(line_length)  # Call the move_turtle function to draw lines
