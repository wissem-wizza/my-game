import pygame
from gameCamera import GameCamera


class World():

    def __init__(self, handler, bg_images):
        self.handler = handler
        self.bg_images = []
        self.pathway = []
        self.start_pos = (0, 0)

    def initializer(self):

        self.bg = pygame.image.load(f"Assets/{self.bg_images}").convert()
        # self.bg = pygame.transform.scale(self.bg, (1200, 600))

        self.bg_images.append(self.bg)
        ground_width = self.bg.get_width()
        ground_height = self.bg.get_height()

        self.camera = GameCamera(self.handler)
        self.handler.characterManager.initializer()

        # rect_1 = pygame.Rect(0, 210, 190, 109)  # start
        # rect_2 = pygame.Rect(250, 255, 70, 160)  # little(between 2 stairs)
        line_1 = pygame.Rect(374, 260, 1200, 1)  # the biggest
        # rect_4 = pygame.Rect(self.bg.get_rect().width -
        #                      325, 255, 75, 160)  # little 2
        # rect_5 = pygame.Rect(self.bg.get_rect().width -
        #                      190, 210, 190, 109)  # finish
        # self.bg_images.append(self.bg)
        self.pathway.append(line_1)

        for i in range(1, 6):
            bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
            self.bg_images.append(bg_image)
        self.bg_width = self.bg_images[0].get_width()

    # def parallax(self):
    #     scroll = 0

    #     ground_image = pygame.image.load("ground.png").convert_alpha()
    #     ground_width = ground_image.get_width()
    #     ground_height = ground_image.get_height()

    #     bg_images = []

    #     for i in range(1, 6):
    #         bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
    #         bg_images.append(bg_image)
    #         bg_width = bg_images[0].get_width()

    # def draw_bg(bg_images):
    #     for x in range(5):
    #         speed = 1
    #         for i in bg_images:
    #             return (i, ((x * bg_width) - scroll * speed, 0))
    #         speed += 0.2

    # def draw_ground():
    #     for x in range(15):
    #         screen.blit(ground_image, ((x * ground_width) -
    #                     scroll * 2.5, SCREEN_HEIGHT - ground_height))

    def tick(self):
        # return
        self.handler.characterManager.tick()

    def draw(self):
        # pygame.draw.line(self.handler.game.WIN,
        #                  (255, 255, 255), (40, 780), (80, 720), 4)

        # print("world draw")
        # self.handler.game.WIN.fill((0, 0, 0))
        self.handler.game.WIN.blit(
            self.bg, (0 - self.camera.xOffset, 0 - self.camera.yOffset))
        self.handler.characterManager.draw()
        # for i in range(len(self.pathway)):
        #     pygame.draw.rect(self.handler.game.WIN, (0, 0, 255), (self.pathway[i].x - self.handler.game.gameState.gameDisplayer.current_world.camera.xOffset, self.pathway[i].y - self.handler.game.gameState.gameDisplayer.current_world.camera.yOffset, self.pathway[i].w, self.pathway[i].h), 1)
