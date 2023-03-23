import pygame
import random
from dino_runner.components.obstacles.cactus import *
from dino_runner.components.obstacles.bird import *
from dino_runner.components.obstacles.moedas import *
from dino_runner.utils.constants import * 
from dino_runner.components.obstacles.gameover import *
from dino_runner.components.obstacles.cloud import *




class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.clouds = []

    def update(self, game):


        if len(self.obstacles) == 0: 
            random_obstacle = random.randint(0, 4) 

            if random_obstacle == 0:   
                self.obstacles.append(Cactus(SMALL_CACTUS)) 
            elif random_obstacle == 1: 
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random_obstacle == 2: 
                self.obstacles.append(Bird(BIRD))
            elif random_obstacle == 3:
                self.obstacles.append(Moedas(MOEDAS))
            elif random_obstacle == 4:
                self.obstacles.append(Bird(BIRD2))
        
        if len(self.clouds) == 0:
            self.clouds.append(Cloud(CLOUD))


        for obstacle in self.obstacles: 
            obstacle.update(game.game_speed, self.obstacles)  
            if game.player.dino_rect.colliderect(obstacle.rect): 
                pygame.time.delay(500) 
                game.playing = False 
                game.death_count += 1
                break 
        
        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)
            
    
    def draw(self, screen):
        for obstacle in self.obstacles: #PARA CADA OBJETO DENTRO DA LISTA
            obstacle.draw(screen) #DESENHA O OBJETO NA TELA
        
        for cloud in self.clouds:
            cloud.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles.clear()