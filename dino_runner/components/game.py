import pygame

from dino_runner.utils.constants import *
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.scores import *
from dino_runner.components.obstacles.gameover import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.executing = False
        self.death_count = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.scores = Scores()
        self.gameover = GameOver()
    

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
         # Game loop: events - update - draw
        self.playing = True
        if self.death_count == 0:
            self.reset_game()
        else:
            self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = 20
        self.score = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)       
        
        self.obstacle_manager.update(self)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.scores.draw(self.screen)

        if not self.playing:
            self.gameover.draw(self.screen)
        
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def show_menu(self):
        self.screen.fill((255, 255, 255)) #PINTANDOO A TELA
        half_screen_height = SCREEN_HEIGHT // 2 #MOSTRAR NO MEIO DA TELA
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press (S) to start playing", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_height, half_screen_width)
            self.screen.blit(text, text_rect)
        
        else:
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press (C) to continue playing", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_height, half_screen_width)
            self.screen.blit(text, text_rect)

        pygame.display.update()

        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c]:
                    self.run()