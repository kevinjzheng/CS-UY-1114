#Problem 4

import turtle
sides = int(input("Please enter the number of sides on your polygon: "))
sumAngle = (sides - 2) * 180
angle = sumAngle/sides
for i in range(sides):
    turtle.forward(100)
    turtle.right(180-angle)
turtle.done()
turtle.hideturtle()
