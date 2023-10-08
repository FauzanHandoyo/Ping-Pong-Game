from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.message = ""
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(0, 100)
        self.write(self.message, align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        if self.l_score == 7:
            self.message = "Left Paddle Wins!"
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        if self.r_score == 7:
            self.message = "right Paddle Wins!"
        self.update_scoreboard()
    
    def reset_score(self):
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_high_score(self, new_high_score):
        self.high_score = new_high_score
        self.update_scoreboard()
    