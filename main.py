import pygame
from random import randint

from input import *
from model_objects import *
from vis import *
import time

'''

Параметры игры (ФПС - влияет на скорость игры, начальное кол-во очков (Почти всегда это 0))
'''
FPS = 30
score = 0
number_of_food = 3

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

'''

Параметры экрана (Ширина, Высота и масштаб, т.е. кол-во пикселей в одном игровом квадратике)
'''
WIDTH = 41
HEIGHT = 41
SIZE = 20

'''

Задаём параметры экрана
'''
screen = pygame.display.set_mode((WIDTH * SIZE, HEIGHT * SIZE))


def StartDisplay(event, size):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if size * mo.HEIGHT / 3 <= event.pos[1] <= 11 * size * mo.WIDTH / 24:
            if size * mo.WIDTH / 7 <= event.pos[0] <= 2 * size * mo.WIDTH / 7:
                return 1
            elif size * 28 * mo.WIDTH / 70 <= event.pos[0] <= size * mo.WIDTH * 43 / 70:
                return 2
            elif size * 5 / 7 * mo.WIDTH <= event.pos[0] <= size * 6 / 7 * mo.WIDTH:
                return 3
    return 0


def ChoiceDisplay(event, size):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if size / 3 * mo.WIDTH <= event.pos[0] <= 2 * size / 3 * mo.WIDTH:
            if size * mo.HEIGHT / 7 <= event.pos[1] <= 2 * size * mo.HEIGHT / 7:
                return 1
            elif 3 * size * mo.HEIGHT / 7 <= event.pos[1] <= 4 * size * mo.HEIGHT / 7:
                return 2
            elif 5 * size * mo.HEIGHT / 7 <= event.pos[1] <= 6 * size * mo.HEIGHT / 7:
                return 3
    return 0


pygame.display.update()
clock = pygame.time.Clock()
screen_number = 1
finished = False
result = 0
# while not finished:
# if screen_number == 1:

while not finished and result == 0:
    pygame.display.update()
    for event in pygame.event.get():
        DrawStartDisplay(screen, event, SIZE)
        result = StartDisplay(event, SIZE)

if result == 1:
    walls = read_wall_data_from_file('Lvl_1.txt')
elif result == 2:
    walls = read_wall_data_from_file('Lvl_2.txt')
elif result == 3:
    walls = read_wall_data_from_file('Lvl_3.txt')

result = 0
while not finished and result == 0:
    pygame.display.update()
    for event in pygame.event.get():
        DrawChoiceDisplay(screen, event, SIZE)
        result = ChoiceDisplay(event, SIZE)
if result == 1:
    FPS = 10
elif result == 2:
    FPS = 20
elif result == 3:
    FPS = 30

'''

Считываем файлы с параметрами змейки, стен и змеек - еды
'''
main_snake = read_main_snake_data_from_file('main_snake.txt')
food = read_food_data_from_file('food.txt')

'''

Рисуем начальные положения всех объектов

Из всех змеек-еды выбираем одну с помощью рандома
'''
for wall in walls:
    DrawWall(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end, wall.color, screen)

live_food = [0] * number_of_food
for num in range(number_of_food):
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

    DrawSnake(food[num].coordinates, food[num].color, food[num].head_color, screen)

DrawSnake(main_snake.coordinates, main_snake.color, main_snake.head_color, screen)
DrawField(screen)

'''

Тут мы начинаем гонять нашу игру, пока змея не врежится в стену или не укусит сама себя
'''

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
    for wall in walls:
        '''
        
        Рисуем стену
        '''
        DrawWall(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end, wall.color, screen)
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
        DrawSnake(food[num].coordinates, food[num].color, food[num].head_color, screen)

    '''
    
    Проверяем, скушала ли змея еду
    
    Если да, то создаётся новая еда, а змейка вырастает на одну ячейку
    '''
    for num in range(number_of_food):
        food_number = live_food[num]
        if main_snake.collision(food[food_number].coordinates) == 1:
            l = len(main_snake.coordinates)
            x_end = main_snake.coordinates[l - 1][0]
            y_end = main_snake.coordinates[l - 1][1]
            main_snake.elongation(x_end, y_end)
            score += 1

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
    DrawSnake(main_snake.coordinates, main_snake.color, main_snake.head_color, screen)

    '''
    
    Проверяем нажатые клавиши
    
    Если нажата клавиша w, a, s или d, то змея поворачивается в нужном направлении
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            main_snake.veer()

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
finished = False
right_pressed = False
name = ''

'''

Экран ввода имени

Работает, пока не нажата стрелочка вправо
'''
while not finished and not right_pressed:
    '''
    
    Рисуем экран, на котором пишется всякая всячина
    '''
    pygame.display.update()
    screen.fill(WHITE)
    End_game_display(screen, score, name)

    '''
    
    Проверяем, нажата ли какая-либо клавиша
    
    Если нажата, то заставляем функцию Alphabet возвращает эту кнопку
    
    При нажатом BACKSPACE стирается последний символ
    
    При нажатии правой стрелочки ввод заканчивается 
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            letter = Alphabet()
            if letter == 'BACKSPACE':
                name = name[:-1]
            elif letter == 'RIGHT':
                right_pressed = True
            else:
                name += letter

'''

Здесь читается, анализируется, переписывается и записывается обратно в файл таблица лидеров
'''
table = top_entry(score, name)

'''

Здесь игрок модет полубоваться таблицей лидеров

Закрыть окно можно, нажав любую кнопку
'''
bottom_pressed = False
while not finished and not bottom_pressed:
    pygame.display.update()
    screen.fill(WHITE)
    Draw_table(screen, table, table[20])
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            bottom_pressed = True

pygame.quit()
