"""
# 30_Loop_with_Turtle.py

In this program, use a loop to draw a regular pentagon (5-sided shape) with Tina the Turtle.

- Review your previous program, 20_Loop_with_Turtle.py, which uses a loop to draw a shape with the turtle module.
- Make sure your code is clear and well-commented.
- Run your program to verify that Tina the Turtle draws a pentagon.

(Hint: You can copy and modify your previous code!)

uid: BpGnQq64
name: Loop With Turtle
"""

... # Your code here
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.pencolor('red')
tina.begin_fill()
tina.fillcolor('orange')
for pent in range(5):
    tina.forward(108)
    tina.left(72)
tina.end_fill()

turtle.exitonclick()