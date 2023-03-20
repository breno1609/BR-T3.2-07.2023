import pygame

class Scores:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial Black', 30)
        self.pontos = 0
        self.x = 100
        self.y = 10
        self.text = ' '
        self.sound_effect = pygame.mixer.Sound('dino_runner/assets/sons/score_sound.wav')

    def draw(self, screen):
        self.pontos += 1
        self.text = self.font.render('Pontos: ' + str(self.pontos), True, ((0, 0, 0,)))
        screen.blit(self.text, (self.x, self.y))

        if self.pontos % 100 == 0:
            self.sound_effect.play()