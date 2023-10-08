from turtle import Screen, Turtle
from movement import Paddle
from ball import Ball
from scoreboard import Scoreboard
import keyboard
import time
import mainMenu

screen = Screen()
screen.setup(width=800, height=600)


screen.tracer(0)  # Turn off animation
DELAY_FACTOR = 0.04
ball = Ball()
score_board = Scoreboard()



# Create two paddle instances with different positions
paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))


GameIsNotOver = True
while GameIsNotOver:
    
    screen.update()
    ball.move()

    screen.listen()
    if keyboard.is_pressed("w"):
        paddle1.move_up()
    if keyboard.is_pressed("s"):
        paddle1.move_down()
    if keyboard.is_pressed("Up"):
        paddle2.move_up()
    if keyboard.is_pressed("Down"):
        paddle2.move_down()
    

    # Ball bounce with paddles
    if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        DELAY_FACTOR *= 0.9 

    time.sleep(DELAY_FACTOR)

    # Ball bounce with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()


    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()
        DELAY_FACTOR = 0.04

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()
        DELAY_FACTOR = 0.04
    
    if score_board.l_score >= 7 or score_board.r_score >= 7:
        score_board.reset_score()
        break

    if score_board.l_score == 7:
        high_score = max(high_score, score_board.l_score)
        score_board.update_high_score(high_score)

    if score_board.r_score == 7:
        high_score = max(high_score, score_board.r_score)
        score_board.update_high_score(high_score)

screen.exitonclick()
