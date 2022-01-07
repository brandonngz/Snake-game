from turtle import Turtle
import random


def coordinates():
    xcor = random.randint(-280, 280)
    ycor = random.randint(-280, 270)
    return xcor, ycor


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed(0)

    def random_food(self):
        x, y = coordinates()
        self.goto(x, y)
