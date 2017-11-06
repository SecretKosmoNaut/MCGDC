import sys
import pygame

def check_events(player):
    test = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            player.timer.start()
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
            elif event.key == pygame.K_UP:
                player.jumping = True

        elif event.type == pygame.KEYUP:
            player.timer.reset()
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            elif event.key == pygame.K_LEFT:
                player.moving_left = False

def update_screen(screen, settings, *actors):
    screen.fill(settings.bg_color)
    for actor in actors:
        actor.blitme()
    pygame.display.flip()
