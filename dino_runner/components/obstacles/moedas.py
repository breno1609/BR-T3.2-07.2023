import random
from dino_runner.components.obstacles.obstacle import Obstacle 

class Moedas(Obstacle):
    def __init__(self, images): #images[0,1]
        self.type =0   #Primeira magem na lista
        self.time = 0  #Intervalos para a animação
        super().__init__(images, self.type)
        self.rect.y = random.randint(200, 260)

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y)) #VAI DESENHAR NA TELA, O BIRD DE ACORDO COM A POSIÇÃO E A IMAGEM
        self.time += 1 
        if self.time > 12: #ASE FOR MAIOR, MUDA A IMAGEM PARA O BIRD COM ASAS PRA BAIXO, ANIMA O BIRD
            self.type += 1 #VAI MUDAR A IMAGEM DO PAASARO
            self.time = 0 #VAI ZERAR O TEMPO, PRA VOLTAR A CONTAGEM
        if self.type == 2: 
            self.type = 0 