#DavidFunctions
import turtle
bob=turtle.Turtle()

def square(distance):
    for times in range(4):
        bob.forward(distance)
        bob.right(90)

def triangle(distance):
    for times in range(3):
        bob.forward(distance)
        bob.right(120)


def polygon(distance,sides,c):
    angle=360/sides
    bob.color(c)
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()
    
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(d)
        bob.right(144)
    bob.end_fill() 

def explosion(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
    bob.end_fill()















    
