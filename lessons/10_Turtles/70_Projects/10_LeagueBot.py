"""
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables.

"""

import turtle, time 

turtle.turtlesize(stretch_wid=10, stretch_len=10)     # Make the turtle 10x10 

time.sleep(1)

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path                            # Import Path from pathlib module
    image_dir = Path(__file__).parent.parent / "images" # Define the directory containing images
    image_path = str(image_dir / image_name)            # Create the full path to the image file

    screen = turtle.getscreen()                     # Get the turtle's screen
    screen.addshape(image_path)                     # Register the image as a shape
    turtle.shape(image_path)                        # Set the turtle's shape to the image

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('light green')

t = turtle.Turtle()

... # Your Code Here
set_turtle_image(t, 'leaguebot_bolt.gif') 

t.pencolor('blue')

for _ in range(6):
    t.forward(100)
    t.right(60)


turtle.done() # Use `done` not `exitonclick` to keep the window open

