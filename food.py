from turtle import Turtle,Screen
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.goto_random_position()

    def goto_random_position(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

