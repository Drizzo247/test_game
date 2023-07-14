
import pygame; pygame.init()
from sys import exit




screen = pygame.display.set_mode((800,400))

#set's tittle
pygame.display.set_caption('Drizzo')
#Imporant
clock = pygame.time.Clock() #Clock obj that controls fps

#how the letter look
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


#background
background=pygame.image.load("assets/mbackground.png").convert_alpha()
ground=pygame.image.load("assets/ground2.png").convert_alpha()

snail_surface = pygame.image.load("assets/snail1.png").convert_alpha()
snail_rec = snail_surface.get_rect( bottomright=(600,300))

player_surface = pygame.image.load("assets/player_walk_1.png").convert_alpha()
player_retc = player_surface.get_rect( midbottom=(80,300))


player_gravity = 0
game_active = True
mouse_pos = pygame.mouse.get_pos()



while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

            #key input

        if event.type == pygame.K_SPACE: player_gravity = 2
        player_retc.y += player_gravity


        if event.type == pygame.MOUSEBUTTONDOWN:player_gravity = -20
        if player_retc.collidepoint(80, 300):player_retc.y += player_gravity





    screen.blit(background,(0,0))    # Add surface to the screen.
    screen.blit(ground,(0,300))


    if game_active:


        snail_rec.x -=1
        screen.blit(snail_surface,(snail_rec))
        player_retc.left += 1
        if snail_rec.right <= 0: snail_rec.left = 800
                                    #left #right

        #player
        def player(*args):
            screen.blit(player_surface, player_retc)


            player_retc.y += player_gravity
            if player_retc.bottom >= 300:
                player_retc.bottom = 300
            screen.blit(player_surface, player_retc)
        player()




        #draw all our elements/updates everything
        pygame.display.update()

        #collision
        if snail_rec.colliderect(player_retc):
            screen.fill('Yellow')
            game_active = False




    clock.tick(60)

#import sound MAKE SURE TO MAKE S CAPTIOAL
pygame.mixer.Sound('')
