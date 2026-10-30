# def sumTo(n):
#     total = n * (n + 1) / 2
#     return total
#
# print(sumTo(10))
#
# n = int(input("Enter a number: "))
# print(sumTo(n))
# import turtle
#
#
# def drawstar(t,n,size):
#     angle = 180 - 180 /n
#     for i in range(n):
#         t.fd(size)
#         t.rt(angle)
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
# drawstar(t,23,100) :


# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
#
# print(sumTo(10))
#
# n = int(input("Enter a number: "))
# print(sumTo(n))

import math
import turtle


# def mysqrt(x):
#     guess = x / 2
#     for i in range(20):
#         guess = (1 / 2)  * (guess + x / guess)
#     return guess
#
# n = int(input("Enter a number: "))
# print(mysqrt(n))

# import turtle
#
# def drawsprite(someturtle,legs,length):
#     angle = 360/legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
#
# def fancysquare(t,size):
#     for corner in range(4):
#         drawsprite(t,8,20)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.pencolor("red")
# t.pensize(2)
# t.speed(100)
#
# fancysquare(t, 100)
#
#
#
#
# wn.exitonclick()

# import turtle
#
# def drawTip(t,size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size/2)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size/2)
#     t.right(90)
#     t.end_fill()
#
# def drawspritewithtips(someturtle ,legs,legth):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(legth)
#         drawTip(someturtle,10)
#         someturtle.backward(legth)
#         someturtle.left(angle)
#
# def fancysquare(t,size):
#     for corner in range(4):
#         drawspritewithtips(t,8,20)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("blue")
# t = turtle.Turtle()
# t.pensize(2)
# t.speed(100)
#
#
# fancysquare(t, 100)
# wn.exitonclick()

# def checksign(n):
#     if n > 0:
#         return "positive"
#     elif n < 0:
#         return "negative"
#     else:
#          return "zero"
#
# num_list = [-7,5,0]
#
# for num in num_list:
#     print(checksign(num))
#
# n = int(input("Enter a number: "))
# print(checksign(n))


# import turtle
#
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.write("" + str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barchart(data):
#     maxheight = max(data)
#     num_bars = len(data)
#
#     border = 10
#     gap = (maxheight - border) /25
#
#     wn = turtle.screen()
#     wn.bgcolor("lightgreen")
#     right = 48 * num_bars + border
#     top = maxheight + 4 * border
#
#
#     wn.setworldcoordinates(-border,-border,right,top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.fillcolor("blue")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#         wn.
#
#
#
