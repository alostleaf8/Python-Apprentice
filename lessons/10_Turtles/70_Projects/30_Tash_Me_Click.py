"""
# 30_Tash_Me_Click.py

Copy your old 20_Tash_Me.py code here and update the program to put the moustache where you click on the screen.

Hint: See 10_More_Turtle_Programs, section 'Respond to Screen Clicks'
"""
 
... # Your code here

import turtle, time

time.sleep(1)

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

set_turtle_image(t, "moustache1.gif")



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


screen = turtle.Screen()                    # Get the screen that t is on
set_background_image(screen, "emoji.png")   # Set the background image of the screen

t.pencolor('red')
def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    t.goto(x, y) # Move the turtle to the clicked location
  
screen.onclick(screen_clicked) # Important! Tell Python which function to use when the screen is clicked

turtle.done()