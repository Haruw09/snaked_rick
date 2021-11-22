class Wall:
    def __init__(self, x_begin, y_begin, x_end, y_end):
        """
        Инициализация стен в виде прямоугольника, которые ограничивают пространство для движения змейки
        """
        self.x_begin = x_begin
        self.y_begin = y_begin
        self.x_end = x_end
        self.y_end = y_end
        self.color = (0, 0, 0)  # FIXME изменить на COLOR

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
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def collision(self, coordinates):
        '''
        :param coordinates - массив координат квадратиков другой змейки
        :return: 0 - дополнительная змейка врезалась в данную, 1 - наоборот, 2 - ничего не произошло
        '''
        for position in self.coordinates:
            x = position[0]
            y = position[1]
            if x == coordinates[0][0] and y == coordinates[0][1]:
                return 0
        for position in coordinates:
            x = position[0]
            y = position[1]
            if x == self.coordinates[0][0] and y == self.coordinates[0][1]:
                return 1
        return 2

    def move_tail(self):
        for number in (1, len(self.coordinates) - 1, 1):
            self.coordinates[number] = self.coordinates[number - 1]


class Food(Snakes):
    def __init__(self, coordinates):
        Snakes.__init__(self, coordinates)
        self.color = (100, 100, 100)  # FIXME изменить на COLOR
        self.actions = []
        self.live = True
        self.mass = 5

    def eating(self, coordinates):
        '''
        :param coordinates: координаты "побочной змейки"
        :return: вывод прибавки к счёту по итогу обработки
        '''
        if self.collision(coordinates) == 0:
            self.live(False)
            return self.mass
        return 0

    def death(self, coordinates):
        if self.collision(coordinates) == 1:
            self.live(False)

    def move(self):
        self.actions.pop(0)


class Enemy(Snakes):
    def __init__(self, coordinates):
        Snakes.__init__(self, coordinates)
        self.color = (200, 200, 200)  # FIXME изменить на COLOR
