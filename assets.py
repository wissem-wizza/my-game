import pygame
import pygame.image
import pygame.transform
import math
from spriteSheet import SpriteSheet


class Assets:

    def __init__(self, handler):
        self.handler = handler

    def initAssets(self):
        self.pygame = pygame.image.load("Assets/pygame_lofi.png")
        self.pg_rect = self.pygame.get_rect()
        self.pygame = pygame.transform.scale(
            self.pygame, (669, 188))  # (self.pg_rect.x, self.pg_rect.y)

        self.heroknight = self.parceling(SpriteSheet(
            [["Hero Knight/HeroKnight", 10, 9]], (1, 1)), [8, 18, 24, 0, 46, 48, 58, 0, 38, 45])

        self.background = pygame.image.load("Assets/Menu/menu background.jpg")
        self.background = pygame.transform.scale(
            self.background, (self.handler.game.WIDTH, self.handler.game.HEIGHT - 120))  # (int(1920/2.05), int(1080/2.05))

        self.grid = pygame.image.load("Assets/Menu/Grid.png")
        self.grid = pygame.transform.scale(self.grid, (300, 246))
        # self.grid.set_alpha(100)

        self.newGame = self.buttons("New game Button.png", 200, 60)
        self.quit = self.buttons("Quit Button.png", 200, 60)
        self.options = self.buttons("options Button.png", 200, 60)
        self.start = self.buttons("Start Button.png", 200, 60)
        self.back = self.buttons("Back Button.png", 200, 60)
        self.right = self.buttons("Next Square Button.png", 50, 50)
        self.left = self.buttons("Back Square Button.png", 50, 50)
        self.continu = self.buttons("Continue Button.png", 50, 50)
        self.resume = self.buttons("Resume Button.png", 200, 60)

    def buttons(self, img, w, h):
        button = pygame.image.load(f"Assets/Menu/{img}")
        button = pygame.transform.scale(button, (w, h))
        return button

    # def rect_pos(self, button, a, b):
    #     button_rect = button.get_rect()
    #     button_rect.x = math.ceil(self.handler.game.WIN.get_width()/a)
    #     button_rect.y = math.ceil(self.handler.game.WIN.get_height()/b)
    #     return button_rect

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
