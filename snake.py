"""
Juego de Snake

"""
"""
Juego de Snake

"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 10)
snake = [vector(0, 10)]
aim = vector(0, -10)
color = randrange(1,3)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    aux = 0

    if -180 < head.x < 190:
        aux = aux + 1
    
    if -200 < head.y < 190:
        aux = aux + 1
    
    if aux == 2:
        return True

def switch_side(head):
    if head.x < -200:
        head.x = head.x + 390 
    if head.x > 190:
        head.x = head.x - 390
    if head.y < -200:
        head.y = head.y + 390  
    if head.y > 190:
        head.y = head.y - 390  

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if  head in snake or not inside(head):
        square(head.x, head.y, 9, 'red')
        update()
        return

    if not inside(head):
        switch_side(head)

    if not inside(food):
        switch_side(food)

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    wall_a = square(-250, 180, 200,'black')
    wall_b = square(40, 180, 200,'black')
    wall_c = square(40, -370, 200,'black')
    wall_d = square(-250, -370, 200,'black')
    wall_e = square(-380, 100, 200,'black')
    wall_f = square(-380, -280, 200,'black')
    wall_h = square(170, -280, 200,'black')
    wall_i = square(170, 100, 200,'black')

    center_a = square(0,0,30,'black')
    center_b = square(-30,0,30,'black')
    center_c = square(-40,0,30,'black')
    center_d = square(30,0,30,'black')
    center_e = square(-70,0,30,'black')

    if color == 1:
        for body in snake:
            square(body.x, body.y, 9, 'orange')
    elif color == 2:
        for body in snake:
            square(body.x, body.y, 9, 'blue')
    else:
        for body in snake:
            square(body.x, body.y, 9, 'black')

    if len(snake) % 2 == 0:
        food.x = food.x + 10
    else:
        food.y = food.y + 10 
        
    square(food.x, food.y, 9, 'green')
    
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()