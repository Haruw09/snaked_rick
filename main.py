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

game.play_display()
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
