from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.dx = 10
        self.dy = 10 #use for collision to wall
        self.moveSpeed = 8

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        print(f"new_x: {new_x}, new_y: {new_y}")

        self.goto(new_x, new_y)    
        
    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.moveSpeed *= 0.4
        
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()   