from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Turtle controlled across road
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.reset()
        self.shape("turtle")
        self.setheading(90)
        self.pencolor("orange")
        self.fillcolor("green")

    def move_up(self):
        self.forward(10)

    def reset(self):
        self.hideturtle()
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
        self.showturtle()

    def reached_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
