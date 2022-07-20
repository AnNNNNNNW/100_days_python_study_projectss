from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.position_score_board()
    
    def position_score_board(self):
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def score_left(self):
        self.l_score += 1
        self.position_score_board()

    def score_right(self):
        self.r_score += 1
        self.position_score_board()