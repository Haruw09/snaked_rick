import random

import pygame
from random import randint

import input
import model_objects as mo
import vis
import time
import control

pygame.init()

WIDTH = 41
HEIGHT = 41
SIZE = vis.SIZE
screen = pygame.display.set_mode((WIDTH * SIZE, HEIGHT * SIZE))

pygame.display.update()
clock = pygame.time.Clock()

game = mo.GameManager(WIDTH, HEIGHT, screen, clock)
gameplay = [game.start_display_1, game.start_display_2, game.play_display, game.endgame_display, game.table_display]
for i in range(len(gameplay)):
    if not game.finished:
        gameplay[i]()
pygame.quit()
