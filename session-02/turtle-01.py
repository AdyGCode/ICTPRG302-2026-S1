# Drawing a square
#
# Using Python's turtle this program will draw a square
#
# Author: Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
#

# Import the Turtle module
import turtle

# create a turtle to be controlled
my_turtle = turtle.Turtle()

# change the turtle colour and line thickness
my_turtle.color("hotpink", "purple")
my_turtle.pensize(6)

# Ask the turtle to draw a square
my_turtle.begin_fill()
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.end_fill()
