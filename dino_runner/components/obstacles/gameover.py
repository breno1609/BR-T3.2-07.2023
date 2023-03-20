import pygame

class GameOver:
    def __init__(self):
        self.x = 500
        self.y = 300
        self.font = pygame.font.SysFont('Arial Black', 40)
        self.text = " "

    def draw(self, screen):
        self.text = self.font.render('Game Over!', True, ((0, 0, 0)))
        screen.blit(self.text, (self.x, self.y))
        pygame.time.wait(1000)