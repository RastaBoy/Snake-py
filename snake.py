import pygame 
from utils import *


class Snake:

    def __init__(self, x, y, direction:str, length=4):
        self.direction = direction
        self.head = [x, y]
        self.tail = []
        self.length = length
        self.tail.append([self.head[0] - 35, self.head[1]])
        for i in range(1, self.length):
            self.tail.append([self.tail[i-1][0] - 35, self.tail[i-1][1]])
        

    def update(self):
        temp = self.tail[0]
        self.tail[0] = [*self.head]
        for i in range(1, len(self.tail)):
            temp2 = [*self.tail[i]]
            self.tail[i] = temp
            temp = temp2


                

    def set_direction(self, direction:str):
        self.direction = direction

    def move(self):
        if self.direction == "UP":
            if self.head[1] < 0:
                self.head[1] = SCREEN[1]
            else:
                self.head[1] -= 40
        if self.direction == "DOWN":
            if self.head[1] > SCREEN[1]:
                self.head[1] = 0
            else:
                self.head[1] += 40
        if self.direction == "LEFT":
            if self.head[0] < 0:
                self.head[0] = SCREEN[0]
            else:
                self.head[0] -= 40
        if self.direction == "RIGHT":
            if self.head[0] > SCREEN[0]:
                self.head[0] = 0
            else:
                self.head[0] += 40

    def render(self):
        pygame.draw.rect(screen, WHITE, (self.head[0], self.head[1], 30, 30))
        for i in self.tail:
            pygame.draw.rect(screen, WHITE, (i[0], i[1], 30, 30))