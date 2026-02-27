import turtle

my_turtle = turtle.Turtle()

my_turtle.clear()
my_turtle.home()
my_turtle.pendown()

# range(start, end)
# 1) start at 0, end at max repeats
# 2) start at 1, end at max repeats + 1
for count in range(0,4):
    my_turtle.forward(50)
    my_turtle.right(90)

pause = input("press enter to finish")