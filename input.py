from model_objects import Wall, MainSnake, Food, Enemy


def read_wall_data_from_file(input_filename):
    '''

    Считывает данные о стене из строки

    Входная строка должна иметь следующий вид:

    <x_begin> <y_begin> <x_end> <y_end> <Цвет>

    Где (x_begin, y_begin) - координаты начала стены, (x_end, y_end) - координаты конца стены

    Пример строки:

    20 30 40 30 BLACK

    input_filename - имя считываемого файла
    '''
    walls = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue

            tokens = line.split()
            x_begin = int(tokens[0])
            y_begin = int(tokens[1])
            x_end = int(tokens[2])
            y_end = int(tokens[3])
            color = tokens[4]
            wall = Wall(x_begin, y_begin, x_end, y_end)
            walls.append(wall)

    return (walls)


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

            tokens = line.split(' ')
            color = tokens[-1]
            direction = tokens[-2]
            coordinates = []
            for i in range(0, len(tokens) - 2, 2):
                cell = []
                cell.append(int(tokens[i]))
                cell.append(int(tokens[i+1]))
                coordinates.append(cell)

            snake = Food(coordinates, direction)
            foods.append(snake)
    return (foods)


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

            tokens = line.split(' ')
            color = tokens[-1]
            direction = tokens[-2]
            coordinates = []
            for i in range(0, len(tokens) - 2, 2):
                cell = []
                cell.append(int(tokens[i]))
                cell.append(int(tokens[i+1]))
                coordinates.append(cell)

            snake = Enemy(coordinates, direction)
            enemies.append(snake)
    return (enemies)

