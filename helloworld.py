from turtle import *
import math
import random

# Name your Turtle.
tom = Turtle()
num_sides = input('Enter your preferred number of sides: ')
sides = int(num_sides)
colors  = ["red","green","blue","orange","purple","pink","yellow"]

# Set Up your screen and starting position.
setup(1000,800)
x_pos = -5
y_pos = 0
tom.setposition(x_pos, y_pos)



### Write
def draw_shapes(num_sides):
    tom.pendown()
    angle = 360 / sides

    for side in range(sides):
        tom.pencolor(random.choice(colors))
        tom.forward(20)
        tom.left(angle)


draw_shapes(sides)
exitonclick()











# Close window on click.
exitonclick()
