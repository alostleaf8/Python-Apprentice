"""
Copy the code from the previous lesson, 10_More_Turtle_Programs.ipynb,
from the section "Change the Turtle's Image"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern.
"""
import turtle, time


def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path                        # Import Path from pathlib module
    image_dir = Path(__file__).parent.parent / "images"    # Define the directory containing images
    image_path = str(image_dir / image_name)        # Create the full path to the image file

    screen = turtle.getscreen()                     # Get the turtle's screen
    screen.addshape(image_path)                     # Register the image as a shape
    turtle.shape(image_path)                        # Set the turtle's shape to the image

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t, "pikachu.gif")

t.penup()   # Prevent drawing when moving
t.speed(2)  # Set a moderate speed

time.sleep(3)
# Move the turtle to each corner of the screen in a square pattern
for x, y in [(0, -200), (-100, 0), (-100, -200), (0, 0)]:
    t.goto(x, y)

turtle.exitonclick() 
