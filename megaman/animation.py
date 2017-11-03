import pygame

def animate(player):
        if player.moving_right:
            if player.running_time % 2 == 0
            player.image = pygame.image.load('images/megaman/walk1.png')
            player.image = pygame.image.load('images/megaman/walk2.png')

        if not player.moving_right and not player.moving_left:
            player.image = pygame.image.load('images/megaman/stand.png')
