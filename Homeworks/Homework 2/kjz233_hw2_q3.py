#Problem 3: Given sides and an angle in between calculate the third side and then make a turtle print the resulting triangle
import math
import turtle

#inputs
side1 = int(input("Please enter the length of side 1: "))
side2 = int(input("Please enter the length of side 2: "))
angle1 = int(input("Please enter the angle in between these two sides: "))

#calculations ( math.cos() takes radians!!!!! )
angle2Rad = math.radians(angle1)
side3 = math.sqrt(side1**2 + side2**2 - 2*side1*side2*(math.cos(angle2Rad)))
angle2 = math.degrees(math.acos( (side2**2 + side3**2 - side1**2) / (2*side2*side3) ))

#turtle movements
turtle.forward(side1)
turtle.left(180 - angle1)
turtle.forward(side2)
turtle.left(180 - angle2)
turtle.forward(side3)
turtle.hideturtle()
turtle.done()

