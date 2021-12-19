import pygame
import pygame.freetype
import model_objects as mo

pygame.freetype.init()
SIZE = 15


def draw_image(name, size, scale, screen, bottom_right_x, bottom_right_y, width, height):
    """
    Вывод картинки на экран
    :param name: имя файла и место расположения
    :param size: число пикселей в одной клетке змейки
    :param scale: масштабирование картинки
    :param screen: экран, на котором рисуется
    :param bottom_right_x: абсцисса нижнего правого края картинки
    :param bottom_right_y: ордината нижнего правого края картинки
    :param width: параметр ширины экрана (в клетках)
    :param height: параметр высоты экрана (в клетках)
    :return: рисование картинки на экране
    """
    surface = pygame.image.load(name)
    surface = pygame.transform.scale(surface, ((int(surface.get_width() * scale * size / 20),
                                                int(surface.get_height() * scale * size / 20))))
    rectangle = surface.get_rect(bottomright=(size * bottom_right_x * width, size * bottom_right_y * height))
    screen.blit(surface, rectangle)


def draw_text(text, font, x, y, size, screen, width, height, color):
    """
    Вывод заданного текста на экран
    :param text: текст в кавычках, который хочется вывести
    :param font: шрифт, которым нужно писать
    :param x: абсцисса начала текста
    :param y: ордината начала текста
    :param screen: экран вывода
    :param color: цвет шрифта
    :return: нарисованный текст
    """
    vis_text, rect = font.render(text, color)
    screen.blit(vis_text, (x * size * width / 20, y * size * height / 20))


def draw_rect_button(screen, color, x, y, delta_x, delta_y, font, text, text_color, x_text, y_text, size, width,
                     height):
    pygame.draw.rect(screen, color,
                     (size * x * width, size * y * height, size * delta_x * width,
                      size * delta_y * height))
    draw_text(text, font, 20 * (x_text + x), 20 * (y_text + y), size, screen, width, height, text_color)


def draw_border(screen, color, x, y, delta_x, delta_y, rect_width, width, height, event):
    if event.type == pygame.MOUSEMOTION and x <= event.pos[0] <= x + delta_x and y <= event.pos[0] <= y + delta_y:
        pygame.draw.rect(screen, color,
                         (size * x * width, size * y * height, size * delta_x * width,
                          size * delta_y * height), rect_width)


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


def draw_field(screen, size):
    pygame.draw.rect(screen, mo.WHITE, (0, 0, mo.WIDTH * size, mo.HEIGHT * size))


def draw_start_display(screen, event, size):
    draw_field(screen, size)
    head_font = pygame.freetype.Font("fonts\\COOPBL.TTF", 60 * size / 20)
    my_font = pygame.freetype.Font('fonts\\comic.ttf', 40 * size / 20)
    medium_font = pygame.freetype.Font('fonts\\comic.ttf', 35 * size / 20)
    small_font = pygame.freetype.Font('fonts\\comic.ttf', 20 * size / 20)
    text_font = pygame.freetype.Font('fonts\\comic.ttf', 50 * size / 20)
    draw_text("Snaked Rick", head_font, 6, 1, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    for i in range(0, 3, 1):
        draw_rect_button(screen, mo.ORANGE, (20 * i + 9) / 70, 1 / 3, 99 / 500, 1 / 9, my_font, "LEVEL " + str(i + 1),
                         mo.BLACK, 5 / 700, 1 / 30, size, mo.WIDTH, mo.HEIGHT)
        pygame.draw.circle(screen, mo.YELLOW_GREEN, ((20 * i + 15) * size * mo.WIDTH / 70, 2 * size * mo.HEIGHT / 3),
                           size * mo.HEIGHT / 10)
        draw_text("Table of", medium_font, (400 * i + 190) / 70, 370 / 30, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
        draw_text("LEVEL " + str(i + 1), medium_font, (400 * i + 190) / 70, 410 / 30, size, screen, mo.WIDTH, mo.HEIGHT,
                  mo.BLACK)
    draw_text("Eat all the Morties", text_font, 36 / 7, 8 / 3, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_text("or they'll eat you", text_font, 40 / 7, 4, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_text("Choose your level!", text_font, 36 / 7, 28 / 3, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_text("Table of results", text_font, 36 / 7, 48 / 3, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_text("Music by Kevin MacLeod", small_font, 100 / 7, 56 / 3, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
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
    draw_field(screen, size)
    my_font = pygame.freetype.Font('fonts\\comic.ttf', 45 * size / 20)
    text_font = pygame.freetype.Font('fonts\\comic.ttf', 50 * size / 20)
    draw_rect_button(screen, mo.GREEN, 1 / 3, 1 / 7, 1 / 3, 1 / 7, my_font, "EASY",
                     mo.BLACK, 1 / 10, 3 / 70, size, mo.WIDTH, mo.HEIGHT)
    draw_rect_button(screen, mo.YELLOW, 1 / 3, 3 / 7, 1 / 3, 1 / 7, my_font, "MEDIUM",
                     mo.BLACK, 1 / 20, 3 / 70, size, mo.WIDTH, mo.HEIGHT)
    draw_rect_button(screen, mo.RED, 1 / 3, 5 / 7, 1 / 3, 1 / 7, my_font, "HARD",
                     mo.BLACK, 1 / 10, 3 / 70, size, mo.WIDTH, mo.HEIGHT)
    draw_text("Choose your difficulty level!", text_font, 8 / 3, 6 / 7, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_image('images\\Rick1.png', size, 2 / 5, screen, 79 / 80, 13 / 30, mo.WIDTH, mo.HEIGHT)
    draw_image('images\\pickle_rick.png', size, 1 / 4, screen, 4 / 10, 79 / 80, mo.WIDTH, mo.HEIGHT)
    draw_image('images\\portal.png', size, 1 / 2, screen, 9 / 10, 7 / 8, mo.WIDTH, mo.HEIGHT)
    draw_image('images\\wubba.png', size, 1 / 5, screen, 3 / 10, 45 / 80, mo.WIDTH, mo.HEIGHT)
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


def draw_end_display(screen, score, name, size):
    """
    Функция рисует экран, после проигрыша игры, на котором происходит ввод имени игрока
    screen - экран, на котором всё пишется
    score - счёт игрока
    name - имя игрока
    """
    draw_field(screen, size)
    my_font = pygame.freetype.Font('fonts\\comic.ttf', 45 * size / 20)
    draw_text("Game over. Your score is ", my_font, 10 / 41, 10 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_text(str(score), my_font, 545 / 41, 10 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_text("Write your name: ", my_font, 10 / 41, 70 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_text(str(name), my_font, 400 / 41, 70 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_text('Press key "->" to continue', my_font, 10 / 41, 130 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_image('images\\end.png', size, 1, screen, 1.06, 75 / 80, mo.WIDTH, mo.HEIGHT)


def draw_table(screen, table, place, size):
    """

    Рисуем экран с таблицей лидеров

    Так же на экране пишется, какое место в таблице занял игрок

    Если игрок не занял никакого места, то пишем другую фразу

    screen - экран

    table - массив с очками и именами игроков

    place - место игрока в этой таблице
    """
    draw_field(screen, size)
    my_font = pygame.freetype.Font('fonts\\comic.ttf', 45 * size / 20)
    if place <= 10:
        draw_text("Congratulations!", my_font, 10 / 41, 10 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
        draw_text("Your place is ", my_font, 10 / 41, 60 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
        draw_text(str(place), my_font, 300 / 41, 60 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    else:
        draw_text("You're too bad!", my_font, 10 / 41, 10 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
        draw_text("Try again!", my_font, 10 / 41, 60 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    for i in range(0, 10):
        draw_text(str(table[2 * i]), my_font, 10 / 41, (150 + i * 50) / 41, size, screen, mo.WIDTH,
                  mo.HEIGHT, mo.BLACK)
        draw_text(str(table[2 * i + 1]), my_font, 150 / 41, (150 + i * 50) / 41, size, screen, mo.WIDTH,
                  mo.HEIGHT, mo.BLACK)
    draw_text("Press any key to exit", my_font, 10 / 41, 700 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_text("Thanks for playing!", my_font, 10 / 41, 750 / 41, size, screen, mo.WIDTH, mo.HEIGHT, mo.BLACK)
    draw_image('images\\rickroll.jpg', size, 4 / 5, screen, 12 / 10, 65 / 80, mo.WIDTH, mo.HEIGHT)
