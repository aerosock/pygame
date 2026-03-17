# Example file showing a basic pygame "game loop"
import pygame
from sys import exit
from settings import *
from utility import imagecutter
from player import Player
from monster import Monster


pygame.init()



# imagecutter(playerspritesheet, 1, 2, 16, 16, 1)


def resetgame():
    global game_state
    player.sprite.lives = 3
    player.sprite.midbottom = (50 ,100)
    game_state = "playing"

game_state = "playing"
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
running = True

font = pygame.font.Font('assets/PixelifySans-Regular.ttf')



 
# game loop
restartbuth = 55
restartbutw = 150
restartbut = pygame.Rect((0, 0, restartbutw, restartbuth))
restartbut.center = (screen_rect.centerx, screen_rect.centery + 50)
restartbtncolor = (0, 255, 0)
restartbtncolorhover = (0, 200, 0)
restartbtntextcolor = (0, 0, 0)

restartbtnfont = pygame.font.Font('assets/PixelifySans-Regular.ttf', 30)
restartbtntext = restartbtnfont.render('Restart', False, restartbtntextcolor)


player = pygame.sprite.GroupSingle()
player.add(Player())
monsters = pygame.sprite.Group()
monsters.add(Monster())
time = 0
lasttime = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if game_state == "gameover":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restartbut.collidepoint(event.pos):
                    resetgame()
             
        
    if game_state == "playing":
        
        screen.fill("black")
        text_lives = font.render(f'Lives: {player.sprite.lives}', False, (255, 255, 255))
        cornerlives = screen.blit(text_lives, (SCREEN_WIDTH - 150, 200))
        monsters.update()
        for monster in monsters:
            monster.drawing(screen)
        player.draw(screen)
        player.update()
        # playerdraw = pygame.draw.rect(screen, (255, 0, 0), playerect)
        # flip() the display to put your work on screen
        time += clock.get_time()
        # if player.sprite.rect.colliderect(monsters.rect):
        #         if time - lasttime > 2000:
        #             lasttime = time
        #             player.sprite.lives -= 1
        #             print(player.sprite.lives)

        # THIS IS COLLISIONS THAT DONT WORK

        if player.sprite.lives <= 0:
            game_state = "gameover"

    elif game_state == "gameover":
        mousepos = pygame.mouse.get_pos()
        
        screen.fill("white")
        gameovertext = font.render(f'u\'ve died bro)', False, "black")
        gameovertextrect = gameovertext.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        gameover = screen.blit(gameovertext, gameovertextrect)
        restartbut = pygame.draw.rect(screen, restartbtncolor, restartbut)
        if restartbut.collidepoint(mousepos):
            restartbut = pygame.draw.rect(screen, restartbtncolorhover, restartbut)
            
        else:
            restartbut = pygame.draw.rect(screen, restartbtncolor, restartbut)

        screen.blit(restartbtntext, restartbtntext.get_rect(topleft = (restartbut.centerx - restartbtntext.get_width()/2, restartbut.centery - restartbtntext.get_height()/2)))

    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()