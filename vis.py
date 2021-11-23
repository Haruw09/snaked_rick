import pygame

import model_objects as mo

SIZE = 20


def DrawSnake(screen, coordinates, color):
    for position in coordinates:
        pygame.draw.rect(screen, color, (position[0] * SIZE, position[1] * SIZE, SIZE, SIZE))


def DrawField(screen):
    pygame.draw.rect(screen, mo.BLACK, (0, 0, mo.WIDTH, mo.HEIGHT))
