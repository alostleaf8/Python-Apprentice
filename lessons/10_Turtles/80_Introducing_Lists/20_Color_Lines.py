"""
# 20_Color_Lines.py

Finish the program to make Tina draw a square with each side being a different color.
"""

import turtle, time                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
time.sleep(1)

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Move at a moderate speed, not too fast.

forward = 100
right = 90
colors = ['hot pink', 'lavender', 'pink', 'purple']    # define a list of colors

for color in colors:                            # loop through the colors
# Your code here
    tina.color(color)
    tina.forward(forward)
    tina.right(right)

# 2) Make another square, but put the colors in reverse order, using a negative index. 

# Your code here
tina.penup()
tina.goto(-100,150)
tina.pendown()
for color in reversed(colors):                            # loop through the colors
    tina.color(color)
    tina.forward(forward)
    tina.right(right)

turtle.exitonclick()                     # Close the window when we click on it