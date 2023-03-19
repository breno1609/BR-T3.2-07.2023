import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle 


class Bird(Obstacle):
    def __init__(self, images, velocidade = 2.0): #images[0,1]
        self.type =0
        super().__init__(images, self.type)
        self.rect.y = random.randint(200, 260)
        self.velocidade = velocidade

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
        self.type += 1
        if self.type == 2:
            self.type = 0    
        pygame.time.wait(int(100 / self.velocidade))
  