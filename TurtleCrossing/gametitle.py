from turtle import Turtle

class GameIcon(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(0, -100)
        self.setheading(90)
        self.shapesize(stretch_wid=5, stretch_len=5)
        self.showturtle()

    def delete_icon(self):
        self.clear()

    def game_over_icon(self):
        self.shape("turtle")
        self.color("black")
        self.goto(0, -100)
        self.showturtle()
        self.setheading(270)
        self.shapesize(stretch_wid=2, stretch_len=2)
