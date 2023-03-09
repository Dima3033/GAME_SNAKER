import pygame
import random
pygame.init()
window_width = 400
window_height = 400
GAME_WINDOW = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
class Snake:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 10
        self.speed = 10
        self.direction = 'RIGHT'
        self.body = []
    def move(self):
        if self.direction == 'RIGHT':
            self.x += self.speed
        elif self.direction == 'LEFT':
            self.x -= self.speed
        elif self.direction == 'UP':
            self.y -= self.speed
        elif self.direction == 'DOWN':
            self.y += self.speed
    def draw(self):
        for body_part in self.body:
            pygame.draw.rect(GAME_WINDOW, self.color, (body_part[0], body_part[1], self.size, self.size))
        pygame.draw.rect(GAME_WINDOW, self.color, (self.x, self.y, self.size, self.size))
    def add_body_part(self):
        self.body.append((self.x, self.y))
class Food:
    def __init__(self, color):
        self.color = color
        self.size = 10
        self.x = random.randint(0, (window_width - self.size) // self.size) * self.size
        self.y = random.randint(0, (window_height - self.size) // self.size) * self.size
    def draw(self):
        pygame.draw.rect(GAME_WINDOW, self.color, (self.x, self.y, self.size, self.size))
def main():
    clock = pygame.time.Clock()
    snake = Snake(window_width // 2, window_height // 2, GREEN)
    food = Food(RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.direction = 'RIGHT'
                elif event.key == pygame.K_LEFT:
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_UP:
                    snake.direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    snake.direction = 'DOWN'
        snake.move()
        if snake.x == food.x and snake.y == food.y:
            food = Food(RED)
            snake.add_body_part()
        if snake.x < 0 or snake.x > window_width - snake.size or snake.y < 0 or snake.y > window_height - snake.size:
            pygame.quit()
            quit()
        for body_part in snake.body:
            if snake.x == body_part[0] and snake.y == body_part[1]:
                pygame.quit()
                quit()
        GAME_WINDOW
