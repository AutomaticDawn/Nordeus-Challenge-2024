import pygame
import pygame_gui

from colour import Color

from networkManager import NetworkManager
from variables import *

class GUI:
    def __init__(self, game, screen, window_size, top_left):
        self.game = game
        self.screen = screen
        self.window_size = window_size
        self.top_left = top_left
        self.y = top_left[1]

        self.manager = pygame_gui.UIManager(self.window_size)

        pygame.font.init()
        self.my_font = pygame.font.SysFont('freesansbold', FONT_SIZE)

        gui_rect = pygame.Rect(top_left[0], top_left[1], SIDEBAR_WIDTH, self.window_size[1])
        grey_rgb = Color("grey").rgb
        self.grey = (grey_rgb[0] * 255, grey_rgb[1] * 255, grey_rgb[2] * 255)
        pygame.draw.rect(self.screen, self.grey, gui_rect)

        #description
        self.y += BUFFER
        text_surface = self.my_font.render('Height', False, (0, 0, 0))
        self.screen.blit(text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE

        text_surface = self.my_font.render('Guesser', False, (0, 0, 0))
        self.screen.blit(text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE + BUFFER * 3

        text_surface = self.my_font.render('Click', False, (0, 0, 0))
        self.screen.blit(text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE

        text_surface = self.my_font.render('The Island', False, (0, 0, 0))
        self.screen.blit(text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE

        text_surface = self.my_font.render('With The', False, (0, 0, 0))
        self.screen.blit(text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE

        text_surface = self.my_font.render('Highest', False, (0, 0, 0))
        self.screen.blit(text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE

        text_surface = self.my_font.render('Average', False, (0, 0, 0))
        self.screen.blit(text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE

        text_surface = self.my_font.render('Height', False, (0, 0, 0))
        self.screen.blit(text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE + BUFFER * 3

        self.score_text_surface = self.my_font.render('Score: 0', False, (0, 0, 0))
        self.score_text_surface_y = self.y
        self.screen.blit(self.score_text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE + BUFFER * 3

        self.lives_text_surface = self.my_font.render('Lives: 3', False, (0, 0, 0))
        self.lives_text_surface_y = self.y
        self.screen.blit(self.lives_text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE + BUFFER * 3

        self.state_text_surface = self.my_font.render('---', False, (0, 0, 0))
        self.state_text_surface_y = self.y
        self.screen.blit(self.state_text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.y))
        self.y += FONT_SIZE + BUFFER * 3

        self.test_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(top_left[0], self.y, BUTTON_WIDTH, BUTTON_HEIGHT), text="Get new map", manager=self.manager)
        self.y += BUTTON_HEIGHT + BUFFER


    def process_events(self, event):
        self.manager.process_events(event)

    def update(self, time_delta):
        self.manager.update(time_delta)
        self.manager.draw_ui(self.screen)
        pygame.display.update()

    def handle_ui_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.test_btn:
                self.game.change_map()
                #print("New map")
                return True

        return False

    def display_win_text(self):
        self.state_text_surface = self.my_font.render('Correct    ', False, (20, 220, 20), self.grey)
        self.screen.blit(self.state_text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.state_text_surface_y))

    def display_lose_text(self):
        self.state_text_surface = self.my_font.render('Incorrect', False, (220, 20, 20), self.grey)
        self.screen.blit(self.state_text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.state_text_surface_y))

    def display_sea_text(self):
        self.state_text_surface = self.my_font.render('Sea :(      ', False, (20, 20, 220), self.grey)
        self.screen.blit(self.state_text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.state_text_surface_y))

    def display_score_text(self, lives):
        self.score_text_surface = self.my_font.render('Score: ' + str(lives) + "  ", False, (0, 0, 0), self.grey)
        self.screen.blit(self.score_text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.score_text_surface_y))

    def display_lives_text(self, lives):
        self.lives_text_surface = self.my_font.render('Lives: ' + str(lives) + "  ", False, (0, 0, 0), self.grey)
        self.screen.blit(self.lives_text_surface, (self.top_left[0] + TEXT_X_OFFSET, self.lives_text_surface_y))



