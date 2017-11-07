import pygame
import time
from timer import Timer
from player_actions import Actions

class Megaman():

    def __init__(self, screen):
        """Initialize Mega Man and his starting position."""

        self.screen = screen
        self.image = pygame.image.load('images/megaman/stand.png')
        self.timer = Timer()
        self.action = Actions(self)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom

        # Movement flags and attributes.
        self.speed = .003
        self.moving_right = False
        self.moving_left = False
        self.facing_left = False
        self.jumping = False

    def update(self):
        """Update the player animation and positon based on flags."""
        if self.moving_right:
            self.rect.centerx += 1
            time.sleep(self.speed)
        elif self.moving_left:
            self.rect.centerx -= 1
            time.sleep(self.speed)

        if self.jumping and not self.action.jump_init:
            print("Sending to jump: ")      # Debug
            print(self.rect.bottomleft)     # Debug
            print()                         # Debug

            self.action.jump(self.rect.bottomleft)
        elif self.jumping and self.action.jump_init:
            self.action.jump((0,0))

    def blitme(self):
        """Draws Mega Man at his current location."""
        self.update()
        self.screen.blit(self.image, self.rect)
