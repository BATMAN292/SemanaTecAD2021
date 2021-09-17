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
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if  head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    if not inside(head):
        if head.x < -200:
            head.x = head.x + 390 
        if head.x > 190:
            head.x = head.x - 390
        if head.y < -200:
            head.y = head.y + 390  
        if head.y > 190:
            head.y = head.y - 390  

    if not inside(food):
        if food.x < -200:
            food.x = food.x + 390 
        if food.x > 190:
            food.x = food.x - 390
        if food.y < -200:
            food.y = food.y + 390  
        if food.y > 190:
            food.y = food.y - 390  

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    if color == 1:
        for body in snake:
            square(body.x, body.y, 9, 'yellow')
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
    ontimer(head.move, 60)
    ontimer(food.move, 60)


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
