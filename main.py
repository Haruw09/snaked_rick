import random

import pygame
from random import randint

import input
import model_objects as mo
import vis
import time
import control

pygame.init()


'''
Цвета
'''
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
AQUAMARINE = (127, 255, 212)
YELLOW_GREEN = (154, 205, 50)

WIDTH = 41
HEIGHT = 41
SIZE = vis.SIZE

screen = pygame.display.set_mode((WIDTH * SIZE, HEIGHT * SIZE))
game = mo.GameManager(WIDTH, HEIGHT, screen)
'''
Задаём параметры экрана
'''



pygame.display.update()
clock = pygame.time.Clock()

game.start_display_1()

finished = False
result = 0
while not finished and result == 0:
    pygame.display.update()
    for event in pygame.event.get():
        vis.draw_choice_display(screen, event, SIZE)
        result = control.ChoiceDisplay(event, SIZE)
        finished = control.update(event)

if result == 1:
    FPS = 10
    score_for_food = 1
elif result == 2:
    FPS = 20
    score_for_food = 2
elif result == 3:
    FPS = 30
    score_for_food = 3

'''
Считываем файлы с параметрами змейки, стен и змеек - еды
'''
main_snake = input.read_main_snake_data('other\\main_snake.txt')
food = input.read_food_data('other\\food.txt')

'''
Рисуем начальные положения всех объектов
Из всех змеек-еды выбираем одну с помощью рандома
'''
for wall in game.walls:
    vis.draw_wall(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end, wall.color, screen)

live_food = [0] * game.number_of_food
for num in range(game.number_of_food):
    flag = 0
    while flag == 0:
        live_food[num] = randint(0, len(food) - 1)
        x = food[live_food[num]].coordinates[0][0]
        y = food[live_food[num]].coordinates[0][1]
        for wall in game.walls:
            if not (wall.x_begin <= x <= wall.x_end and wall.y_begin <= y <= wall.y_end):
                flag = 1
        for another_num in range(num):
            if live_food[another_num] == live_food[num]:
                flag = 0

    vis.draw_snake(food[num].coordinates, food[num].color, food[num].head_color, screen)

vis.draw_snake(main_snake.coordinates, main_snake.color, main_snake.head_color, screen)
vis.draw_field(screen, SIZE)

'''
Тут мы начинаем гонять нашу игру, пока змея не врежется в стену или не укусит сама себя
'''
rnd = random.randint(1, 3)
if rnd == 1:
    pygame.mixer.music.load('music\\breaktime.mp3')
    pygame.mixer.music.play(-1)
elif rnd == 2:
    pygame.mixer.music.load('music\\carefree.mp3')
    pygame.mixer.music.play(-1)
elif rnd == 3:
    pygame.mixer.music.load('music\\fretless.mp3')
    pygame.mixer.music.play(-1)

while not finished and main_snake.death == 0:
    clock.tick(FPS)
    '''
    Создаём чистый экран
    '''
    pygame.display.update()
    screen.fill(WHITE)
    '''
    Работаем со стенами (С каждой отдельно)
    '''
    for wall in game.walls:
        '''
        Рисуем стену
        '''
        vis.draw_wall(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end, wall.color, screen)
        '''
        Проверяем, ударилась ли главная змея со стеной
        Если да, то главная змея умирает
        '''
        if wall.collision(main_snake.coordinates[0][0], main_snake.coordinates[0][1]):
            main_snake.death = 1
        '''
        Проверяем, дошла ли змея - еда до стены
        Если да, то она развернётся
        '''
        for num in live_food:
            food[num].turn(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end)
    '''
    Рисуем змейку-еду
    '''
    for num in live_food:
        vis.draw_snake(food[num].coordinates, food[num].color, food[num].head_color, screen)
    '''
    Проверяем, скушала ли змея еду
    Если да, то создаётся новая еда, а змейка вырастает на одну ячейку
    '''
    for num in range(game.number_of_food):
        food_number = live_food[num]
        if main_snake.collision(food[food_number].coordinates) == 1:
            l = len(main_snake.coordinates)
            x_end = main_snake.coordinates[l - 1][0]
            y_end = main_snake.coordinates[l - 1][1]
            main_snake.elongation(x_end, y_end)
            score += score_for_food
            flag = 0
            while flag == 0:
                live_food[num] = randint(0, len(food) - 1)
                x = food[live_food[num]].coordinates[0][0]
                y = food[live_food[num]].coordinates[0][1]
                for wall in walls:
                    if not (wall.x_begin <= x <= wall.x_end and wall.y_begin <= y <= wall.y_end):
                        flag = 1
                for another_num in range(num):
                    if live_food[another_num] == live_food[num]:
                        flag = 0
    '''
    Проверяем, не укусила ли змея сама себя
    Если да, то змея умирает
    '''
    if main_snake.collision(main_snake.coordinates) == 0:
        main_snake.death = 1
    '''
    Рисуем змею
    '''
    vis.draw_snake(main_snake.coordinates, main_snake.color, main_snake.head_color, screen)
    '''
    Проверяем нажатые клавиши
    Если нажата клавиша w, a, s или d, то змея поворачивается в нужном направлении
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            main_snake.veer()
        finished = control.update(event)
    '''
    Двигаем змею
    Сначала хвост, потом голову
    '''
    main_snake.move_tail()
    main_snake.move_head(main_snake.direction)
    '''
    Змея - еда двигается в зависимости от своей скорости
    Еда двигается на клетку каждый 2 ход (food[food_number].miss + 1)
    '''
    for num in live_food:
        food[num].move_miss = (food[num].move_miss + 1) % (food[num].miss + 1)
        if food[num].move_miss == food[num].miss:
            food[num].move_tail()
            food[num].move_head(food[num].direction)
'''
Игра закончилась, подготавливаемся к экрану конца игры
name - это имя, которое введёт пользователь
right_pressed - флаг, который сработает, когда нажмётся стрелочка вправо
'''
right_pressed = False
'''
Экран ввода имени
Работает, пока не нажата стрелочка вправо
'''
pygame.mixer.music.load('music\\fivecardshuffle.mp3')
pygame.mixer.music.play(-1)
while not finished and not right_pressed:
    '''
    Рисуем экран, на котором пишется всякая всячина
    '''
    pygame.display.update()
    screen.fill(WHITE)
    vis.draw_end_display(screen, game.score, game.name, SIZE)
    '''
    Проверяем, нажата ли какая-либо клавиша
    Если нажата, то заставляем функцию alphabet возвращает эту кнопку
    При нажатом BACKSPACE стирается последний символ
    При нажатии правой стрелочки ввод заканчивается 
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            letter = input.alphabet(event, key)
            if letter == 'BACKSPACE':
                name = name[:-1]
            elif letter == 'RIGHT':
                right_pressed = True
            else:
                name += letter
        finished = control.update(event)

game.table_display(game.score, game.name, game.top_number)

pygame.quit()
