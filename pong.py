# My second Pong game
# Author Benjamin Appelberg
# copyright 2022
# all rights reserved
import turtle
''' ###  Screen - Singleton  ######################## '''
wn = turtle.Screen()  # the program canvas. in turtle.py =>  Screen Singleton has 3 class attributes to be assigned to:    _root = None, _canvas = None, _title = _CFG["title"]
wn.title("Pong 2.0 by @bekko && @portofOS")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # this stop the windows for updating, we can speed up our game by updating it ourselves my wn.update method

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation 0 = instant padding 0 sec
paddle_a.shape("square")  # default shape is w= 20px, h= 20px. to animate pong rectangle use shapesize method of the turtle object
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # 5x rectangle on t
paddle_a.penup()  # turtle objects draw lines as they move and we dont need to draw lines
paddle_a.goto(-350, 0)  # x = 0, y = 0 == origo.

# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation 0 = instant padding 0 sec
paddle_b.shape(
    "square")  # default shape is w= 20px, h= 20px. to animate pong rectangle use shapesize method of the turtle object
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # 5x rectangle on t
paddle_b.penup()  # turtle objects draw lines as they move and we dont need to draw lines
paddle_b.goto(350, 0)  # x = 0, y = 0 == origo.
# ball
ball = turtle.Turtle();
ball.speed(0)  # speed of animation 0 = instant padding 0 sec
ball.shape("square")  # default shape is w= 20px, h= 20px. to animate pong rectangle use shapesize method of the turtle object
ball.color("white")
ball.penup()  # turtle objects draw lines as they move and we dont need to draw lines
ball.goto(0, 0)  # x = 0, y = 0 == origo.

# func = piece of a collection of instructions that has been defined for the function.
def move_paddle_a_y_pos():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# keyboard binding turtle module
wn.listen() # listen on keyboard input
wn.onkeypress(move_paddle_a_y_pos(), "w")
# main game loop - '''every game need a main game loop''' --freecodecamp
while True:
    wn.update()  # everytime the loops runs, this object method updates the screen