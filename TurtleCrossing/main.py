import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from gametitle import GameIcon

# Define the Screen
screen = Screen()
screen.bgcolor("white")
screen.setup(width = 600, height = 600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
score.display_home_screen()
screen.onkey(key="Up", fun=player.move_up)

# statements within will be updated every 0.1 seconds
def play_game():
    screen.onkey(key="Down", fun=None)

    game_is_on = True
    game_loop = 0
    list_of_cars = []
    time_speed = 0.1

    score.next_level()

    while game_is_on:
        game_loop += 1

        if game_loop == 1:
            list_of_cars.append(CarManager())
        elif game_loop == 6:
            game_loop = 0

        # move the cars
        if len(list_of_cars) > 0:
            for car in list_of_cars:
                car.move_car()
                if player.distance(car) < 45:
                    score.display_game_over()
                    player.hideturtle()
                    for item in list_of_cars:
                        item.hideturtle()

                    game_is_on = False

        # Detect if player has reached the end
        if player.reached_finish_line():
            player.reset()
            score.next_level()
            time_speed *= 0.9

        time.sleep(time_speed)
        screen.update()


screen.onkey(key = "Down", fun = play_game)
screen.exitonclick()

