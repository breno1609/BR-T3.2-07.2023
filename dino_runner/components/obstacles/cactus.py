import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle): #HERDA DA CLASSE OBSTACULOS
    def __init__(self, images): #MEOTOD CONSTRUTOR, QUE VAI RECEBER AS IMAGENS COMO PARAMETRO
        self.type = random.randint(0,2) #VAI SORTEAR UM NUMERO, PARA SABER QUAL CACTO VAI APARECER
        super().__init__(images, self.type)
        
        self.rect.y = 325 #POSIÇÃO ONDE O CACTU VAI APARECER


class LargeCactus(Obstacle): #HERDA DA CLASSE OBSTACULOS
    def __init__(self, images): #VAI SORTEAR UM NUMERO, PARA SABER QUAL CACTO VAI APARECER
        self.type = random.randint(0,2) #MEOTOD CONSTRUTOR, QUE VAI RECEBER AS IMAGENS COMO PARAMETRO
        super().__init__(images, self.type)
        
        self.rect.y = 300  #POSIÇÃO ONDE O CACTU VAI APARECER 