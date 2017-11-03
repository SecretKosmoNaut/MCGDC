import pygame
import time
from timer import Timer

class Megaman():

    def __init__(self, screen):
        """Initialize Mega Man and his starting position."""

        self.screen = screen
        self.image = pygame.image.load('images/megaman/stand.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start Mega Man on the left-bottom side of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag and attributes.
        self.speed = .003
        self.timer = Timer()
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the player animation and positon based on flags."""
        if self.moving_right:
            self.rect.centerx += 1
            time.sleep(self.speed)
        elif self.moving_left:
            self.rect.centerx -= 1
            time.sleep(self.speed)

    def blitme(self):
        """Draws Mega Man at his current location."""
        self.update()
        self.screen.blit(self.image, self.rect)
