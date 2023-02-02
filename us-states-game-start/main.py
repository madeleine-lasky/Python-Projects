'''This project implements a States Guessing game. The turtle module
will be used for a GUI interaction with the user. Pandas will also
be used in order to read to and write to csv files. '''
import turtle
import pandas
import time

# Create the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"          # file path to reach the image


# adds the image to the screen
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y, state):
    '''
    Writes the name of the correctly guessed state onto the map.
    :param x: The x-coordinate of the state on the map.
    :param y: The y-coordinate of the state on the map.
    :param state: The name of the correctly guessed state
    :return: None
    '''
    temp_turtle = turtle.Turtle()
    temp_turtle.hideturtle()
    temp_turtle.penup()
    temp_turtle.goto(x = int(x), y = int(y ))
    temp_turtle.write(state, align = "center", font = ("Copperplate",12, "normal"))

total = 0
guesses = f"{total}/50 States Correct"

# create a list of all states in the csv
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []

# Loop until the user has either guessed all states OR opts to exit
while total < 50:
    user_guess = screen.textinput(title=guesses, prompt="What's another state's name?")
    user_guess = str(user_guess).title()
    if user_guess == "Exit":
        break
    if user_guess in states:
        total+= 1
        guessed_states += user_guess
        states.remove(user_guess)
        row = data[data.state == user_guess]
        get_mouse_click_coor(x = row.x, y = row.y, state = user_guess)
        guesses = f"{total}/50 States Correct"
    time.sleep(0.1)

# Store the states in the CSV
data_dict = {"States":[]}
data_dict["States"] += states
df = pandas.DataFrame(data_dict)
df.to_csv("Incorrect_States.csv")
print(f"Total correctly guessed states: {total}")

turtle.mainloop()


