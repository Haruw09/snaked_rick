import pygame
from random import randint

import input
import model_objects as mo
import vis
import time


def StartDisplay(event, size):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if size * mo.HEIGHT / 3 <= event.pos[1] <= 4 * size * mo.HEIGHT / 9:
            if size * 90 * mo.WIDTH / 700 <= event.pos[0] <= size * (9 / 70 + 99 / 500) * mo.WIDTH:
                return 1
            elif size * 290 * mo.WIDTH / 700 <= event.pos[0] <= size * (29 / 70 + 99 / 500) * mo.WIDTH:
                return 2
            elif size * 490 * mo.WIDTH / 700 <= event.pos[0] <= size * (49 / 70 + 99 / 500) * mo.WIDTH:
                return 3
    return 0

def TableButtons(event, size):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (event.pos[0] - size * 15 * mo.WIDTH / 70) ** 2 + (event.pos[1] - size * 2 * mo.HEIGHT / 3) ** 2 <= (
                size * mo.HEIGHT / 10) ** 2:
            return 1
        elif (event.pos[0] - size * 35 * mo.WIDTH / 70) ** 2 + (event.pos[1] - size * 2 * mo.HEIGHT / 3) ** 2 <= (
                size * mo.HEIGHT / 10) ** 2:
            return 2
        elif (event.pos[0] - size * 55 * mo.WIDTH / 70) ** 2 + (event.pos[1] - size * 2 * mo.HEIGHT / 3) ** 2 <= (
                size * mo.HEIGHT / 10) ** 2:
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

def update(event):
    """
    Проверка на закрытие программы
    :param event: пайгеймовский евент
    :return: True если евент был закрытие программы, иначе False
    """
    if event.type == pygame.QUIT:
        return True
    elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
        return True
    else:
        return False