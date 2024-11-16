import pygame

from variables import *
from colour import Color

from tile import Tile
from island import Island

class Map:
    tiles = dict()
    islands = list()

    highest_island = None

    def __init__(self, game, content, is_content_string = False):
        self.game = game
        self.tile_width = None
        self.tile_height = None
        self.width = None
        self.height = None

        self.tiles.clear()
        self.islands.clear()

        blue = Color('blue')
        green = Color('green')
        yellow = Color('yellow')
        brown = Color('brown')
        white = Color('white')

        self.colors = list(blue.range_to(green, 200))
        self.colors.extend(list(green.range_to(yellow, 300)))
        self.colors.extend(list(yellow.range_to(brown, 250)))
        self.colors.extend(list(brown.range_to(white, 250)))

        if is_content_string:
            self.generate_map_from_string(content)
            self.determine_island_with_highest_average_height()
        else:
            file_path = "maps/" + content + ".txt"
            file = open(file_path, "r")
            self.generate_map_from_file(file)
            self.determine_island_with_highest_average_height()

    def generate_map_from_string(self, content):
        x = 0
        y = 0

        content_list = content.split("\\n")

        while len(content_list)>0:
            line = content_list.pop(0)
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
        #print("Drawing map")
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.tiles[(x, y)].redraw(screen)

    def determine_island_with_highest_average_height(self):
        max_average_height = 0
        for island in self.islands:
            if island.average_height() > max_average_height:
                max_average_height = island.average_height()
                self.highest_island = island
        #print(self.highest_island.average_height())


    def handle_click(self, world_pos):
        win = False
        sea = True
        for island in self.islands:
            if island.tiles.__contains__(world_pos):
                sea = False
                #print(island.average_height())
                if island == self.highest_island:
                    win = True
                    self.game.gui.display_win_text()
                    island.select()
                else:
                    win = False
                    self.game.gui.display_lose_text()
                    island.select()
            else:
                island.deselect()
        if sea:
            self.game.gui.display_sea_text()
        else:
            if win:
                self.game.gain_score()
            else:
                self.game.lose_life()

