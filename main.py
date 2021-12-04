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

pygame.display.update()
clock = pygame.time.Clock()
finished = False
bottom_pressed = False
while not finished and bottom_pressed == False:
    pygame.display.update()
    for event in pygame.event.get():
        StartDisplay(screen, event, SIZE)
'''

Считываем файлы с параметрами змейки, стен и змеек - еды
'''
main_snake = read_main_snake_data_from_file('main_snake.txt')
walls = read_wall_data_from_file('walls.txt')
food = read_food_data_from_file('food.txt')

'''

Рисуем начальные положения всех объектов

Из всех змеек-еды выбираем одну с помощью рандома
'''
for wall in walls:
    DrawWall(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end, wall.color, screen)

food_number = randint(0, len(food) - 1)
DrawSnake(food[food_number].coordinates, food[food_number].color, food[food_number].head_color, screen)

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
        food[food_number].turn(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end)

    '''
    
    Рисуем змейку-еду
    '''
    DrawSnake(food[food_number].coordinates, food[food_number].color, food[food_number].head_color, screen)

    '''
    
    Проверяем, скушала ли змея еду
    
    Если да, то создаётся новая еда, а змейка вырастает на одну ячейку
    '''
    if main_snake.collision(food[food_number].coordinates) == 1:
        l = len(main_snake.coordinates)
        x_end = main_snake.coordinates[l - 1][0]
        y_end = main_snake.coordinates[l - 1][0]
        main_snake.elongation(x_end, y_end)
        score += 1
        food_number = randint(0, len(food) - 1)

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
    food[food_number].move_miss = (food[food_number].move_miss + 1) % (food[food_number].miss + 1)
    if food[food_number].move_miss == food[food_number].miss:
        food[food_number].move_tail()
        food[food_number].move_head(food[food_number].direction)

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
            letter = Alphabet(event)
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
