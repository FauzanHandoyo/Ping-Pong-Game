from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)
    
    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:  # Adjust this limit as needed
            self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -240:  # Adjust this limit as needed
            self.sety(new_y)
    
    