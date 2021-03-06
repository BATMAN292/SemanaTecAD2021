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

"valores de inicio"
ball = vector(0, 0)
ball2 = vector(10, 10)
aim = vector(value(), value())
"aim2 = vector(value(), value())"
state = {1: 0, 2: 0}

"Color de los rectángulos"
c = randrange(1,4)
if c==1:
    col='red'
elif c==2:
    col='blue'
elif c==3:
    col='pink'
elif c==4:
    col='black'

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

    "Crear 2 pelotas (aún no funciona)"
    ball.move(aim)
    x = ball.x
    y = ball.y

    ball2.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    dot(10)
    dot(10)
    update()

    "Rebote de la pelota"
    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    "Velocidad del juego"
    ontimer(draw, 60)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

"Teclas utilizadas para el movimiento de las barras"
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
draw()
done()
