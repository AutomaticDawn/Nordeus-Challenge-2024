import pygame

from variables import *
from map import Map

class Game:
    def __init__(self):
        pygame.init()

        self.tilemap = Map("map3")

        screen = pygame.display.set_mode((self.tilemap.width * TILE_SIZE, self.tilemap.height * TILE_SIZE))

        self.tilemap.draw_map(screen)

        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    world_pos = (mouse_pos[0]//TILE_SIZE, mouse_pos[1]//TILE_SIZE)
                    #print(world_pos)
                    self.tilemap.handle_click(world_pos)


            pygame.display.update()

        pygame.quit()