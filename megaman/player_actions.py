import pygame

def get_coord(player):
    current_coordinates = []
    for i in player.rect.bottomleft:
        current_coordinates.append(i)
    return current_coordinates

class Actions():

    def __init__(self, player):
        """Initialize actions for player class."""
        self.player = player
        self.jump_start = 0.0
        self.jump_end = 0.0

    def jump(self, initial_coordinates):
        """Basic jumping function. Takes in a tuple with x y coordinates."""

        # Basic Jumping Equation:
        # f(x)=-1/ba^2(x-[b*a+c])^2+b
        # * a = momentum percent
        # * b = maximum height
        # * b * 2 = maximum distance
        # * c = starting x-position
        # * x = current x-position

        current_coordinates = get_coord(self.player)
        print(current_coordinates)
