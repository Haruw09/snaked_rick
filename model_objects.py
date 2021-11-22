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

    def collision(self, x_snake, y_snake):
        for position in self.coordinates:
            x = position[0]
            y = position[1]
            if x == x_snake and y == y_snake:
                return True
        return False


class Food(Snakes):
    def __init__(self):
        super(Food, self).__init__()
        self.color = (100, 100, 100)  # FIXME изменить на COLOR
        self.live = True
    def eating(self, x_snake, y_snake):
        if:
            self.live(False)
        else: