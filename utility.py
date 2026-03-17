import pygame

def imagecutter(sheet, x , y, sizex, sizey, scale):
   img = pygame.Surface((sizex, sizey)).convert_alpha()
   img.blit(sheet, (0, 0), ((x*sizex), (y*sizey), sizex, sizey))
   img = pygame.transform.scale(img, (sizex * scale, sizey * scale))
   img.set_colorkey((0, 0, 0))
   return img