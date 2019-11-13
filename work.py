

from CuencaFunctions2 import*

bob.speed(0)

bob.color("dark gray")

bob.begin_fill()


bob.penup()
bob.goto(100,-150)
bob.pendown()

bob.forward(357)
bob.left(90)
bob.forward(58)
bob.left(90)
bob.forward(48)

bob.right(90)
bob.forward(74)
bob.left(90)
bob.forward(38)
bob.left(90)
bob.forward(28)
bob.right(90)
bob.forward(39)
bob.left(90)
bob.forward(32)
bob.right(90)
bob.forward(41)
bob.right(90)
bob.forward(36)
bob.left(90)
bob.forward(24)
bob.right(90)
bob.forward(24)
bob.left(90)
bob.forward(24)
bob.left(90)
bob.forward(26)
bob.right(90)
bob.forward(19)
bob.left(90)
bob.forward(42)
bob.right(90)
bob.forward(19)
bob.right(90)
bob.forward(20)
bob.right(90)
bob.forward(20)
bob.left(90)
bob.forward(19)
bob.left(90)
bob.forward(28)
bob.right(90)
bob.forward(12)
bob.left(90)
bob.forward(16)
bob.right(90)
bob.forward(11)
bob.left(90)
bob.forward(27)
bob.left(90)
bob.forward(19)
bob.right(90)
bob.forward(30)
bob.left(90)
bob.forward(25)
bob.right(90)
bob.forward(30)
bob.left(90)
bob.forward(82)
bob.left(90)

bob.forward(362)
bob.left(90)
bob.forward(58)
bob.end_fill()


bob.end_fill()

bob.penup()
bob.goto(-120,-100)
bob.pendown()

turtle.colormode(255)
turtle.bgcolor(0,0,0)

for times in range(45):
    bob.begin_fill()
    c = (225,255-times*2,0)
    bob.color(c)
    bob.circle(240-times)
    bob.end_fill()


bob.penup()
bob.goto(-500,-150)
bob.pendown()

bob.color("paleturquoise")
bob.begin_fill()
bob.right(90)
bob.forward(975)
bob.right(90)
bob.forward(250)
bob.right(90)
bob.forward(975)
bob.right(250)
bob.end_fill()



