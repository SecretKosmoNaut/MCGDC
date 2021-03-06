import pygame

def animate(player):
        walking_frames = 4
        current_frame = player.timer.elapsed_time

        if not player.moving_right and not player.moving_left:
            player.image = pygame.image.load('images/megaman/stand.png')

        if player.moving_right:
            player.timer.update()

            if player.facing_left:
                player.facing_left = False

            if current_frame > 0.6:
                player.image = pygame.image.load('images/megaman/walk4.png')
            elif current_frame > 0.4:
                player.image = pygame.image.load('images/megaman/walk3.png')
            elif current_frame > 0.2:
                player.image = pygame.image.load('images/megaman/walk2.png')
            else:
                player.image = pygame.image.load('images/megaman/walk1.png')

        if player.moving_left:
            player.timer.update()

            if not player.facing_left:
                player.facing_left = True

            if current_frame > 0.6:
                player.image = pygame.image.load('images/megaman/walk4.png')
            elif current_frame > 0.4:
                player.image = pygame.image.load('images/megaman/walk3.png')
            elif current_frame > 0.2:
                player.image = pygame.image.load('images/megaman/walk2.png')
            else:
                player.image = pygame.image.load('images/megaman/walk1.png')

        if player.jumping:
            player.image = pygame.image.load('images/megaman/jump.png')

        if player.facing_left:
            player.image = pygame.transform.flip(player.image, True, False)
        else:
            player.image = pygame.transform.flip(player.image, False, False)
