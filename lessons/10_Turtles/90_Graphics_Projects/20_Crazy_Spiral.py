"""
# 20_Crazy_Spiral.py

Make your own crazy spiral with a pattern like
in 10_Flaming_Ninja_Star.py, but use what you've learned about loops

uid: zfzMbyH7
name: Crazy Spiral
"""
import turtle 

turtle.setup(600, 600, 0, 0)            # Set the size of the window
window = turtle.Screen()

# Copy code to make a turtle and set up the window

tina = turtle.Turtle()      # Create a turtle named tina
tina.shape("circle")        # Make the shape of tina a turtle 
tina.width(5)               # Make the width of tina 5
tina.shapesize(3,3,1)      # Make the size of the cursor bigger 
tina.speed(0)               # Make the speed of the tina that is moving 

# 2) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like

def make_a_shape2(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    f=100
    t.pencolor("#C50303")
    t.begin_fill()
    t.forward(f) 
    t.right(130) 
    t.forward(f) 
    t.left(70) 
    t.forward(f)
    t.goto(0,0) 
    t.end_fill()
    tina.pencolor("#fbb400")
    tina.begin_fill()
    tina.fillcolor("#fbb400")
    tina.end_fill()
    
def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    t.pencolor("#C50303")
    t.begin_fill()
    for triangle in range(3): 
        tina.forward(100)
        tina.right(30) 
    t.goto(0,0) 
    t.end_fill()
    tina.pencolor("#fbb400")
    tina.begin_fill()
    tina.fillcolor("#fbb400")
    tina.end_fill()


# 2: Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make,
# for example 100, or a list of numbers.

num_shapes = 16

for i in range(num_shapes):
    if i%4 == 0:
        tina.fillcolor("#db2a27")
    elif i%4 == 1:
        tina.fillcolor("#fd0905")
    elif i%4 == 2:
        tina.fillcolor("#fc4f4c")
    else:
        tina.fillcolor("#fb8684")   
    make_a_shape(tina)
    tina.right(360/num_shapes)

turtle.done()