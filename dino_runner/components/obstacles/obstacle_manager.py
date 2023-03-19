import pygame
import random
from dino_runner.components.obstacles.cactus import *
from dino_runner.components.obstacles.bird import *
from dino_runner.utils.constants import * 


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):


        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 2) 

            if random_obstacle == 0:            
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random_obstacle == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random_obstacle == 2:
                self.obstacles.append(Bird(BIRD))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)    #mover para esquerda e deleta.
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
