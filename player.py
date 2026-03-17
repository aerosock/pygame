import pygame
from utility import imagecutter

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 150
        self.y = 150
        self.spritesheet = pygame.image.load('assets/64X128_Runing_Free.png').convert_alpha()
        self.image = imagecutter(self.spritesheet, 0, 0, 64, 128, 1)
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
        self.index = 0
        self.speed = 5
        self.lives = 3
        self.invulnurability = False

    def animation(self, direction):
        framecount = 3
        if self.index >= framecount:
            self.index = 0
        self.image = imagecutter(self.spritesheet, self.index, direction, 64, 128, 1)

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.animation(2)
            self.rect.move_ip(self.speed, 0)
        elif key[pygame.K_LEFT]:
            self.animation(1)
            self.rect.move_ip(-self.speed, 0)
        elif key[pygame.K_UP]:
            self.animation(3)
            self.rect.move_ip(0, -self.speed)
        elif key[pygame.K_DOWN]:
            self.animation(0)
            self.rect.move_ip(0, self.speed)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)