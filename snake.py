# Juego de SNAKE

# LIBRERIAS

from turtle import update, clear, ontimer, setup, \
    hideturtle, tracer, listen, onkey, done
from random import randrange
from freegames import square, vector


# VARIABLES DE POSICION INICIALES
food = vector(0, 10)
snake = [vector(0, -140)]
aim = vector(0, 10)
color = randrange(1, 3)


# FUNCIONES


def change(x, y):  # Cambia la dirección de la serpiente
    aim.x = x
    aim.y = y


def inside(head):  # Checa que la serpiente este entre los limites
    return -200 < head.x < 190 and -200 < head.y < 190


def switch_side(head):  # Si la serpiente sale de limites cambia al otro lado
    if head.x < -200:
        head.x = head.x + 390
    if head.x > 190:
        head.x = head.x - 390
    if head.y < -200:
        head.y = head.y + 390
    if head.y > 190:
        head.y = head.y - 390


def obstacles(head):  # Define los espacios en los que no se puede estar
    if head.x < -50 and head.y < -170:
        return False
    if head.x > 30 and head.y < -170:
        return False
    if head.x < -50 and head.y > 170:
        return False
    if head.x > 30 and head.y > 170:
        return False
    if head.x < -180 and head.y > 90:
        return False
    if head.x < -180 and head.y < -80:
        return False
    if head.x > 160 and head.y > 90:
        return False
    if head.x > 160 and head.y < -80:
        return False
    if -80 < head.x < 70 and -10 < head.y < 40:
        return False
    else:
        return True


def move():  # Funcion principal del programa
    head = snake[-1].copy()
    head.move(aim)

    if head in snake or not obstacles(head):
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

    square(-250, 180, 200, 'black')
    square(40, 180, 200, 'black')
    square(40, -370, 200, 'black')
    square(-250, -370, 200, 'black')
    square(-380, 100, 200, 'black')
    square(-380, -280, 200, 'black')
    square(170, -280, 200, 'black')
    square(170, 100, 200, 'black')

    square(0, 0, 40, 'black')
    square(-30, 0, 40, 'black')
    square(-40, 0, 40, 'black')
    square(30, 0, 40, 'black')
    square(-70, 0, 40, 'black')

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


# GAME SETUP


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
