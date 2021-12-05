import pygame
import pygame.freetype
import model_objects as mo

pygame.freetype.init()
SIZE = 20


def DrawSnake(coordinates, color, head_color, screen):
    """

    Функция рисует змейку по квадратикам.

    Сначала рисует кадратики по всем координатам змеи, а только потом голову

    coordinates - массив координат змейки

    color - цвет змейки

    head_color - цвет головы змеи

    screen - экран, на котором рисуется змейка
    """
    for position in coordinates:
        pygame.draw.rect(screen, color, (position[0] * SIZE, position[1] * SIZE, SIZE, SIZE))
    pygame.draw.rect(screen, head_color, (coordinates[0][0] * SIZE, coordinates[0][1] * SIZE, SIZE, SIZE))


def DrawWall(x_begin, y_begin, x_end, y_end, color, screen):
    """

    Функция рисует стену

    x_begin, y_begin - координаты левого-верхнего квадратика стены

    x_end, y_end - координаты правого-верхнего квадратика стены
    """
    pygame.draw.rect(screen, color,
                     (x_begin * SIZE, y_begin * SIZE, (x_end - x_begin + 1) * SIZE, (y_end - y_begin + 1) * SIZE))


def DrawField(screen):
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH, mo.HEIGHT))


def End_game_display(screen, score, name):
    """

    Функция рисует экран, после проигрыша игры, на котором происходит ввод имени игрока

    screen - экран, на котором всё пишется

    score - счёт игрока

    name - имя игрока
    """
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH, mo.HEIGHT))
    my_font = pygame.freetype.Font('comic.ttf', 45)

    text_game_over, rect = my_font.render("GAME OVER. YOUR SCORE IS ", mo.BLACK)
    screen.blit(text_game_over, (10, 10))

    text_score, rect = my_font.render(str(score), mo.BLACK)
    screen.blit(text_score, (680, 10))

    text_write_name, rect = my_font.render('WRITE YOUR NAME', mo.BLACK)
    screen.blit(text_write_name, (10, 70))

    text_name, rect = my_font.render(str(name), mo.BLACK)
    screen.blit(text_name, (500, 70))

    text_press_right, rect = my_font.render('PRESS --> TO CONTINUE', mo.BLACK)
    screen.blit(text_press_right, (10, 130))


def DrawStartDisplay(screen, event, size):
    screen.fill(mo.WHITE)
    head_font = pygame.freetype.Font("COOPBL.TTF", 60)
    head, rect = head_font.render("Snaked Rick", mo.BLACK)
    screen.blit(head, (size * 9 * mo.WIDTH / 30, size * mo.HEIGHT / 20))
    pygame.draw.rect(screen, mo.AQUAMARINE,
                     (size * mo.WIDTH / 7, size * mo.HEIGHT / 3, size * mo.WIDTH / 7, size * mo.HEIGHT / 8))
    pygame.draw.rect(screen, mo.YELLOW,
                     (size * 28 * mo.WIDTH / 70, size * mo.HEIGHT / 3, size * 15 * mo.WIDTH / 70, size * mo.HEIGHT / 8))
    pygame.draw.rect(screen, mo.RED,
                     (size * 5 * mo.WIDTH / 7, size * mo.HEIGHT / 3, size * mo.WIDTH / 7, size * mo.HEIGHT / 8))
    pygame.draw.circle(screen, mo.YELLOW_GREEN, (15 * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                       size * mo.HEIGHT / 10)
    pygame.draw.circle(screen, mo.YELLOW_GREEN, (35 * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                       size * mo.HEIGHT / 10)
    pygame.draw.circle(screen, mo.YELLOW_GREEN, (55 * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                       size * mo.HEIGHT / 10)

    my_font = pygame.freetype.Font('comic.ttf', 40)
    easy, rect, = my_font.render("EASY", mo.BLACK)
    screen.blit(easy, (size * 105 * mo.WIDTH / 700, 11 * size * mo.HEIGHT / 30))
    medium, rect = my_font.render("MEDIUM", mo.BLACK)
    screen.blit(medium, (size * 281 * mo.WIDTH / 700, 11 * size * mo.HEIGHT / 30))
    hard, rect = my_font.render("HARD", mo.BLACK)
    my_font = pygame.freetype.Font('comic.ttf', 35)
    screen.blit(hard, (size * 503 * mo.WIDTH / 700, 11 * size * mo.HEIGHT / 30))
    table, rect = my_font.render("Table of")
    screen.blit(table, (size * 95 * mo.WIDTH / 700, 185 * size * mo.HEIGHT / 300))
    screen.blit(table, (size * 295 * mo.WIDTH / 700, 185 * size * mo.HEIGHT / 300))
    screen.blit(table, (size * 495 * mo.WIDTH / 700, 185 * size * mo.HEIGHT / 300))
    table, rect = my_font.render("LEVEL 1")
    screen.blit(table, (size * 95 * mo.WIDTH / 700, 205 * size * mo.HEIGHT / 300))
    table, rect = my_font.render("LEVEL 2")
    screen.blit(table, (size * 295 * mo.WIDTH / 700, 205 * size * mo.HEIGHT / 300))
    table, rect = my_font.render("LEVEL 3")
    screen.blit(table, (size * 495 * mo.WIDTH / 700, 205 * size * mo.HEIGHT / 300))

    text_font = pygame.freetype.Font('comic.ttf', 50)
    text, rect = text_font.render("Choose your difficulty level")
    screen.blit(text, (size * 8 * mo.WIDTH / 70, 7 * size * mo.HEIGHT / 15))
    text, rect = text_font.render("Table of results")
    screen.blit(text, (size * 18 * mo.WIDTH / 70, 12 * size * mo.HEIGHT / 15))
    description, rect = text_font.render("Eat all the Morties")
    screen.blit(description, (size * 18 * mo.WIDTH / 70, 8 * size * mo.HEIGHT / 60))
    description, rect = text_font.render("or they'll eat you")
    screen.blit(description, (size * 20 * mo.WIDTH / 70, 1 * size * mo.HEIGHT / 5))
    if event.type == pygame.MOUSEMOTION:
        if size * mo.HEIGHT / 3 <= event.pos[1] <= 11 * size * mo.WIDTH / 24:
            if size * mo.WIDTH / 7 <= event.pos[0] <= 2 * size * mo.WIDTH / 7:
                pygame.draw.rect(screen, mo.BLACK,
                                 (size * mo.WIDTH / 7, size * mo.HEIGHT / 3, size * mo.WIDTH / 7, size * mo.HEIGHT / 8),
                                 2)
            elif size * 28 * mo.WIDTH / 70 <= event.pos[0] <= size * mo.WIDTH * 43 / 70:
                pygame.draw.rect(screen, mo.BLACK,
                                 (size * 28 * mo.WIDTH / 70, size * mo.HEIGHT / 3, size * 15 * mo.WIDTH / 70,
                                  size * mo.HEIGHT / 8), 2)
            elif size * 5 / 7 * mo.WIDTH <= event.pos[0] <= size * 6 / 7 * mo.WIDTH:
                pygame.draw.rect(screen, mo.BLACK,
                                 (size * 5 * mo.WIDTH / 7, size * mo.HEIGHT / 3, size * mo.WIDTH / 7,
                                  size * mo.HEIGHT / 8), 2)
        if (event.pos[0] - size * 15 * mo.WIDTH / 70) ** 2 + (event.pos[1] - size * 2 * mo.HEIGHT / 3) ** 2 <= (
                size * mo.HEIGHT / 10) ** 2:
            pygame.draw.circle(screen, mo.BLACK, (15 * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                               size * mo.HEIGHT / 10, 2)
        elif (event.pos[0] - size * 35 * mo.WIDTH / 70) ** 2 + (event.pos[1] - size * 2 * mo.HEIGHT / 3) ** 2 <= (
                size * mo.HEIGHT / 10) ** 2:
            pygame.draw.circle(screen, mo.BLACK, (35 * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                               size * mo.HEIGHT / 10, 2)
        elif (event.pos[0] - size * 55 * mo.WIDTH / 70) ** 2 + (event.pos[1] - size * 2 * mo.HEIGHT / 3) ** 2 <= (
                size * mo.HEIGHT / 10) ** 2:
            pygame.draw.circle(screen, mo.BLACK, (55 * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                               size * mo.HEIGHT / 10, 2)


def DrawChoiceDisplay(screen, event, size):
    screen.fill(mo.WHITE)
    pygame.draw.rect(screen, mo.ORANGE,
                     (size / 3 * mo.WIDTH, size * mo.HEIGHT / 7, size / 3 * mo.WIDTH, size * mo.HEIGHT / 7))
    pygame.draw.rect(screen, mo.ORANGE,
                     (size / 3 * mo.WIDTH, 3 * size * mo.HEIGHT / 7, size / 3 * mo.WIDTH, size * mo.HEIGHT / 7))
    pygame.draw.rect(screen, mo.ORANGE,
                     (size / 3 * mo.WIDTH, 5 * size * mo.HEIGHT / 7, size / 3 * mo.WIDTH, size * mo.HEIGHT / 7))
    my_font = pygame.freetype.Font('comic.ttf', 45)
    level, rect = my_font.render("LEVEL 1", mo.BLACK)
    screen.blit(level, (size * 24 * mo.WIDTH / 60, 13 * size * mo.HEIGHT / 70))
    level, rect = my_font.render("LEVEL 2", mo.BLACK)
    screen.blit(level, (size * 24 * mo.WIDTH / 60, 33 * size * mo.HEIGHT / 70))
    level, rect = my_font.render("LEVEL 3", mo.BLACK)
    screen.blit(level, (size * 24 * mo.WIDTH / 60, 53 * size * mo.HEIGHT / 70))



def Draw_table(screen, table, place):
    """

    Рисуем экран с таблицей лидеров

    Так же на экране пишется, какое место в таблице занял игрок

    Если игрок не занял никакого места, то пишем другую фразу

    screen - экран

    table - массив с очками и именами игроков

    place - место игрока в этой таблице
    """
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH, mo.HEIGHT))
    my_font = pygame.freetype.Font('comic.ttf', 45)

    if place <= 10:
        text_congratulations, rect = my_font.render("CONGRATULATIONS!", mo.BLACK)
        screen.blit(text_congratulations, (10, 10))

        text_your_place, rect = my_font.render("YOUR PLACE IS ", mo.BLACK)
        screen.blit(text_your_place, (10, 60))

        text_place, rect = my_font.render(str(place), mo.BLACK)
        screen.blit(text_place, (400, 60))
    else:
        text_not_in_the_top, rect = my_font.render("YOU'RE TOO BAD!", mo.BLACK)
        screen.blit(text_not_in_the_top, (10, 10))

        text_try_again, rect = my_font.render("TRY AGAIN", mo.BLACK)
        screen.blit(text_try_again, (10, 60))

    for i in range(0, 10):
        text_score, rect = my_font.render(str(table[2 * i]), mo.BLACK)
        screen.blit(text_score, (10, 150 + i * 50))

        text_name, rect = my_font.render(str(table[2 * i + 1]), mo.BLACK)
        screen.blit(text_name, (150, 150 + i * 50))

    text_press_any_key, rect = my_font.render("PRESS ANY KEY TO EXIT", mo.BLACK)
    screen.blit(text_press_any_key, (10, 750))


def Alphabet():
    """

    Функция преобразует нажатие клавиши в символ, соответствующий этой клавише

    Функция возвращает символ, соответсвующий нажатой клавише
    """
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        return 'A'
    if pressed[pygame.K_b]:
        return 'B'
    if pressed[pygame.K_c]:
        return 'C'
    if pressed[pygame.K_d]:
        return 'D'
    if pressed[pygame.K_e]:
        return 'E'
    if pressed[pygame.K_f]:
        return 'F'
    if pressed[pygame.K_g]:
        return 'G'
    if pressed[pygame.K_h]:
        return 'H'
    if pressed[pygame.K_i]:
        return 'I'
    if pressed[pygame.K_j]:
        return 'J'
    if pressed[pygame.K_k]:
        return 'K'
    if pressed[pygame.K_l]:
        return 'L'
    if pressed[pygame.K_m]:
        return 'M'
    if pressed[pygame.K_n]:
        return 'N'
    if pressed[pygame.K_o]:
        return 'O'
    if pressed[pygame.K_p]:
        return 'P'
    if pressed[pygame.K_q]:
        return 'Q'
    if pressed[pygame.K_r]:
        return 'R'
    if pressed[pygame.K_s]:
        return 'S'
    if pressed[pygame.K_t]:
        return 'T'
    if pressed[pygame.K_u]:
        return 'U'
    if pressed[pygame.K_v]:
        return 'V'
    if pressed[pygame.K_w]:
        return 'W'
    if pressed[pygame.K_x]:
        return 'X'
    if pressed[pygame.K_y]:
        return 'Y'
    if pressed[pygame.K_z]:
        return 'Z'
    if pressed[pygame.K_0]:
        return '0'
    if pressed[pygame.K_1]:
        return '1'
    if pressed[pygame.K_2]:
        return '2'
    if pressed[pygame.K_3]:
        return '3'
    if pressed[pygame.K_4]:
        return '4'
    if pressed[pygame.K_5]:
        return '5'
    if pressed[pygame.K_6]:
        return '6'
    if pressed[pygame.K_7]:
        return '7'
    if pressed[pygame.K_8]:
        return '8'
    if pressed[pygame.K_9]:
        return '9'
    if pressed[pygame.K_BACKSPACE]:
        return 'BACKSPACE'
    if pressed[pygame.K_RIGHT]:
        return 'RIGHT'
    return ''
