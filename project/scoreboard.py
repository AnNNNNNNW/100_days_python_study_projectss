from turtle import Turtle

score = 1
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.current_score = score
        self.write(f"Score: {self.current_score}", FONT)
        
    
    def score_increas(self):
        self.clear()
        self.current_score += 1
        self.write(f"Score: {self.current_score}", FONT)
        
