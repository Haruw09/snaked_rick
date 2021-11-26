import pygame

import model_objects as mo

SIZE = 20


class DrawableSnake:
    def __init__(self, obj):
        self.obj = obj

    def DrawSnake(self, screen):
        object = self.obj
        for position in object.coordinates:
            pygame.draw.rect(screen, object.color, (position[0] * SIZE, position[1] * SIZE, SIZE, SIZE))


class DrawableWall:
    def __init__(self, obj):
        self.obj = obj

    def DrawWall(self, screen):
        object = self.obj
        pygame.draw.rect(screen, object.color,
                         (object.x_begin, object.y_begin, object.x_end - object.x_begin, object.y_end - object.y_begin))


def DrawField(screen):
    pygame.draw.rect(screen, mo.BLACK, (0, 0, mo.WIDTH, mo.HEIGHT))
