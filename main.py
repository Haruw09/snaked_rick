import pygame

import main
from input import *
from model_objects import *
from vis import *
import time

FPS = 30

# Цвета
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D

WIDTH = 40
HEIGHT = 40
SIZE = 20


def veer(event):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        if main_snake.direction != 's':
            main_snake.direction = 'w'

    if pressed[pygame.K_s]:
        if main_snake.direction != 'w':
            main_snake.direction = 's'

    if pressed[pygame.K_a]:
        if main_snake.direction != 'd':
            main_snake.direction = 'a'

    if pressed[pygame.K_d]:
        if main_snake.direction != 'a':
            main_snake.direction = 'd'

#read_main_snake_data_from_file(main_snake.txt)

screen = pygame.display.set_mode((WIDTH * SIZE, HEIGHT * SIZE))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

main_snake = MainSnake([[20, 20], [21, 20], [22, 20], [23, 20], [24, 20], [24, 21], [24, 22], [24, 23]], 's')
draw_main_snake = DrawableSnake(main_snake)
draw_main_snake.DrawSnake(screen)
DrawField(screen)

while not finished:
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(BLACK)
    draw_main_snake.DrawSnake(screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            veer(event)

    main_snake.move_tail()
    main_snake.move_head(main_snake.direction)

    print(main_snake.coordinates)

pygame.quit()