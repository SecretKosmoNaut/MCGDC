import pygame
import time

class Timer():

    def __init__(self):
        """Initialize a timer object."""
        self.start_time = 0
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()

    def update(self):
        self.elapsed_time = time.time() - self.start_time

        if self.elapsed_time > 0.8:
            self.start()

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
