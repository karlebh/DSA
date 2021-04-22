from turtle import Turtle

myTurtle = Turtle()
window = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
	if lineLen > 0:
		myTurtle.forward(lineLen)
		myTurtle.right(90)
		drawSpiral(myTurtle, lineLen - 5)

drawSpiral(myTurtle, 100)
window.exitonclick()
