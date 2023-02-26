import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, "Up")
cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_generator()
    cars.move()

    for car in cars.car_list:
        if car.distance(player) < 23:
            score.game_over()
            game_is_on = False
    if player.ycor() > 280:
        score.add_level()
        cars.add_speed()
        player.pos_res()

screen.exitonclick()
