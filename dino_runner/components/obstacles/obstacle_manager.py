import pygame
import random
from dino_runner.components.obstacles.cactus import *
from dino_runner.components.obstacles.bird import *
from dino_runner.utils.constants import * 
from dino_runner.components.obstacles.gameover import *



class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):


        if len(self.obstacles) == 0: #SE A LISTA ESTIVER VAZIA
            random_obstacle = random.randint(0, 3) # GERA UM NUMERO ALEATOPIO ENTRE 0 E2, PARA ESCOLHER QUAL OBJETO VAI APARECER NA TELA

            if random_obstacle == 0: #SE O NUMERO SORTEADO FOR 0, VAI APARECER O CACTU PEQUENO      
                self.obstacles.append(Cactus(SMALL_CACTUS)) 
            elif random_obstacle == 1: #SE FOR 1, VAI APARECER O CACTU GRANDE
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random_obstacle == 2: #SE FOR 2, VAI APARECER O PASSARINHO
                self.obstacles.append(Bird(BIRD))


        for obstacle in self.obstacles: #PARA CADA OBSTACULO NA LISTA
            obstacle.update(game.game_speed, self.obstacles)  #CHAMA O METODO UPDATE DE CADA OBJETO, PASSA A VELOCIDADE DO JODO E A LISTA DE OBSTACULOS COMO PARAMETRO
            if game.player.dino_rect.colliderect(obstacle.rect): #VERIFICA SE TEM COLISAO DO DINOSSAURO COM OS OBSTACULOS DA LISTA
                pygame.time.delay(500) #ESPERA ESSE TEMPO PRO JOGADOR PERCEBER QUE COLIDIU
                game.playing = False #ALTERA O ESTADO DO JOGO PARA FALSE
                break #PARA O JOGO
    
    def draw(self, screen):
        for obstacle in self.obstacles: #PARA CADA OBJETO DENTRO DA LISTA
            obstacle.draw(screen) #DESENHA O OBJETO NA TELA
