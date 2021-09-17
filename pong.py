"""Pong, classic arcade game.
Exercises
1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.
"""

from random import choice, random, randrange
from turtle import *
from freegames import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

ball1 = vector(0, 0)
ball2 = vector(0, 0)
aim1 = vector(value(), value())
aim2 = vector(value(), value())
state = {1: 0, 2: 0}

c = randrange(1,3)
if c==1:
    col='red'
elif c==2:
    col='blue'
elif c==3:
    col='green'

def move(player, change):
    "Move player position by change."
    state[player] += change

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    up()
    goto(x, y)
    down()
    fillcolor(col)
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    "Draw game and move pong ball."
    clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball1.move(aim1)
    x1 = ball1.x
    y1 = ball1.y

    ball2.move(aim2)
    x2 = ball2.x
    y2 = ball2.y

    up()
    goto(x1, y1)
    goto(x2, y2)
    dot(10)
    update()

    if y1 < -200 or y1 > 200:
        aim1.y = -aim1.y

    if x1 < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y1 <= high:
            aim1.x = -aim1.x
        else:
            return

    if x1 > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y1 <= high:
            aim1.x = -aim1.x
        else:
            return

    if y2 < -200 or y2 > 200:
        aim2.y = -aim2.y

    if x2 < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y2 <= high:
            aim2.x = -aim2.x
        else:
            return

    if x2 > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y2 <= high:
            aim2.x = -aim2.x
        else:
            return

    ontimer(draw, 60)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
draw()
done()

