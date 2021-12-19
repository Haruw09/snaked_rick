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

pygame.display.update()
clock = pygame.time.Clock()
game = mo.GameManager(WIDTH, HEIGHT, screen, clock)
game.start_display_1()
game.start_display_2()
game.play_display()
game.endgame_display()
game.table_display()
pygame.quit()
