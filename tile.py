from functools import reduce

import pygame

from variables import TILE_SIZE


class Tile:
    screen = None

    def __init__(self, x, y, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.default_color = color
        self.color = color
        self.island = None

    def select(self):
        red = self.default_color[0] * 1.25
        if red > 255:
            red = 255
        green = self.default_color[1] * 1.25
        if green > 255:
            green = 255
        blue = self.default_color[2] * 1.25
        if blue > 255:
            blue = 255

        self.color = (red, green, blue)
        self.redraw()

    def deselect(self):
        self.color = self.default_color
        self.redraw()

    def redraw(self, screen = None):
        if screen is not None:
            self.screen = screen
        tile_rect = pygame.Rect(int(self.x * TILE_SIZE), int(self.y * TILE_SIZE), TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(self.screen, self.color, tile_rect)
