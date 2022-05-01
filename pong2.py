# Author: Benjamin Appelberg
# University: Uppsala Universitet
# import required library "turtle". turtle is a lightweight library for coding simple games
# Copyright (c) 2022-2080 Benjamin Appelberg, Stockholm.
# All Rights Reserved.
import turtle
import player

# create screen object from the imported turtle library
screen = turtle.Screen()
screen.title("Pong v.2 by Benjamin Appelberg")
screen.bgcolor("white")
screen.setup(width=800, height=600)

p1name = screen.textinput("Start setting 1/2", "Enter name of BLUE player: ")


p1 = player.Player(p1name, 0)

p2name = screen.textinput("Start setting 2/2", "Enter name of RED player: ")


p2 = player.Player(p2name, 0)

# create [left] paddle rectangle with desired attributes
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("blue")
paddle_1.shapesize(stretch_wid=6, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# create [right] paddle rectangle with desired attributes
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=6, stretch_len=1)
paddle_2.penup()
paddle_2.goto(+350, 0)

# create match ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# score-counters for each respective player
left_player_score_number = 0
left_player_score_number = 0

# initialize scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle() # hide pointer/drawer
scoreboard.goto(0, 260)
scoreboard.write("{}: {}    {}: {}".format(p1.name, p1.score, p2.name, p2.score), align="center",
                 font=("Arial", 24, "bold"))
blue_setting_board = turtle.Turtle()
blue_setting_board.speed(0)
blue_setting_board.color("blue")
blue_setting_board.penup()
blue_setting_board.hideturtle() # hide pointer/drawer
blue_setting_board.goto(-300, -260)
blue_setting_board.write("Blue keys: \n w = Up\n s = Down" "", align="center",
                        font=("Arial", 11, "italic"))

blue_setting_board = turtle.Turtle()
blue_setting_board.speed(0)
blue_setting_board.color("red")
blue_setting_board.penup()
blue_setting_board.hideturtle() # hide pointer/drawer
blue_setting_board.goto(300, -260)
blue_setting_board.write("Red keys: \n ↑ = Up \n  ↓ = Down" "", align="center",
                        font=("Arial", 11, "italic"))

# vertical function moves for both paddles
def paddle_left_up():
    y = paddle_1.ycor()
    y += 40
    paddle_1.sety(y)


def paddle_left_down():
    y = paddle_1.ycor()
    y -= 40
    paddle_1.sety(y)


def paddle_right_up():
    y = paddle_2.ycor()
    y += 40
    paddle_2.sety(y)


def paddle_right_down():
    y = paddle_2.ycor()
    y -= 40
    paddle_2.sety(y)


# key-bindings
screen.listen()
screen.onkeypress(paddle_left_up, "w")
screen.onkeypress(paddle_left_down, "s")
screen.onkeypress(paddle_right_up, "Up")
screen.onkeypress(paddle_right_down, "Down")

# while program is running, update the turtle_screen_object.
while True:
    screen.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    # TODO: fix name attribute copy this: scoreboard.write("{}: {} {}: {}".format(p1.name, p1.score, p2.name, p2.score), align="center", font=("Courier", 20, "normal"))
    #left and right
    if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50):
        p1.score += 1
        scoreboard.clear()
        scoreboard.write("{}: {} {}: {}".format(p1.name, p1.score, p2.name, p2.score), align="center", font=("Courier", 20, "normal"))
    if ball.xcor() > 380:
        score_a = 0
        scoreboard.clear()
        scoreboard.write("Player A: {} Player B: {}".format(p1.score, p2.score), align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1


    if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50):
        p2.score += 1
        scoreboard.clear()
        scoreboard.write("Player A: {} Player B: {}".format(p1.score, p2.score), align="center", font=("Courier", 20, "normal"))
    if ball.xcor() < -380:
        p2.score = 0
        scoreboard.clear()
        scoreboard.write("Player A: {} Player B: {}".format(p1.score, p2.score), align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1


    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1