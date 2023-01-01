from handler import Handler
import pygame
from assets import Assets
from gameState import GameState
from menuState import MenuState
# from gameDisplayer import GameDisplayer
pygame.init()


class Game:

    def __init__(self):
        # pygame.display.set_caption("FAST CRUSH !")
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.WIDTH, self.HEIGHT = self.WIN.get_size()
        # self.WIN = pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(
        #     0, 60, self.WIDTH, self.HEIGHT - 120))
        # self.WIDTH = self.Surface.get_width()  # 900
        # self.HEIGHT = self.Surface.get_height()  # 480  # 500
        # self.BLACK = (0, 0, 0)
        self.dest = (100, 100)
        self.handler = Handler(self)
        # should be before any other object that have handler in its constr.
        # Handler(self) current instance in the current class

        self.assets = Assets(self.handler)
        self.menuState = MenuState(self.handler)
        self.menuState.initializer()
        self.gameState = GameState(self.handler)
        self.gameState.initializer()
        self.currentState = self.menuState
        # self.currentState = self.gameState

    # draw everything here:
    def draw_window(self):
        self.WIN.fill(self.WHITE)

        self.currentState.draw()

        pygame.draw.rect(self.WIN, self.BLACK, pygame.Rect(
            0, 0, self.handler.game.WIDTH, 60))
        pygame.draw.rect(self.WIN, self.BLACK, pygame.Rect(
            0, self.handler.game.HEIGHT - 60, self.handler.game.WIDTH, 60))

        # end of drawing
        pygame.display.update()

    def tick(self):
        self.currentState.tick()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.FPS)
            self.handler.inputManager.tick()
            self.tick()
            self.draw_window()
