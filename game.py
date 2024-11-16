import pygame
import pygame_gui

from networkManager import NetworkManager
from variables import *
from map import Map
from gui import GUI

class Game:
    tile_map = None
    score = 0
    lives = 3
    guessed_correct = False

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Height Guesser")

        self.window_size = (MAP_WIDTH * TILE_SIZE + SIDEBAR_WIDTH, MAP_HEIGHT * TILE_SIZE)
        self.screen = pygame.display.set_mode(self.window_size)

        self.network_manager = NetworkManager()

        #self.tile_map = Map(self, "map3")
        self.change_map()

        self.gui = GUI(self, self.screen, self.window_size, (self.tile_map.width * TILE_SIZE, 0))

        #self.tile_map.draw_map(self.screen)

        self.clock = pygame.time.Clock()

        self.running = True

    def change_map(self):
        content = self.network_manager.get_new_map_str()
        self.tile_map = Map(self, content, True)
        self.tile_map.draw_map(self.screen)
        self.guessed_correct = False

    def lose_life(self):
        if self.guessed_correct:
            return
        self.lives -= 1
        if self.lives == 0:
            self.running = False
        self.gui.display_lives_text(self.lives)

    def gain_score(self):
        if self.guessed_correct:
            return
        self.score += 1
        self.gui.display_score_text(self.score)
        self.guessed_correct = True

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                    continue

                self.gui.process_events(event)

                if self.gui.handle_ui_event(event):
                    continue

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    world_pos = (mouse_pos[0]//TILE_SIZE, mouse_pos[1]//TILE_SIZE)
                    self.tile_map.handle_click(world_pos)

            self.gui.update(time_delta)

        pygame.quit()