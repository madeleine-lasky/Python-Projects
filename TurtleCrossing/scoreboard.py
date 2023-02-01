from turtle import Turtle
BIG_FONT = ("Copperplate", 30, "bold")
SMALL_FONT = ("Copperplate", 14, "normal")

# writes level we are on as well as the game over sequence
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0

    def next_level(self):
        self.clear()
        self.hideturtle()
        self.update_level()
        self.color("black")
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align = "center", font = BIG_FONT)

    def update_level(self):
        self.level += 1

    def display_game_over(self):
        self.home()
        self.write(f"GAME OVER", align = "center", font = BIG_FONT)
        self.goto(0, -20)
        self.shapesize(stretch_wid= 1, stretch_len=1)
        self.setheading(90)
        self.stamp()

    def display_home_screen(self):
        self.clear()
        self.home()
        self.write(f"TURTLE CROSSING", align = "center", font = BIG_FONT)
        self.goto(0, -150)
        self.write(f"PRESS DOWN KEY TO BEGIN", align = "center", font = SMALL_FONT)
        self.goto(0, -75)
        self.shape("turtle")
        self.color("green")
        self.shapesize(stretch_wid= 2, stretch_len= 2)
        self.setheading(90)
        self.stamp()

    def reset(self):
        self.level = 0
        self.next_level()









