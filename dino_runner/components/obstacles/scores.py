import pygame

class Scores: #VAI FAZER A CONTAGEM DOS PONTOS
    def __init__(self):
        self.font = pygame.font.SysFont('Arial Black', 30)
        self.pontos = 0 #INICIALMENTE COMEÇA COM 0 E VAI SOMANDO A CADA FRAME
        self.x = 100 #POSIÇÃO DE X NA TELA
        self.y = 10 #POSIÇÃO DE Y NA TELA
        self.text = ' ' #VARIAVEL QUE VAI GUARDAR O TEXTO ESCRITO
        self.sound_effect = pygame.mixer.Sound('dino_runner/assets/sons/score_sound.wav') #VARIAVEL DE SOM

    def draw(self, screen):
        self.pontos += 1 #VAI SOMANDO +1 A CADA FRAME PERCODDIO PELO DINOSAURO
        self.text = self.font.render('Pontos: ' + str(self.pontos), True, ((0, 0, 0,))) #IMPRIME OS PONTOS NA TELA
        screen.blit(self.text, (self.x, self.y))

        if self.pontos % 100 == 0: #A CADA 100 PONTOS, VAI EMITIR UM SOM. SE O NUMERO FOR DIVISIVEL POR 100 E RESTAR 0
            self.sound_effect.play()
        