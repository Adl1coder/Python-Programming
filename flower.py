import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

colors = ["red", "blue", "green", "yellow", "orange", "purple", "white", "pink", "cyan"]

for _ in range(180):
    t.color(random.choice(colors))
    t.forward(100)
    t.right(45)
    t.forward(50)
    t.right(45)
    t.forward(30)
    t.right(45)
    t.forward(20)
    t.right(45)
    t.forward(10)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.right(20)

wn.exitonclick()
