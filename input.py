from model_objects import Wall, MainSnake, Food, Enemy


def read_wall_data_from_file(input_filename):
    """

    Считывает данные о стене из строки

    Входная строка должна иметь следующий вид:

    <x_begin> <y_begin> <x_end> <y_end> <Цвет>

    Где (x_begin, y_begin) - координаты начала стены, (x_end, y_end) - координаты конца стены

    Пример строки:

    20 30 40 30 BLACK

    input_filename - имя считываемого файла
    """
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
    """

    Считывает данные о главной змее из файла

    input_filename - имя считываемого файла

    Входные данные должны представлять из себя строку, состоящую из

    <Координаты, введённые через пробел> <Ориентация головы змеи (w, a, s или d)> <Цвет змеи>
    """
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
                cell.append(int(tokens[i + 1]))
                coordinates.append(cell)

            snake = MainSnake(coordinates, direction)

    return (snake)


def read_food_data_from_file(input_filename):
    """

    Считывает данные о змеях-еде из файла, создаёт сами объекты и вызывает создание их графических образов

    input_filename - имя считываемого файла
    """
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
                cell.append(int(tokens[i + 1]))
                coordinates.append(cell)

            snake = Food(coordinates, direction)
            foods.append(snake)
    return (foods)


def read_enemy_data_from_file(input_filename):
    """

    Считывает данные о змеях-врагах из файла, создаёт сами объекты и вызывает создание их графических образов

    input_filename - имя считываемого файла
    """
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
                cell.append(int(tokens[i + 1]))
                coordinates.append(cell)

            snake = Enemy(coordinates, direction)
            enemies.append(snake)
    return (enemies)


def read_file(file_name):
    """

    Считывает данные из файла с таблицей лидеров

    file_name - имя считываемого файла

    Возвращает двумерный массив, состоящий из пар [очки, имя игрока]
    """
    file = [] * 10
    inp = open(file_name, encoding='utf8')
    lines = inp.read().split('\n')
    for each_line in lines:
        cell = []
        tokens = each_line.split(' ')
        cell.append(tokens[0])
        cell.append(tokens[1])
        file.append(cell)
    inp.close()
    return file


def top_entry(score, changing_name):
    """

    Функция проверяет, попал ли игрок в таблицу лидеров

    Если попал, то вносит его результат и имя в список

    Так же функция перезаписывает файл

    score - счёт игрока

    changing_name - имя игрока

    Возвращает массив эллементов, где каждый каждый чётный элемент от 0 до 18 - очки, каждый нечётный от 1 до 19 имена

    20 элемент - место текущего игрока в этой таблице (Если место больше 10, то в всегда будет отдавать 11)
    """
    file = read_file('other\\top.txt')
    top = []
    names = []
    place = 11
    for i in range(10):
        player_score = int(file[i][0])
        top.append(player_score)
        names.append(str(file[i][1]))

    for i in range(10):
        if score >= top[i]:
            smth = score
            score = top[i]
            top[i] = smth

            smbd = changing_name
            changing_name = names[i]
            names[i] = smbd
            if place > i + 1:
                place = i + 1

    table = []
    out = open('other\\top.txt', 'w')
    for i in range(9):
        out.write(str(top[i]) + ' ' + str(names[i]) + '\n')
        table.append(str(top[i]))
        table.append(str(names[i]))

    out.write(str(top[9]) + ' ' + str(names[9]))
    table.append(str(top[9]))
    table.append(str(names[9]))
    table.append(place)
    out.close()

    return table
