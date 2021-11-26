import pygame

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

WIDTH = 41
HEIGHT = 41
SIZE = 20


def veer(event):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        if abs(main_snake.coordinates[0][1] - main_snake.coordinates[1][1]) != 1:
            main_snake.direction = 'w'

    if pressed[pygame.K_s]:
        if abs(main_snake.coordinates[0][1] - main_snake.coordinates[1][1]) != 1:
            main_snake.direction = 's'

    if pressed[pygame.K_a]:
        if abs(main_snake.coordinates[0][0] - main_snake.coordinates[1][0]) != 1:
            main_snake.direction = 'a'

    if pressed[pygame.K_d]:
        if abs(main_snake.coordinates[0][0] - main_snake.coordinates[1][0]) != 1:
            main_snake.direction = 'd'


screen = pygame.display.set_mode((WIDTH * SIZE, HEIGHT * SIZE))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

main_snake = read_main_snake_data_from_file('main_snake.txt')
walls = read_wall_data_from_file('walls.txt')

for wall in walls:
    DrawWall(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end, wall.color, screen)
DrawSnake(main_snake.coordinates, main_snake.color, screen)
DrawField(screen)

while not finished:
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(WHITE)
    for wall in walls:
        DrawWall(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end, wall.color, screen)
    DrawSnake(main_snake.coordinates, main_snake.color, screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            veer(event)

    main_snake.move_tail()
    main_snake.move_head(main_snake.direction)

pygame.quit()