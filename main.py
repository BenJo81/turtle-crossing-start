import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create a turtle player that starts at the bottom of the screen and listen for the "Up"
# keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.

# I am adding a comment
screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
