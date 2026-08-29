"""
# 20_Efficient_Turtle.py

In this program, use what you've learned about functions and variables to make a program that can draw a square, pentagon, and hexagon with a single function.

- Create a function that draws a polygon based on the number of sides passed to it as an argument.
- Use variables to calculate the angle needed to turn the turtle based on the number of sides.
- Call the function multiple times with different arguments to draw a square, pentagon, and hexagon.
"""

import turtle                            # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)             # Set the size of the window

tina = turtle.Turtle()                   # Create a turtle named tina

tina.shape('turtle')                     # Set the shape of the turtle to a turtle
tina.speed(2)                            # Move at a moderate speed, not too fast.

def draw_polygon(sides,color):

    angle = 360/sides
    tina.fillcolor(color)  
    tina.begin_fill()                                           # Calculate angle from number of sides

    for i in range(sides):                 # Loop through the number of sides
        tina.forward(45)                              # Move tina forward by the forward distance
        tina.right(angle) 
    tina.end_fill()
                               # Turn tina left by the left turn

draw_polygon(4,'indigo')                        # Draw a square

tina.penup()
tina.right(90)
tina.forward(60)
tina.pendown()                                      # Move tina to another spot on the screen

draw_polygon(5,'red')                        # Draw a pentagon
tina.penup()
tina.right(90)                               # Move tina to another spot on the screen
tina.forward(80)
tina.pendown()                                      

draw_polygon(6,'green')                     # Draw a hexagon
tina.penup()                                   #Move tina to another spot on the screen
tina.right(90)
tina.forward(90)
tina.pendown()                         

draw_polygon(7,'purple')                       # Draw a septagon      

turtle.exitonclick()                     # Close the window when we click on it