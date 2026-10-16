# import random
#
# for i in range(10):
#     print(random.random())
import turtle


# import random
#
# for i in range(10):
#     print(random.randint(25,35))

# import math
#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
#
# c = math.hypot(a,b)
#
#
# print(c)

# import math
#
# def area0fcircle(r):
#     area = math.pi * r**2
#     return area
#
# print(area0fcircle(1))

# import turtle
#
# def drawStar(t,side):
#     for i in range(5):
#         t.fd(side)
#         t.rt(144)
#
# test=turtle.Turtle()
# screen=turtle.Screen()
#
# drawStar(test,200)
#
# screen.exitonclick()

def drawsquare(t, side):
    for i in range(4):
        t.forward(side)
        t.left(90)

# import turtle
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.pensize(3)
#
# for i in range(4):
#     drawsquare(tess, 20)
#
# screen.exitonclick()

# import turtle
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.pensize(3)
#
# for i in range(20,120,20):
#     drawsquare(tess, i)
#     tess.penup()
#     tess.backward(10)
#     tess.right(90)
#     tess.forward(10)
#     tess.left(90)
#     tess.pendown()


