from tkinter import CENTER
from turtle import Turtle




ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")
score = 0
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
            
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_score()
    
    def reset(self):
        if self.score > self.high_score:
            pass
            self.high_score = self.score
            # with open("data.txt", mode="w") as file:
            #     file.write(self.high_score)

        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.color("white")
    #     self.hideturtle()
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("GAME OVER STUPID PLAYER", align = "center", font = ("Arial", 16, "normal"))



    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = "center", font = ("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

  