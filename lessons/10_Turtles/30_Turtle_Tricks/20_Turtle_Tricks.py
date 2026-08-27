"""
# 20_Turtle_Tricks.py

In this assignment, you will use Tina the Turtle to draw a pentagon. 

- Each side of the pentagon should be a different color. 
- Use the turtle commands: tina.forward(), tina.left(), and tina.pencolor() to accomplish this.

Refer to the previous program, Meet_Tina.py, for examples of how to use turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtlethe turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

... # Your code here
tina.forward(108)
tina.pencolor('red')
tina.left(72)
tina.pencolor('blue') 
tina.forward(108)
tina.pencolor('green')
tina.left(72)
tina.forward(108)
tina.pencolor('purple')
tina.left(72) 
tina.forward(108) 
tina.pencolor('pink')
tina.left(72)
tina.forward(108)
turtle.exitonclick()                    # Close the window when we click on it