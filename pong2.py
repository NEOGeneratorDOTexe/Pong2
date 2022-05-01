# Author: Benjamin Appelberg
# University: Uppsala Universitet
# import required library "turtle". turtle is a lightweight library for coding simple games
# Copyright (c) 2022 Benjamin Appelberg, Stockholm.
# All Rights Reserved.

# import required module
from playsound import playsound

import turtle
import player

# create screen object from the imported turtle library
screen = turtle.Screen()
screen.title("Pong v.2 by Benjamin Appelberg")
screen.bgcolor("white")
screen.setup(width=800, height=600)

#
p1 = player.Player(screen.textinput("Start setting 1/2", "Enter name of BLUE player: "), 0)

p2 = player.Player(screen.textinput("Start setting 2/2", "Enter name of RED player: "), 0)

# create [left] paddle rectangle with desired attributes
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# create [right] paddle rectangle with desired attributes
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# create match ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# initialize scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()  # hide pointer/drawer
scoreboard.goto(0, 260)
scoreboard.write("{}: {}    {}: {}".format(p1.name, p1.score, p2.name, p2.score), align="center",
                 font=("Arial", 24, "bold"))


# vertical functions to move paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)


# key-bindings
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

blue_setting_board = turtle.Turtle()
blue_setting_board.speed(0)
blue_setting_board.color("blue")
blue_setting_board.penup()
blue_setting_board.hideturtle()  # hide pointer/drawer
blue_setting_board.goto(-300, -260)
blue_setting_board.write("Blue controls: \n w = Up\n s = Down" "", align="center",
                         font=("Arial", 11, "italic"))

red_setting_board = turtle.Turtle()
red_setting_board.speed(0)
red_setting_board.color("red")
red_setting_board.penup()
red_setting_board.hideturtle()  # hide pointer/drawer
red_setting_board.goto(300, -260)
red_setting_board.write("Red controls: \n ↑ = Up \n  ↓ = Down" "", align="center",
                        font=("Arial", 11, "italic"))

# while program is running, update the turtle_screen_object.
while True:
    screen.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border top hit
    if ball.ycor() > 280:
        print('ball hits TOP-border')
        ball.sety(280)
        ball.dy *= -1

    # border bottom hit
    if ball.ycor() < -280:
        print('ball hits BOTTOM-border')
        ball.sety(-280)
        ball.dy *= -1

    # paddle a scores
    if ball.xcor() > 380:
        p1.score += 1
        print(p1.name, "has scored! Current scoreboard: ", p1.name, ": ", p1.score, " ", p2.name, ": ", p2.score)
        ball.goto(0, 0)  # reset ball back to origo
        ball.dx *= -1
        # clear scoreboard text and then write  new score
        scoreboard.clear()
        scoreboard.write("{}: {}    {}: {}".format(p1.name, p1.score, p2.name, p2.score), align="center",
                         font=("Arial", 24, "bold"))

    # paddle b scores
    if ball.xcor() < -380:
        p2.score += 1
        print(p2.name, "has scored! Current score: ", p2.score)
        ball.goto(0, 0)  # reset ball to origo
        ball.dx *= -1
        # clear scoreboard text and then write  new score
        scoreboard.clear()
        scoreboard.write("{}: {}    {}: {}".format(p1.name, p1.score, p2.name, p2.score), align="center",
                         font=("Arial", 24, "bold"))

    ''' paddle and ball collisions '''
    # paddle_a hit ball
    if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() + 70 > ball.ycor() > paddle_a.ycor() - 70):
        print(p1.name, "hits the ball...")
        ball.setx(-340)
        ball.dx *= -1

    # paddle_b hit ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_b.ycor() + 70 > ball.ycor() > paddle_b.ycor() - 70):
        print(p2.name, "hits the ball...")
        ball.setx(340)
        ball.dx *= -1