from model_objects import Wall, MainSnake, Food, Enemy
from vis import DrawableWall, DrawableSnake


def read_wall_data_from_file(input_filename):
    '''

    Считывает данные о стенах из файла, создаёт сами объекты и вызывает создание их графических образов

    input_filename - имя считываемого файла
    '''
    walls = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue

            wall = Wall()
            parse_wall_parameters(line, wall)
            walls.append(wall)

    return (DrawableWall(obj) for obj in walls)


def read_main_snake_data_from_file(input_filename):
    '''

    Считывает данные о главной змее из файла

    input_filename - имя считываемого файла

    Входные данные должны представлять из себя строку, состоящую из

    <Координаты, введённые через пробел> <Ориентация головы змеи (w, a, s или d)> <Цвет змеи>
    '''
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue

            tokens = line.split(' ')
            color = tokens[-1]
            direction = tokens[-2]
            coordinates = []
            for i in range(0, len(tokens) - 2, 2):
                cell = []
                cell.append(int(tokens[i]))
                cell.append(int(tokens[i+1]))
                coordinates.append(cell)

            snake = MainSnake(coordinates, direction)

    return (snake)


def read_food_data_from_file(input_filename):
    '''

    Считывает данные о змеях-еде из файла, создаёт сами объекты и вызывает создание их графических образов

    input_filename - имя считываемого файла
    '''
    foods = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue

            food = Food()
            parse_food_parameters(line, food)
            foods.append(food)
    return (DrawableSnake(obj) for obj in foods)


def read_enemy_data_from_file(input_filename):
    '''

    Считывает данные о змеях-врагах из файла, создаёт сами объекты и вызывает создание их графических образов

    input_filename - имя считываемого файла
    '''
    enemies = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue

            enemy = Enemy()
            parse_enemy_parameters(line, enemy)
            enemies.append(enemy)
    return (DrawableSnake(obj) for obj in enemies)


def parse_wall_parameters(line, wall):
    '''

    Считывает данные о стене из строки

    Входная строка должна иметь следующий вид:

    <x_begin> <y_begin> <x_end> <y_end> <Цвет>

    Где (x_begin, y_begin) - координаты начала стены, (x_end, y_end) - координаты конца стены

    Пример строки:

    20 30 40 30 BLACK

    Параметры:

    line - строка с описанием файла

    wall - объект стены
    '''
    tokens = line.split()
    assert (len(tokens) == 5)
    wall.x_begin = int(tokens[0])
    wall.y_begin = int(tokens[1])
    wall.x_end = int(tokens[2])
    wall.y_end = int(tokens[3])
    wall.color = tokens[4]

def parse_food_parameters(line, food):
    '''

    Считывает данные о змее-еде из строки

    Входная строка должна иметь следующий вид:

    <Массив координат змеи> <direction> <Цвет> <Массив действий>

    Где direction - направление движения змейки в данный момент, характеризуется одной из букв 'w', 'a', 's', 'd'

    Пример строки (не знаю, как написать массив координат, но предположу):

    [(20, 30), (20, 31), (20, 32), (21, 32), (22, 32), (23, 32)] a GREEN [не знаю, как выглядит массив действий]

    Параметры:

    line - строка с описанием файла

    food - объект змеи-еды
    '''
    tokens = line.split()
    assert (len(tokens) == 4)
    food.coordinates = tokens[0]
    food.direction = tokens[1]
    food.color = tokens[2]
    food.actions = tokens[3]


def parse_enemy_parameters(line, enemy):
    '''

    Считывает данные о змее-враге из строки

    Входная строка должна иметь следующий вид:

    <Массив координат змеи> <direction> <Цвет>

    Где direction - направление движения змейки в данный момент, характеризуется одной из букв 'w', 'a', 's', 'd'

    Пример строки (не знаю, как написать массив координат, но предположу):

    [(20, 30), (20, 31), (20, 32), (21, 32), (22, 32), (23, 32)] a MAGENTA

    Параметры:

    line - строка с описанием файла

    enemy - объек змеи-врага
    '''
    tokens = line.split()
    assert (len(tokens) == 3)
    enemy.coordinates = tokens[0]
    enemy.direction = tokens[1]
    enemy.color = tokens[2]
