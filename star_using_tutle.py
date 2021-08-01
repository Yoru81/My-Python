import turtle
import random
import time

colorlist = ["cyan" , "red" , "white"]

# window & setup
window = turtle.Screen()
window.setup(width=1200, height=600)
window.bgcolor("black")
window.title("Star(turtle)")

# obj def
m = turtle.Turtle() 
m.color(random.choice(colorlist))
m.shape("turtle")


m.penup()

# border
m.speed(10)
m.pensize(10)
m.goto(-590, 290)
m.pendown()
m.goto(-590, -290)
m.goto(590, -290)
m.goto(590, 290)
m.goto(-590, 290)
m.penup()
m.goto(0, 0)

m.pendown()

# star
m.speed(1)
m.pensize(2)
m.left(72)
m.forward(50)
m.goto(30, 0)
m.right(72)
m.forward(50)
m.goto(30, -30)
m.right(72)
m.forward(50)
m.goto(15, -30)
m.right(50)
m.forward(50)
m.goto(0, -30)
m.goto(-45, 0)
m.goto(0, 0)










wait = input()
