import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle 


class Bird(Obstacle): #CLASSE BIRD, HERDA A CLASSE OBSTACLE
    def __init__(self, images): #CRIA O CONSTRUTOR E RECEBE AS IMAGENS COMO PARAMETRO
        self.type =0 #VAI REPRESENTAR QUAL IMAGEM USAR DO PASSARINHO
        self.time = 0 #VAI CONTROLAR A BATIDA DE ASAS DO BIRD
        super().__init__(images, self.type) #CHAMA O CONSTRUTOR DA CLASSE PAI E PASSA OS ARGUMENTOS, VAI INICIAR O BIRD COM OS PARAMENTROS DA CLASSE PAI
        self.rect.y = random.randint(200, 260) #VAI DEFINRI OS LOCAIS ALEATORIOS ONDE O PASSARO APARECE

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y)) #VAI DESENHAR NA TELA, O BIRD DE ACORDO COM A POSIÇÃO E A IMAGEM
        self.time += 1 
        if self.time > 12: #ASE FOR MAIOR, MUDA A IMAGEM PARA O BIRD COM ASAS PRA BAIXO, ANIMA O BIRD
            self.type += 1 #VAI MUDAR A IMAGEM DO PAASARO
            self.time = 0 #VAI ZERAR O TEMPO, PRA VOLTAR A CONTAGEM
        if self.type == 2: 
            self.type = 0    

class Bird(Obstacle): #CLASSE BIRD, HERDA A CLASSE OBSTACLE
    def __init__(self, images): #CRIA O CONSTRUTOR E RECEBE AS IMAGENS COMO PARAMETRO
        self.type =0 #VAI REPRESENTAR QUAL IMAGEM USAR DO PASSARINHO
        self.time = 0 #VAI CONTROLAR A BATIDA DE ASAS DO BIRD
        super().__init__(images, self.type) #CHAMA O CONSTRUTOR DA CLASSE PAI E PASSA OS ARGUMENTOS, VAI INICIAR O BIRD COM OS PARAMENTROS DA CLASSE PAI
        self.rect.y = random.randint(200, 260) #VAI DEFINRI OS LOCAIS ALEATORIOS ONDE O PASSARO APARECE

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y)) #VAI DESENHAR NA TELA, O BIRD DE ACORDO COM A POSIÇÃO E A IMAGEM
        self.time += 1 
        if self.time > 12: #ASE FOR MAIOR, MUDA A IMAGEM PARA O BIRD COM ASAS PRA BAIXO, ANIMA O BIRD
            self.type += 1 #VAI MUDAR A IMAGEM DO PAASARO
            self.time = 0 #VAI ZERAR O TEMPO, PRA VOLTAR A CONTAGEM
        if self.type == 2: 
            self.type = 0    