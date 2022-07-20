import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()

player = Player()
car = CarManager()



screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for machine in car.all_cars:
        if machine.distance(player) < 25:
            game_is_on = False
            print("You Kill FUcking Turtle Bastard")


    if player.finish():
        player.start_pos()
        car.speed_up()

        score.score_increas()

screen.exitonclick()