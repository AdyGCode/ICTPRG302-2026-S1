import turtle

my_turtle = turtle.Turtle()

my_turtle.clear()
my_turtle.home()
my_turtle.pendown()

count = 0
steps = 90
while count < steps:
    my_turtle.forward(2)
    my_turtle.right(360 / steps)
    

pause = input("press enter to finish")