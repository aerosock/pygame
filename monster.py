import pygame
from settings import *


class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.idle = pygame.image.load('assets/TheGuyStandard.png').convert_alpha()
        self.idle = pygame.transform.scale(self.idle, (self.idle.get_width()*4, self.idle.get_height()*4))
        self.run1 = pygame.image.load('assets/TheGuyrunning1.png').convert_alpha()
        self.run1 = pygame.transform.scale(self.run1, (self.run1.get_width()*4, self.run1.get_height()*4))
        self.run2 = pygame.image.load('assets/TheGuyrunning2.png').convert_alpha()
        self.run2 = pygame.transform.scale(self.run2, (self.run2.get_width()*4, self.run2.get_height()*4))
        self.pics = [self.idle, self.run1, self.run2]
        self.index = 0
        self.surf = self.pics[self.index]
        self.x = 50
        self.y = 300
        self.speed = 5
        self.rect = self.surf.get_rect(midbottom = (self.x, self.y))


    def monsteranim(self):
        self.index += 0.1    
        if self.index >= len(self.pics):
            self.index = 0
        self.surf = self.pics[int(self.index)]
        
    def update(self):
        self.rect.right += self.speed
        self.monsteranim()
        if self.rect.left > SCREEN_WIDTH:
            self.speed = -self.speed
        if self.rect.right < 0:
            self.speed = -self.speed
        # RENDER YOUR GAME HERE
   
    def drawing(self, screen):
        screen.blit(self.surf, self.rect)
        
    