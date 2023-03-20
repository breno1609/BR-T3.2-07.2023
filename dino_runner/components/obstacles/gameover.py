import pygame

class GameOver:
    def __init__(self):
        self.x = 500 #POSIÇÃO DO X
        self.y = 300 #POSIÇÃO DO Y
        self.font = pygame.font.SysFont('Arial Black', 40) #DEFININDO A FONTE QUE SERA UTILIZADA E O TAMANHO
        self.text = " " #CRIOANDO A VARIAVEL DE TEXTO

    def draw(self, screen): #FUNÇÃO PARA DESENHAR NA TELA
        self.text = self.font.render('Game Over!', True, ((0, 0, 0))) #A COR DA LETTRA VAI SER PRETA, E O QUE É ESCRITO É ARMAZENADO NA VARIAVEL TEXT
        screen.blit(self.text, (self.x, self.y)) #POSIÇÃO QUE A FRASE VAI FICAR NA TELA
        pygame.time.wait(1000) #TEMPO DE ESPERA PARA APARECER A IMAGEM