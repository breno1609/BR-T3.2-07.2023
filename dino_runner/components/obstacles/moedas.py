import random
from dino_runner.components.obstacles.obstacle import Obstacle 

class Moedas(Obstacle):
    def __init__(self, images): 
        self.type =0   
        self.time = 0  
        super().__init__(images, self.type)
        self.rect.y = random.randint(200, 260)

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y)) 
        self.time += 1 
        if self.time > 12: 
            self.type += 1 
            self.time = 0 
        if self.type == 2: 
            self.type = 0 