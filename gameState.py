import pygame
import sys
import math
from gameDisplayer import GameDisplayer


class GameState():

    def __init__(self, handler):
        self.handler = handler

    def initializer(self):
        self.handler.initializer()
        self.assets = self.handler.game.assets
        self.assets.initAssets()
        self.gameDisplayer = GameDisplayer(self.handler)
        self.gameDisplayer.initializer()
        self.displayer = {
            "game": True,
            "pause": False,
            "score": False,
        }
        self.resume_rect = self.rect_pos(self.assets.resume, 2.5, 4)
        self.options_rect = self.rect_pos(self.assets.options, 2.5, 2.5)
        self.quit_rect = self.rect_pos(self.assets.quit, 2.5, 1.4)

    def elements_draw(self, elements):
        for i in elements:
            self.handler.game.WIN.blit(i[0], i[1])

    def rect_pos(self, button, a, b):
        button_rect = button.get_rect()
        button_rect.x = math.ceil(self.handler.game.WIN.get_width()/a)
        button_rect.y = math.ceil(self.handler.game.WIN.get_height()/b)
        return button_rect

    def screen_draw(self, screen_name):
        if screen_name == "pause":
            self.elements_draw([[self.assets.background, (0, 0)],
                                [self.assets.resume, self.resume_rect],
                                [self.assets.quit, self.quit_rect],
                                [self.assets.options, self.options_rect]])
        if screen_name == "game":
            self.gameDisplayer.draw()

    def switch_displayer(self, new_screen):
        for screen in self.displayer.keys():
            self.displayer[screen] = False
        self.displayer[new_screen] = True

    def check_clicked_button(self, button_rect):
        if self.handler.inputManager.clicked:
            if button_rect.collidepoint(self.handler.inputManager.pos):
                return True
        return False

    def current_tick(self):
        if self.displayer["game"]:
            self.gameDisplayer.tick()
            if self.handler.inputManager.pressed.get(pygame.K_KP_ENTER) or self.handler.inputManager.pressed.get(pygame.K_RETURN):
                self.switch_displayer("pause")

        if self.displayer["pause"]:
            if self.check_clicked_button(self.resume_rect):
                self.switch_displayer("game")

            # elif self.check_clicked_button(self.assets.options_rect):
            #     self.switch_displayer("options")

            elif self.check_clicked_button(self.quit_rect):
                self.handler.game.currentState = self.handler.game.menuState
                # pygame.quit()
                # print('game closed')
                # sys.exit()

        elif self.displayer["score"]:
            continu_rect = self.rect_pos(self.continu, 2.5, 4)
            if self.check_clicked_button(continu_rect):
                self.switch_displayer("game")

    def draw(self):
        currentdisplayer = ""
        for key, val in self.displayer.items():
            if val == True:
                currentdisplayer = key
        self.screen_draw(currentdisplayer)

    def tick(self):
        self.current_tick()
