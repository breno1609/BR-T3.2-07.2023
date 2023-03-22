from dino_runner.utils.constants import SCREEN_WIDTH


class CloudComportament:
    def __init__(self, image): #O modulo cactus.py traz para seu "pai" as imagens, num aleatorio, POS_Y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def draw(self, screen):
            screen.blit(self.image, (self.rect.x, self.rect.y))
  
    def update(self, game_speed, clouds):
        self.rect.x -= game_speed    

        if self.rect.x < -self.rect.width:
            clouds.pop()


class Cloud(CloudComportament):
    def __init__(self, images):
        super().__init__(images)
        
        self.rect.y = 90