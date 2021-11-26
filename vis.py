import pygame

import model_objects as mo

SIZE = 20


def DrawSnake(coordinates, color, screen):
    for position in coordinates:
        pygame.draw.rect(screen, color, (position[0] * SIZE, position[1] * SIZE, SIZE, SIZE))


def DrawWall(x_begin, y_begin, x_end, y_end, color, screen):
    pygame.draw.rect(screen, color,
                     (x_begin * SIZE, y_begin * SIZE, (x_end - x_begin + 1) * SIZE, (y_end - y_begin + 1) * SIZE))


def DrawField(screen):
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH, mo.HEIGHT))
