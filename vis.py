import pygame
import pygame.freetype
import model_objects as mo

pygame.freetype.init()
SIZE = 15


def draw_image(name, size, scale, screen, bottom_right_x, bottom_right_y, width, height):
    surface = pygame.image.load(name)
    surface = pygame.transform.scale(surface, ((int(surface.get_width() * scale * size / 20),
                                                int(surface.get_height() * scale * size / 20))))
    rectangle = surface.get_rect(bottomright=(size * bottom_right_x * width, size * bottom_right_y * height))
    screen.blit(surface, rectangle)


def draw_snake(coordinates, color, head_color, screen):
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


def draw_wall(x_begin, y_begin, x_end, y_end, color, screen):
    """

    Функция рисует стену

    x_begin, y_begin - координаты левого-верхнего квадратика стены

    x_end, y_end - координаты правого-верхнего квадратика стены
    """
    pygame.draw.rect(screen, color,
                     (x_begin * SIZE, y_begin * SIZE, (x_end - x_begin + 1) * SIZE, (y_end - y_begin + 1) * SIZE))


def draw_field(screen):
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH, mo.HEIGHT))


def draw_end_display(screen, score, name, size):
    """

    Функция рисует экран, после проигрыша игры, на котором происходит ввод имени игрока

    screen - экран, на котором всё пишется

    score - счёт игрока

    name - имя игрока
    """
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH, mo.HEIGHT))
    my_font = pygame.freetype.Font('fonts\\comic.ttf', 45 * size / 20)

    text_game_over, rect = my_font.render("Game over. Your score is ", mo.BLACK)
    screen.blit(text_game_over, (10 * size / 20, 10 * size / 20))

    text_score, rect = my_font.render(str(score), mo.BLACK)
    screen.blit(text_score, (545 * size / 20, 10 * size / 20))

    text_write_name, rect = my_font.render('Write your name: ', mo.BLACK)
    screen.blit(text_write_name, (10 * size / 20, 70 * size / 20))

    text_name, rect = my_font.render(str(name), mo.BLACK)
    screen.blit(text_name, (400 * size / 20, 70 * size / 20))

    text_press_right, rect = my_font.render('Press key "->" to continue', mo.BLACK)
    screen.blit(text_press_right, (10 * size / 20, 130 * size / 20))
    draw_image('images\\end.png', size, 1, screen, 1.06, 75 / 80, mo.WIDTH, mo.HEIGHT)


def draw_start_display(screen, event, size):
    screen.fill(mo.WHITE)
    head_font = pygame.freetype.Font("fonts\\COOPBL.TTF", 60 * size / 20)
    head, rect = head_font.render("Snaked Rick", mo.BLACK)
    screen.blit(head, (size * 9 * mo.WIDTH / 30, size * mo.HEIGHT / 20))
    pygame.draw.rect(screen, mo.ORANGE,
                     (size * 90 * mo.WIDTH / 700, size * mo.HEIGHT / 3, size * 99 * mo.WIDTH / 500,
                      size * mo.HEIGHT / 9))
    pygame.draw.rect(screen, mo.ORANGE,
                     (size * 290 * mo.WIDTH / 700, size * mo.HEIGHT / 3, size * 99 * mo.WIDTH / 500,
                      size * mo.HEIGHT / 9))
    pygame.draw.rect(screen, mo.ORANGE,
                     (size * 490 * mo.WIDTH / 700, size * mo.HEIGHT / 3, size * 99 * mo.WIDTH / 500,
                      size * mo.HEIGHT / 9))
    pygame.draw.circle(screen, mo.YELLOW_GREEN, (15 * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                       size * mo.HEIGHT / 10)
    pygame.draw.circle(screen, mo.YELLOW_GREEN, (35 * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                       size * mo.HEIGHT / 10)
    pygame.draw.circle(screen, mo.YELLOW_GREEN, (55 * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                       size * mo.HEIGHT / 10)

    my_font = pygame.freetype.Font('fonts\\comic.ttf', 40 * size / 20)
    small_font = pygame.freetype.Font('fonts\\comic.ttf', 20 * size / 20)
    level, rect, = my_font.render("LEVEL 1", mo.BLACK)
    screen.blit(level, (size * 95 * mo.WIDTH / 700, 11 * size * mo.HEIGHT / 30))
    level, rect = my_font.render("LEVEL 2", mo.BLACK)
    screen.blit(level, (size * 295 * mo.WIDTH / 700, 11 * size * mo.HEIGHT / 30))
    level, rect = my_font.render("LEVEL 3", mo.BLACK)
    my_font = pygame.freetype.Font('fonts\\comic.ttf', 35 * size / 20)
    screen.blit(level, (size * 495 * mo.WIDTH / 700, 11 * size * mo.HEIGHT / 30))
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
    text_font = pygame.freetype.Font('fonts\\comic.ttf', 50 * size / 20)
    text, rect = text_font.render("Choose your level!")
    screen.blit(text, (size * 18 * mo.WIDTH / 70, 7 * size * mo.HEIGHT / 15))
    text, rect = text_font.render("Table of results")
    screen.blit(text, (size * 18 * mo.WIDTH / 70, 12 * size * mo.HEIGHT / 15))
    text, rect = small_font.render("Music by Kevin MacLeod")
    screen.blit(text, (size * 50 * mo.WIDTH / 70, 14 * size * mo.HEIGHT / 15))
    description, rect = text_font.render("Eat all the Morties")
    screen.blit(description, (size * 18 * mo.WIDTH / 70, 8 * size * mo.HEIGHT / 60))
    description, rect = text_font.render("or they'll eat you")
    screen.blit(description, (size * 20 * mo.WIDTH / 70, 1 * size * mo.HEIGHT / 5))
    if event.type == pygame.MOUSEMOTION:
        if size * mo.HEIGHT / 3 <= event.pos[1] <= 4 * size * mo.HEIGHT / 9:
            if size * 90 * mo.WIDTH / 700 <= event.pos[0] <= size * (9 / 70 + 99 / 500) * mo.WIDTH:
                pygame.draw.rect(screen, mo.BLACK,
                                 (size * 90 * mo.WIDTH / 700, size * mo.HEIGHT / 3, size * 99 * mo.WIDTH / 500,
                                  size * mo.HEIGHT / 9),
                                 2)
            elif size * 290 * mo.WIDTH / 700 <= event.pos[0] <= size * (29 / 70 + 99 / 500) * mo.WIDTH:
                pygame.draw.rect(screen, mo.BLACK,
                                 (size * 290 * mo.WIDTH / 700, size * mo.HEIGHT / 3, size * 99 * mo.WIDTH / 500,
                                  size * mo.HEIGHT / 9), 2)
            elif size * 490 * mo.WIDTH / 700 <= event.pos[0] <= size * (49 / 70 + 99 / 500) * mo.WIDTH:
                pygame.draw.rect(screen, mo.BLACK,
                                 (size * 490 * mo.WIDTH / 700, size * mo.HEIGHT / 3, size * 99 * mo.WIDTH / 500,
                                  size * mo.HEIGHT / 9), 2)
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


def draw_choice_display(screen, event, size):
    screen.fill(mo.WHITE)
    pygame.draw.rect(screen, mo.GREEN,
                     (size / 3 * mo.WIDTH, size * mo.HEIGHT / 7, size / 3 * mo.WIDTH, size * mo.HEIGHT / 7))
    pygame.draw.rect(screen, mo.YELLOW,
                     (size / 3 * mo.WIDTH, 3 * size * mo.HEIGHT / 7, size / 3 * mo.WIDTH, size * mo.HEIGHT / 7))
    pygame.draw.rect(screen, mo.RED,
                     (size / 3 * mo.WIDTH, 5 * size * mo.HEIGHT / 7, size / 3 * mo.WIDTH, size * mo.HEIGHT / 7))
    my_font = pygame.freetype.Font('fonts\\comic.ttf', 45 * size / 20)
    easy, rect = my_font.render("EASY", mo.BLACK)
    screen.blit(easy, (size * 52 * mo.WIDTH / 120, 13 * size * mo.HEIGHT / 70))
    medium, rect = my_font.render("MEDIUM", mo.BLACK)
    screen.blit(medium, (size * 46 * mo.WIDTH / 120, 33 * size * mo.HEIGHT / 70))
    hard, rect = my_font.render("HARD", mo.BLACK)
    screen.blit(hard, (size * 26 * mo.WIDTH / 60, 53 * size * mo.HEIGHT / 70))
    text_font = pygame.freetype.Font('fonts\\comic.ttf', 50 * size / 20)
    text_level, rect = text_font.render("Choose your difficulty level!")
    screen.blit(text_level, (size * 8 * mo.WIDTH / 60, 3 * size * mo.HEIGHT / 70))
    draw_image('images\\Rick1.png', size, 2 / 5, screen, 79 / 80, 13 / 30, mo.WIDTH, mo.HEIGHT)
    draw_image('images\\pickle_rick.png', size, 1/4, screen, 4/10, 79/80, mo.WIDTH, mo.HEIGHT)
    draw_image('images\\portal.png', size, 1/2, screen, 9/10, 7/8, mo.WIDTH, mo.HEIGHT)
    draw_image('images\\wubba.png', size, 1/5, screen, 3/10, 45/80, mo.WIDTH, mo.HEIGHT)
    if event.type == pygame.MOUSEMOTION:
        if size * mo.WIDTH / 3 <= event.pos[0] <= 2 * size * mo.WIDTH / 3:
            if size * mo.HEIGHT / 7 <= event.pos[1] <= 2 * size * mo.HEIGHT / 7:
                pygame.draw.rect(screen, mo.BLACK,
                                 (size / 3 * mo.WIDTH, size * mo.HEIGHT / 7, size / 3 * mo.WIDTH, size * mo.HEIGHT / 7),
                                 2)
            elif 3 * size * mo.HEIGHT / 7 <= event.pos[1] <= 4 * size * mo.HEIGHT / 7:
                pygame.draw.rect(screen, mo.BLACK,
                                 (size / 3 * mo.WIDTH, 3 * size * mo.HEIGHT / 7, size / 3 * mo.WIDTH,
                                  size * mo.HEIGHT / 7),
                                 2)
            elif 5 * size * mo.HEIGHT / 7 <= event.pos[1] <= 6 * size * mo.HEIGHT / 7:
                pygame.draw.rect(screen, mo.BLACK,
                                 (size / 3 * mo.WIDTH, 5 * size * mo.HEIGHT / 7, size / 3 * mo.WIDTH,
                                  size * mo.HEIGHT / 7),
                                 2)


def draw_table(screen, table, place, size):
    """

    Рисуем экран с таблицей лидеров

    Так же на экране пишется, какое место в таблице занял игрок

    Если игрок не занял никакого места, то пишем другую фразу

    screen - экран

    table - массив с очками и именами игроков

    place - место игрока в этой таблице
    """
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH, mo.HEIGHT))
    my_font = pygame.freetype.Font('fonts\\comic.ttf', 45 * size / 20)

    if place <= 10:
        text_congratulations, rect = my_font.render("Congratulations!", mo.BLACK)
        screen.blit(text_congratulations, (10 * size / 20, 10 * size / 20))

        text_your_place, rect = my_font.render("Your place is ", mo.BLACK)
        screen.blit(text_your_place, (10 * size / 20, 60 * size / 20))

        text_place, rect = my_font.render(str(place), mo.BLACK)
        screen.blit(text_place, (400 * size / 20, 60 * size / 20))
    else:
        text_not_in_the_top, rect = my_font.render("You're too bad!", mo.BLACK)
        screen.blit(text_not_in_the_top, (10 * size / 20, 10 * size / 20))

        text_try_again, rect = my_font.render("Try again!", mo.BLACK)
        screen.blit(text_try_again, (10 * size / 20, 60 * size / 20))

    for i in range(0, 10):
        text_score, rect = my_font.render(str(table[2 * i]), mo.BLACK)
        screen.blit(text_score, (10 * size / 20, (150 + i * 50) * size / 20))

        text_name, rect = my_font.render(str(table[2 * i + 1]), mo.BLACK)
        screen.blit(text_name, (150 * size / 20, (150 + i * 50) * size / 20))

    text_press_any_key, rect = my_font.render("Press any key to exit", mo.BLACK)
    screen.blit(text_press_any_key, (10 * size / 20, 700 * size / 20))
    text_press_any_key, rect = my_font.render("Thanks for playing!", mo.BLACK)
    screen.blit(text_press_any_key, (10 * size / 20, 750 * size / 20))
    draw_image('images\\rickroll.jpg', size, 4 / 5, screen, 12 / 10, 65 / 80, mo.WIDTH, mo.HEIGHT)
