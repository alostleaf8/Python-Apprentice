"""
Copy the code from the previous lesson, 10_More_Turtle_Programs.ipynb,
from the section "Set a Background Picture"

Then change the code so that the turtle uses a different background image
(look in the 'images' directory) and draws a shape on top of it with your turtle.
"""
# Double-click to copy!

import turtle, time

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""
    from pathlib import Path                                        # Import Path from pathlib module
    from PIL import Image                                           # Import Image from PIL (Pillow) library

    image_dir = Path(__file__).parent.parent / "images"                    # Define the directory containing images
    image_path = str(image_dir / image_name)                        # Create the full path to the image file

    image = Image.open(image_path)                                  # Open the image to get its dimensions
    
    window.setup(image.width, image.height, startx=0, starty=0)     # Set window size to image size
    window.bgpic(image_path)                                        # Set the background picture of the window

turtle.setup(width=600, height=600)         # Set the size of the window

tina = turtle.Turtle()                      # Create a turtle named tina
time.sleep(1)
screen = turtle.Screen()                    # Get the screen that tina is on
set_background_image(screen, "emoji.png")   # Set the background image of the screen

tina.penup()
tina.forward(100)
tina.pendown()
tina.pencolor('blue')
tina.left(45)
tina.penup()
tina.forward(45)
tina.left(30)
tina.right(45)
tina.pendown()
tina.fillcolor('lavender')
tina.begin_fill()
tina.circle(60, steps=40)
tina.end_fill()
tina.penup()
tina.left(120)
tina.forward(255)
tina.pendown()
tina.fillcolor('pink')
tina.begin_fill()
tina.circle(60, steps=40)
tina.end_fill()



turtle.exitonclick() 

