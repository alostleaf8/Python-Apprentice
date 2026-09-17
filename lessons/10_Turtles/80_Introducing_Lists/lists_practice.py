

angles = [45, 90, 135]
# your code here
import turtle, time

tina = turtle.Turtle()
tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast
time.sleep(1)

forward = 100

for angle in angles:
    tina.left(angle)
    tina.forward(forward)

turtle.exitonclick()