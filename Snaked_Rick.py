import pygame
import time

pygame.init()

# Постоянные
FPS = 30
scale = 10
display_hight = 40
display_width = 40

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


# Классы
def draw_display():
    pygame.draw.rect(screen, BLACK, (0, 0, display_width, display_hight))


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.color = GREEN
        self.x = 20
        self.y = 20
        self.speed = 10
        self.direction = 'd'

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x * scale, self.y * scale, scale, scale))

    def move(self):
        if self.x > display_width:
            self.x = 0

        if self.x < 0:
            self.x = display_width - 1

        if self.y > display_hight:
            self.y = 0

        if self.y < 0:
            self.y = display_hight - 1

        if self.direction == 'd':
            self.x += 1

        elif self.direction == 'a':
            self.x -= 1

        elif self.direction == 'w':
            self.y -= 1

        else:
            self.y += 1

    def veer(self, event):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.direction = 'w'

        if pressed[pygame.K_s]:
            self.direction = 's'

        if pressed[pygame.K_a]:
            self.direction = 'a'

        if pressed[pygame.K_d]:
            self.direction = 'd'


screen = pygame.display.set_mode((display_width * scale, display_hight * scale))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

snake = Snake(screen)

while not finished:
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(BLACK)
    snake.draw()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            snake.veer(event)

    snake.move()

pygame.quit()
