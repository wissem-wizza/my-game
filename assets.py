import pygame
import pygame.image
import pygame.transform
import math
from spriteSheet import SpriteSheet


class Assets:

    def __init__(self, handler):
        self.handler = handler

    def initAssets(self):
        self.heroknight = self.parceling(SpriteSheet(
            [["Hero Knight/HeroKnight", 10, 9]], (1, 1)), [8, 18, 24, 0, 46, 48, 58])

        self.background = pygame.image.load("Assets/Menu/menu background.jpg")
        self.background = pygame.transform.scale(
            self.background, (int(1920/2.05), int(1080/2.05)))

        self.grid = pygame.image.load("Assets/Menu/Grid.png")
        self.grid = pygame.transform.scale(self.grid, (300, 246))
        # self.grid.set_alpha(100)

        self.newGame = self.buttons("New game Button.png", 200, 60)
        # self.newGame_rect = self.rect_pos(self.newGame, 2.5, 10)

        self.quit = self.buttons("Quit Button.png", 200, 60)
        # self.quit_rect = self.rect_pos(self.quit, 2.5, 4)

        self.options = self.buttons("options Button.png", 200, 60)
        # self.options_rect = self.rect_pos(self.options, 2.5, 2.5)

        self.start = self.buttons("Start Button.png", 200, 60)
        # self.start_rect = self.rect_pos(self.start, 2.6, 1.8)

        self.back = self.buttons("Back Button.png", 200, 60)
        # self.back_rect = self.rect_pos(self.back, 2.6, 1.4)

        self.right = self.buttons("Next Square Button.png", 50, 50)
        # self.right_rect = self.rect_pos(self.right, 1.3, 5)

        self.left = self.buttons("Back Square Button.png", 50, 50)
        # self.left_rect = self.rect_pos(self.left, 7, 5)

        self.continu = self.buttons("Continue Button.png", 50, 50)
        # self.continu_rect = self.rect_pos(self.continu, 2.5, 4)

        self.resume = self.buttons("Resume Button.png", 200, 60)

    def buttons(self, img, w, h):
        button = pygame.image.load(f"Assets/Menu/{img}")
        button = pygame.transform.scale(button, (w, h))
        return button

    def rect_pos(self, button, a, b):
        button_rect = button.get_rect()
        button_rect.x = math.ceil(self.handler.game.WIN.get_width()/a)
        button_rect.y = math.ceil(self.handler.game.WIN.get_height()/b)
        return button_rect

    def parceling(self, spritesheet, indexes):
        result = []
        res = []
        lastIndex = 0
        frames = spritesheet.strip()
        ignore = False
        for index in indexes:
            if index != 0:
                if not ignore:
                    result.append(frames[0][lastIndex: index])
                    result.append(frames[1][lastIndex: index])
                    lastIndex = index
                    res.append(lastIndex)
                else:
                    ignore = False
                    lastIndex = index - 1
            else:
                ignore = True
        return result  # array of arrays (group of frames)
