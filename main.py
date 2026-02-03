# Example file showing a basic pygame "game loop"
import pygame
from sys import exit
SCREEN_HEIGHT = 600 #caps lock oznacuje konstanty
SCREEN_WIDTH = 800

# pygame setup
pygame.init()
player_lives = 10
def monsteranim():
    global monster_index, monster_surf
    monster_index += 0.1    
    if monster_index >= len(monsterpics):
        monster_index = 0
    monster_surf = monsterpics[int(monster_index)]

    
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
player = pygame.Rect((50, 100, 50, 50))  # x, y, width, height
player_speed = 5


monster_idle = pygame.image.load('TheGuyStandard.png').convert_alpha()
monster_idle = pygame.transform.scale(monster_idle, (monster_idle.get_width()*4, monster_idle.get_height()*4))
monster_run1 = pygame.image.load('TheGuyrunning1.png').convert_alpha()
monster_run1 = pygame.transform.scale(monster_run1, (monster_run1.get_width()*4, monster_run1.get_height()*4))
monster_run2 = pygame.image.load('TheGuyrunning2.png').convert_alpha()
monster_run2 = pygame.transform.scale(monster_run2, (monster_run2.get_width()*4, monster_run2.get_height()*4))

monsterpics = [monster_idle, monster_run1, monster_run2]
monster_index = 0
monster_surf = monsterpics[monster_index]

monster_x = 50
monster_y = 300
monster_speed = 5
monster_rect = monster_surf.get_rect(midbottom = (monster_x, monster_y)) 
# game loop
time = 0
lasttime = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        player.move_ip(player_speed, 0)
    elif key[pygame.K_LEFT]:
        player.move_ip(-player_speed, 0)
    elif key[pygame.K_UP]:
        player.move_ip(0, -player_speed)
    elif key[pygame.K_DOWN]:
        player.move_ip(0, player_speed)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    monster_rect.right += monster_speed
    monsteranim()
    if monster_rect.left > SCREEN_WIDTH:
        monster_speed = -monster_speed
    if monster_rect.right < 0:
        monster_speed = -monster_speed
    # RENDER YOUR GAME HERE
    screen.blit(monster_surf, monster_rect)
    pygame.draw.rect(screen, (255, 0, 0), player)
    # flip() the display to put your work on screen
    time += clock.get_time()
    if player.colliderect(monster_rect):
            if time - lasttime > 2000:
                lasttime = time
                player_lives -= 1
                print(player_lives)
             

    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()