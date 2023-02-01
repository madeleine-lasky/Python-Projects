from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# generates random cars and moves them across the screen
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=2)
        self.setx(320)
        self.sety(random.randint(-250, 250))
        self.setheading(180)

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)









