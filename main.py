# Example file showing a basic pygame "game loop"
import pygame
from sys import exit
SCREEN_HEIGHT = 600 #caps lock oznacuje konstanty
SCREEN_WIDTH = 800

player_x = 150
player_y = 150
playerindex = 0
# pygame setup
pygame.init()
player_lives = 1
def imagecutter(sheet, x , y, sizex, sizey, scale):
   img = pygame.Surface((sizex, sizey)).convert_alpha()
   img.blit(sheet, (0, 0), ((x*sizex), (y*sizey), sizex, sizey))
   img = pygame.transform.scale(img, (sizex * scale, sizey * scale))
   img.set_colorkey((0, 0, 0))
   return img

def playeranim(direction):
    global playerimg, playerindex
    framecount = 3
    if playerindex >= framecount:
        playerindex = 0
    playerimg = imagecutter(PLAYERSPRITESHEET, playerindex, direction, 64, 128, 1)

# imagecutter(playerspritesheet, 1, 2, 16, 16, 1)
def monsteranim():
    global monster_index, monster_surf
    monster_index += 0.1    
    if monster_index >= len(monsterpics):
        monster_index = 0
    monster_surf = monsterpics[int(monster_index)]

def resetgame():
    global player_lives, playerect, monster_rect, game_state
    player_lives = 1
    playerect.midbottom = (player_x, player_y)
    monster_rect.midbottom = (monster_x, monster_y)
    game_state = "playing"

game_state = "playing"
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
running = True

font = pygame.font.Font('PixelifySans-Regular.ttf', )
PLAYERSPRITESHEET = pygame.image.load('64X128_Runing_Free.png').convert_alpha()
playerimg = imagecutter(PLAYERSPRITESHEET, 0, 0, 64, 128, 1)
playerect = playerimg.get_rect(midbottom = (player_x, player_y))
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
restartbuth = 55
restartbutw = 150
restartbut = pygame.Rect((0, 0, restartbutw, restartbuth))
restartbut.center = (screen_rect.centerx, screen_rect.centery + 50)
restartbtncolor = (0, 255, 0)
restartbtncolorhover = (0, 200, 0)
restartbtntextcolor = (0, 0, 0)

restartbtnfont = pygame.font.Font('PixelifySans-Regular.ttf', 30)
restartbtntext = restartbtnfont.render('Restart', False, restartbtntextcolor)



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
             
        
    key = pygame.key.get_pressed()
    if game_state == "playing":
        if key[pygame.K_RIGHT]:
            playeranim(2)
            playerect.move_ip(player_speed, 0)
        elif key[pygame.K_LEFT]:
            playeranim(1)
            playerect.move_ip(-player_speed, 0)
        elif key[pygame.K_UP]:
            playeranim(3)
            playerect.move_ip(0, -player_speed)
        elif key[pygame.K_DOWN]:
            playeranim(0)
            playerect.move_ip(0, player_speed)
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        text_lives = font.render(f'Lives: {player_lives}', False, (255, 255, 255))
        cornerlives = screen.blit(text_lives, (SCREEN_WIDTH - 150, 200))

        monster_rect.right += monster_speed
        monsteranim()
        if monster_rect.left > SCREEN_WIDTH:
            monster_speed = -monster_speed
        if monster_rect.right < 0:
            monster_speed = -monster_speed
        # RENDER YOUR GAME HERE
        screen.blit(monster_surf, monster_rect)
        playerdraw = screen.blit(playerimg, playerect)
        # playerdraw = pygame.draw.rect(screen, (255, 0, 0), playerect)
        # flip() the display to put your work on screen
        time += clock.get_time()
        if playerect.colliderect(monster_rect):
                if time - lasttime > 2000:
                    lasttime = time
                    player_lives -= 1
                    print(player_lives)

        if player_lives <= 0:
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