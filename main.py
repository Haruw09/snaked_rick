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

game.start_display_2()

'''
Считываем файлы с параметрами змейки, стен и змеек - еды
'''
game.read_main_snake()
game.read_food()

'''
Рисуем начальные положения всех объектов
Из всех змеек-еды выбираем одну с помощью рандома
'''
game.draw_walls()
for num in range(game.number_of_food):
    game.new_food(num)
game.draw_food()

vis.draw_snake(game.main_snake.coordinates, game.main_snake.color, game.main_snake.head_color, screen)
vis.draw_field(screen, SIZE)

'''
Тут мы начинаем гонять нашу игру, пока змея не врежется в стену или не укусит сама себя
'''
game.choose_music()

finished = False
while not finished and game.main_snake.death == 0:
    clock.tick(game.FPS)
    '''
    Создаём чистый экран
    '''
    pygame.display.update()
    screen.fill(WHITE)
    '''
    Работаем со стенами (С каждой отдельно)
    '''
    game.draw_walls()
    for wall in game.walls:
        '''
        Проверяем, ударилась ли главная змея со стеной
        Если да, то главная змея умирает
        '''
        game.wall_collision(wall)
        '''
        Проверяем, дошла ли змея - еда до стены
        Если да, то она развернётся
        '''
        game.food_turn(wall)
    '''
    Рисуем змейку-еду
    '''
    game.draw_food()
    '''
    Проверяем, скушала ли змея еду
    Если да, то создаётся новая еда, а змейка вырастает на одну ячейку
    '''
    for num in range(game.number_of_food):
        food_number = game.live_food[num]
        if game.main_snake.collision(game.food[food_number].coordinates) == 1:
            l = len(game.main_snake.coordinates)
            x_end = game.main_snake.coordinates[l - 1][0]
            y_end = game.main_snake.coordinates[l - 1][1]
            game.main_snake.elongation(x_end, y_end)
            game.score += game.score_for_food
            flag = 0
            while flag == 0:
                game.live_food[num] = randint(0, len(game.food) - 1)
                x = game.food[game.live_food[num]].coordinates[0][0]
                y = game.food[game.live_food[num]].coordinates[0][1]
                for wall in game.walls:
                    if not (wall.x_begin <= x <= wall.x_end and wall.y_begin <= y <= wall.y_end):
                        flag = 1
                for another_num in range(num):
                    if game.live_food[another_num] == game.live_food[num]:
                        flag = 0
    '''
    Проверяем, не укусила ли змея сама себя
    Если да, то змея умирает
    '''
    if game.main_snake.collision(game.main_snake.coordinates) == 0:
        game.main_snake.death = 1
    '''
    Рисуем змею
    '''
    vis.draw_snake(game.main_snake.coordinates, game.main_snake.color, game.main_snake.head_color, screen)
    '''
    Проверяем нажатые клавиши
    Если нажата клавиша w, a, s или d, то змея поворачивается в нужном направлении
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game.main_snake.veer()
        finished = control.update(event)
    '''
    Двигаем змею
    Сначала хвост, потом голову
    '''
    game.main_snake.move_tail()
    game.main_snake.move_head(game.main_snake.direction)
    '''
    Змея - еда двигается в зависимости от своей скорости
    Еда двигается на клетку каждый 2 ход (game.food[food_number].miss + 1)
    '''
    for num in game.live_food:
        game.food[num].move_miss = (game.food[num].move_miss + 1) % (game.food[num].miss + 1)
        if game.food[num].move_miss == game.food[num].miss:
            game.food[num].move_tail()
            game.food[num].move_head(game.food[num].direction)
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
                game.name = game.name[:-1]
            elif letter == 'RIGHT':
                right_pressed = True
            else:
                game.name += letter
        finished = control.update(event)

game.table_display()

pygame.quit()
