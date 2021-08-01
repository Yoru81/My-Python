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

for i in range(4):
    m.forward(51)
    m.right(90)

m.penup()    
m.goto(26, -51 )
m.pendown()
m.right(90)
m.forward(80)
m.right(45)
m.forward(40)
m.goto(26, -131)
m.left(90)
m.forward(40)


wait = input()
