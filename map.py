import pygame

from variables import *
from colour import Color

from tile import Tile
from island import Island

class Map:
    tiles = dict()
    islands = list()

    def __init__(self, map_name):
        self.tile_width = None
        self.tile_height = None
        self.width = None
        self.height = None

        blue = Color('blue')
        green = Color('green')
        yellow = Color('yellow')
        brown = Color('brown')
        white = Color('white')

        self.colors = list(blue.range_to(green, 200))
        self.colors.extend(list(green.range_to(yellow, 300)))
        self.colors.extend(list(yellow.range_to(brown, 250)))
        self.colors.extend(list(brown.range_to(white, 250)))

        file_path = "maps/" + map_name + ".txt"
        file = open(file_path, "r")
        self.generate_map_from_file(file)


    def generate_map_from_file(self, file):
        x = 0
        y = 0

        while True:
            line = file.readline()
            if not line:
                break

            x = 0
            line_heights = line.split(" ")
            for t in line_heights:
                height = int(t)

                color = BLUE
                if height > 0:
                    c = self.colors[height - 1]
                    color = (c.get_red() * 255, c.get_green() * 255, c.get_blue() * 255)

                new_tile = Tile(x, y, height, color)
                self.tiles[(x, y)] = new_tile
                self.determine_island(new_tile)

                #print(str((x,y)) + " = " + str(t))
                x += 1
            y += 1

        self.width = x
        self.height = y


    def determine_island(self, tile):
        if tile.height == 0:
            return
        added = False

        if tile.y > 0:
            up = self.tiles[(tile.x, tile.y-1)]
            if up.height > 0:
                added = True
                up.island.add_tile(tile)

        if tile.x > 0:
            left = self.tiles[(tile.x - 1, tile.y)]
            if left.height > 0:
                if not added:
                    left.island.add_tile(tile)
                else:
                    left.island.merge(tile.island, self)
                added = True

        if added:
            return

        new_island = Island()
        self.islands.append(new_island)
        new_island.add_tile(tile)


    def draw_map(self, screen):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.tiles[(x, y)].redraw(screen)

    def handle_click(self, world_pos):
        for island in self.islands:
            if island.tiles.__contains__(world_pos):
                island.select()
            else:
                island.deselect()
