"""
Copy the code from the previous lesson, 10_More_Turtle_Programs.ipynb,
from the section "Clicking the Turtle Directly"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location

    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
"""

import turtle, random
                                          # Import the turtle module

screen = turtle.Screen()                                    # Set up the screen
screen.setup(width=600, height=600)                         # Set the size of the window
screen.bgcolor('light blue')                                     # Set the background color

t = turtle.Turtle()                                         # Create a turtle
t.shape("turtle")                                           # Set the shape of the turtle
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)     # Make the turtle really big

def turtle_clicked(t, x, y):
    """Function that gets called when the user clicks on the turtle


    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """

    print('turtle clicked!')

    x=random.randint(-300,300)     
    y=random.randint(-300,300)
    print(x,y)
    t.pencolor('red')
    t.goto(x,y)
   
# Connect the turtle to the turtle_clicked function
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open

