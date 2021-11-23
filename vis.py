import pygame

import model_objects as mo

SIZE = 20


def DrawSnake(screen, coordinates, color):
    for position in coordinates:
        pygame.draw.rect(screen, color, (position[0] * SIZE, position[1] * SIZE, SIZE, SIZE))


def DrawWall(screen, x_begin, y_begin, x_end, y_end, color):
    pygame.draw.rect(screen, color, (x_begin, y_begin, x_end - x_begin, y_end - y_begin))


def DrawField(screen):
    pygame.draw.rect(screen, mo.BLACK, (0, 0, mo.WIDTH, mo.HEIGHT))
