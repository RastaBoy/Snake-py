import pygame
import sys

from snake import Snake
from utils import *

# Init
game = True
clock = pygame.time.Clock()
snake = Snake(300, 300, "RIGHT", 4)

while game:
    # Events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                snake.set_direction("UP")
            if i.key == pygame.K_DOWN:
                snake.set_direction("DOWN")
            if i.key == pygame.K_RIGHT:
                snake.set_direction("RIGHT")
            if i.key == pygame.K_LEFT:
                snake.set_direction("LEFT")
    

    # Drawing
    screen.fill(BLACK)
    snake.render()
    pygame.display.update()

    # Logic
    snake.update()
    snake.move()
    # Clock tick
    clock.tick(FPS)