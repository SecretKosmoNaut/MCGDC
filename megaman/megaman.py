import sys
import pygame
import time
import game_functions as gf
from animation import animate
from settings import Settings
from player import Megaman

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption("Mega Man")
    player = Megaman(screen)

    while True:
        gf.check_events(player)
        animate(player)
        gf.update_screen(screen, settings, player)

run_game()
