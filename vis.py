import pygame
import pygame.freetype
import model_objects as mo

pygame.freetype.init()
SIZE = 20


def DrawSnake(coordinates, color, head_color, screen):
    for position in coordinates:
        pygame.draw.rect(screen, color, (position[0] * SIZE, position[1] * SIZE, SIZE, SIZE))
    pygame.draw.rect(screen, head_color, (coordinates[0][0] * SIZE, coordinates[0][1] * SIZE, SIZE, SIZE))


def DrawWall(x_begin, y_begin, x_end, y_end, color, screen):
    pygame.draw.rect(screen, color,
                     (x_begin * SIZE, y_begin * SIZE, (x_end - x_begin + 1) * SIZE, (y_end - y_begin + 1) * SIZE))


def DrawField(screen):
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH, mo.HEIGHT))


def End_game_display(screen, score, name):
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH, mo.HEIGHT))
    my_font = pygame.freetype.Font('comic.ttf', 50)
    text_letters, rect = my_font.render("GAME OVER. YOUR SCORE IS ", mo.BLACK)
    screen.blit(text_letters, (10, 10))

    text_score, rect = my_font.render(str(score), mo.RED)
    screen.blit(text_score, (10, 20))


def Alphabet(event):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        return 'a'
    if pressed[pygame.K_b]:
        return 'b'
    if pressed[pygame.K_c]:
        return 'c'
    if pressed[pygame.K_d]:
        return 'd'
    if pressed[pygame.K_e]:
        return 'e'
    if pressed[pygame.K_f]:
        return 'f'
    if pressed[pygame.K_g]:
        return 'g'
    if pressed[pygame.K_h]:
        return 'h'
    if pressed[pygame.K_i]:
        return 'i'
    if pressed[pygame.K_j]:
        return 'j'
    if pressed[pygame.K_k]:
        return 'k'
    if pressed[pygame.K_l]:
        return 'l'
    if pressed[pygame.K_m]:
        return 'm'
    if pressed[pygame.K_n]:
        return 'n'
    if pressed[pygame.K_o]:
        return 'o'
    if pressed[pygame.K_p]:
        return 'p'
    if pressed[pygame.K_q]:
        return 'q'
    if pressed[pygame.K_r]:
        return 'r'
    if pressed[pygame.K_s]:
        return 's'
    if pressed[pygame.K_t]:
        return 't'
    if pressed[pygame.K_u]:
        return 'u'
    if pressed[pygame.K_v]:
        return 'v'
    if pressed[pygame.K_w]:
        return 'w'
    if pressed[pygame.K_x]:
        return 'x'
    if pressed[pygame.K_y]:
        return 'y'
    if pressed[pygame.K_z]:
        return 'z'
