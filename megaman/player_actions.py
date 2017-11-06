import pygame
import time
import math
import game_functions as gf

def get_coord(player):
    current_coordinates = []
    for i in player.rect.bottomleft:
        current_coordinates.append(i)
    return current_coordinates

class Actions():

    def __init__(self, player):
        """Initialize actions for player class."""
        self.player = player
        self.a = 0
        self.b = 0
        self.c = 0
        self.i = 0
        self.end_coordinates = []
        self.jump_init = False

    def reset(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.i = 0
        self.end_coordinates = []
        self.jump_init = False
        self.player.jumping = False

    def jump(self, initial_coordinates):
        """Basic jumping function. Takes in a tuple with (x,y) coordinates."""

        # Basic Jumping Equation:
        # f(x)=-1/ba^2(x-[b*a+c])^2+b
        # * a = momentum percent
        # * b = maximum height
        # * b * 2 = maximum distance
        # * c = starting x-position
        # * x = current x-position

        current_coordinates = get_coord(self.player)

        if not self.jump_init:
            self.jump_init = True

            self.a = 1.0
            self.b = 64
            self.c = initial_coordinates[0]

            for coord_val in initial_coordinates:
                self.end_coordinates.append(coord_val)

            old_x = self.end_coordinates[0]
            new_x = old_x+self.b*2

            self.end_coordinates[0] = new_x

        if current_coordinates != self.end_coordinates:
            x = current_coordinates[0]
            y = self.end_coordinates[1]

            x += 4
            self.i = math.trunc(-1/self.b*self.a**2*(x-(self.b*self.a+self.c))**2+self.b)

            y -= self.i

            self.player.rect.bottomleft = (x,y)
            print("   Goal - X:%i\tY:%i" % (self.end_coordinates[0], self.end_coordinates[1]))
            print("Current - X:%i\tY:%i" % self.player.rect.bottomleft)
            print(self.i)
            print()
            time.sleep(self.player.speed)
        else:
            print("Done!")
            self.reset()
