from random import randint
import pygame
import vis
import control
import input

# Цвета
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
ORANGE = (217, 232, 12)

WIDTH = 41
HEIGHT = 41
SIZE = 15


class GameManager:
    def __init__(self, WIDTH, HEIGHT, screen):
        self.FPS = 30
        self.score = 0
        self.score_for_food = 1
        self.number_of_food = 3
        self.live_food = [0] * self.number_of_food
        '''
        Параметры экрана (Ширина, Высота и масштаб, т.е. кол-во пикселей в одном игровом квадратике)
        '''
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.name = ''
        self.top_number = 0
        self.score = 0
        self.screen = screen

        self.walls = []
        self.main_snake = []
        self.food = []

    def start_display_1(self):
        screen_number = 1
        finished = False
        result = 0
        pygame.mixer.music.load('music\\fasterdoesit.mp3')
        pygame.mixer.music.play(-1)
        while not finished and result == 0:
            pygame.display.update()
            for event in pygame.event.get():
                if screen_number == 1:
                    vis.draw_start_display(self.screen, event, SIZE)
                    result = control.StartDisplay(event, SIZE)
                    finished = control.update(event)
                    self.top_number = control.TableButtons(event, SIZE)
                    if self.top_number != 0:
                        screen_number = 2
                else:
                    self.table_display()
                    screen_number = 1
                    self.top_number = 0

        if result == 1:
            self.walls = input.read_wall_data('levels\\Lvl_1.txt')
            self.top_number = 1
        elif result == 2:
            self.walls = input.read_wall_data('levels\\Lvl_2.txt')
            self.top_number = 2
        elif result == 3:
            self.walls = input.read_wall_data('levels\\Lvl_3.txt')
            self.top_number = 3

    def start_display_2(self):
        finished = False
        result = 0
        while not finished and result == 0:
            pygame.display.update()
            for event in pygame.event.get():
                vis.draw_choice_display(self.screen, event, SIZE)
                result = control.ChoiceDisplay(event, SIZE)
                finished = control.update(event)

        if result == 1:
            self.FPS = 10
            self.score_for_food = 1
        elif result == 2:
            self.FPS = 20
            self.score_for_food = 2
        elif result == 3:
            self.FPS = 30
            self.score_for_food = 3

    def table_display(self):
        '''
        Здесь читается, анализируется, переписывается и записывается обратно в файл таблица лидеров
        '''
        table = input.top_entry(self.score, self.name, self.top_number)
        finished = False
        '''
        Здесь игрок модет полюбоваться таблицей лидеров
        Закрыть окно можно, нажав любую кнопку
        '''
        bottom_pressed = False
        while not finished and not bottom_pressed:
            pygame.display.update()
            self.screen.fill(WHITE)
            vis.draw_table(self.screen, table, table[20], SIZE)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    bottom_pressed = True
                    finished = control.update(event)

    def read_main_snake(self):
        self.main_snake = input.read_main_snake_data('other\\main_snake.txt')

    def read_food(self):
        self.food = input.read_food_data('other\\food.txt')

    def draw_walls(self):
        for wall in self.walls:
            vis.draw_wall(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end, wall.color, self.screen)

    def draw_food(self):
        for num in self.live_food:
            vis.draw_snake(self.food[num].coordinates, self.food[num].color, self.food[num].head_color, self.screen)

    def new_food(self, num):
        flag = 0
        while flag == 0:
            self.live_food[num] = randint(0, len(self.food) - 1)
            x = self.food[self.live_food[num]].coordinates[0][0]
            y = self.food[self.live_food[num]].coordinates[0][1]
            for wall in self.walls:
                if not (wall.x_begin <= x <= wall.x_end and wall.y_begin <= y <= wall.y_end):
                    flag = 1
            for another_num in range(num):
                if self.live_food[another_num] == self.live_food[num]:
                    flag = 0


    def choose_music(self):
        rnd = randint(1, 3)
        if rnd == 1:
            pygame.mixer.music.load('music\\breaktime.mp3')
            pygame.mixer.music.play(-1)
        elif rnd == 2:
            pygame.mixer.music.load('music\\carefree.mp3')
            pygame.mixer.music.play(-1)
        elif rnd == 3:
            pygame.mixer.music.load('music\\fretless.mp3')
            pygame.mixer.music.play(-1)

    def wall_collision(self, wall):
        if wall.collision(self.main_snake.coordinates[0][0], self.main_snake.coordinates[0][1]):
            self.main_snake.death = 1

    def food_turn(self, wall):
        for num in self.live_food:
            self.food[num].turn(wall.x_begin, wall.y_begin, wall.x_end, wall.y_end)

    def move_food(self):
        for num in self.live_food:
            self.food[num].move_miss = (self.food[num].move_miss + 1) % (self.food[num].miss + 1)
            if self.food[num].move_miss == self.food[num].miss:
                self.food[num].move_tail()
                self.food[num].move_head(self.food[num].direction)

    def eating(self):
        for num in range(self.number_of_food):
            food_number = self.live_food[num]
            if self.main_snake.collision(self.food[food_number].coordinates) == 1:
                l = len(self.main_snake.coordinates)
                x_end = self.main_snake.coordinates[l - 1][0]
                y_end = self.main_snake.coordinates[l - 1][1]
                self.main_snake.elongation(x_end, y_end)
                self.score += self.score_for_food
                self.new_food(num)

    def bite(self):
        if self.main_snake.collision(self.main_snake.coordinates) == 0:
            self.main_snake.death = 1

    def wasd(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.main_snake.veer()
                finished = control.update(event)
                return finished

class Wall:
    def __init__(self, x_begin, y_begin, x_end, y_end):
        """
        Инициализация стен в виде прямоугольника, которые ограничивают пространство для движения змейки
        """
        self.x_begin = x_begin
        self.y_begin = y_begin
        self.x_end = x_end
        self.y_end = y_end
        self.color = BLACK

    def collision(self, x_snake, y_snake):
        """
        :param x_snake: абсцисса головы змейки
        :param y_snake: ордината головы змейки
        :return: true или false в зависимости от того, столкнулась или нет змея со стеной.
        """
        if self.x_begin <= x_snake <= self.x_end or self.x_end <= x_snake <= self.x_begin:
            if self.y_begin <= y_snake <= self.y_end or self.y_end <= y_snake <= self.y_begin:
                return True
        return False


class Snakes:
    def __init__(self, coordinates, direction):
        """
        :param coordinates: координаты всех квадратиков змейки, начиная с головы
        :param direction: направление движения змейки в данный момент, характеризуется одной
        из букв 'w', 'a', 's', 'd'
        """
        self.coordinates = coordinates
        self.direction = direction
        self.live = True

    def collision(self, coordinates):
        """
        :param coordinates - массив координат квадратиков другой змейки
        :return: 0 - дополнительная змейка врезалась в данную, 1 - наоборот, 2 - ничего не произошло
        """
        for i in range(1, len(self.coordinates)):
            x = self.coordinates[i][0]
            y = self.coordinates[i][1]
            if x == coordinates[0][0] and y == coordinates[0][1]:
                return 0
        for i in range(1, len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            if x == self.coordinates[0][0] and y == self.coordinates[0][1]:
                return 1
        return 2

    def move_tail(self):
        end = [self.coordinates[-1][0], self.coordinates[-1][1]]
        length = len(self.coordinates)
        for number in range(1, length, 1):
            self.coordinates[length - number][0] = self.coordinates[length - number - 1][0]
            self.coordinates[length - number][1] = self.coordinates[length - number - 1][1]
        return end

    def move_head(self, new_direction):
        """
        Функция отвечает за движение головы змейки - поворот и продвижение
        :param new_direction: новое направление движения
        """
        if (self.direction == 'w' or self.direction == 's') and (new_direction == 'a' or new_direction == 'd'):
            self.direction = new_direction
        elif (self.direction == 'a' or self.direction == 'd') and (new_direction == 'w' or new_direction == 's'):
            self.direction = new_direction

        if self.coordinates[0][0] > WIDTH:
            self.coordinates[0][0] = 0
        if self.coordinates[0][0] < 0:
            self.coordinates[0][0] = WIDTH - 1
        if self.coordinates[0][1] > HEIGHT:
            self.coordinates[0][1] = 0
        if self.coordinates[0][1] < 0:
            self.coordinates[0][1] = HEIGHT - 1

        if self.direction == 'd':
            self.coordinates[0][0] += 1
        elif self.direction == 'a':
            self.coordinates[0][0] -= 1
        elif self.direction == 'w':
            self.coordinates[0][1] -= 1
        else:
            self.coordinates[0][1] += 1


class MainSnake(Snakes):
    def __init__(self, coordinates, direction):
        Snakes.__init__(self, coordinates, direction)
        self.color = BLUE
        self.head_color = AQUAMARINE
        self.death = 0

    def elongation(self, x_end, y_end):
        self.coordinates.append([x_end, y_end])

    def veer(self):
        '''

        Функция поворачивает голову змеи, в зависимости от нажатой клавиши.

        Змея не повернёт в противоположную сторону.

        На вход функция получает ивент

        В результате функция отдаёт новое значение ориентации головы змеи
        '''
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            if abs(self.coordinates[0][1] - self.coordinates[1][1]) != 1:
                self.direction = 'w'

        if pressed[pygame.K_s]:
            if abs(self.coordinates[0][1] - self.coordinates[1][1]) != 1:
                self.direction = 's'

        if pressed[pygame.K_a]:
            if abs(self.coordinates[0][0] - self.coordinates[1][0]) != 1:
                self.direction = 'a'

        if pressed[pygame.K_d]:
            if abs(self.coordinates[0][0] - self.coordinates[1][0]) != 1:
                self.direction = 'd'


class Food(Snakes):
    def __init__(self, coordinates, direction):
        Snakes.__init__(self, coordinates, direction)
        self.color = GREEN
        self.head_color = YELLOW_GREEN
        self.actions = []  # Массив действий змейки-еды
        self.miss = 1
        self.move_miss = 0

    def eating(self, coordinates):
        """
        :param coordinates: координаты "побочной змейки"
        :return: вывод прибавки к счёту по итогу обработки
        """
        if self.collision(coordinates) == 0:
            self.live = False
            return True
        return False

    def death(self, coordinates):
        if self.collision(coordinates) == 1:
            self.live = False

    def turn(self, x_begin, y_begin, x_end, y_end):
        dir = self.direction
        if dir == 'w':
            x = self.coordinates[0][0]
            y = self.coordinates[0][1] - 1
        elif dir == 's':
            x = self.coordinates[0][0]
            y = self.coordinates[0][1] + 1
        elif dir == 'a':
            x = self.coordinates[0][0] - 1
            y = self.coordinates[0][1]
        else:
            x = self.coordinates[0][0] + 1
            y = self.coordinates[0][1]

        if x_begin <= x <= x_end and y_begin <= y <= y_end:
            if dir == 'w':
                dir = 's'
            elif dir == 's':
                dir = 'w'
            elif dir == 'a':
                dir = 'd'
            else:
                dir = 'a'

        self.direction = dir
