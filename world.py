import pygame
from gameCamera import GameCamera


class World():

    def __init__(self, handler, hero, background, bg_img):
        self.handler = handler
        self.hero = hero
        self.background = pygame.image.load(background).convert_alpha()
        self.ground_width = self.background.get_width()
        self.ground_height = self.background.get_height()
        self.bg_width_test = self.ground_width*14
        self.bg_images = []
        for i in range(len(bg_img)):
            self.bg_images.append(pygame.image.load(
                "Assets/"+bg_img[i]).convert_alpha())
        self.bg_width = self.bg_images[0].get_width()
        self.pathway = []
        self.start_pos = (0, 0)
        self.scroll = 0
        self.WIN = self.handler.game.WIN
        self.camera = GameCamera(self.handler, self.bg_width_test)

    def parallax(self):
        for x in range(5):
            speed = 1
            for i in self.bg_images:
                self.WIN.blit(
                    i, ((x * self.bg_width) - self.scroll * speed, 0))
                speed += 0.2
        for x in range(15):
            # print("__________________  :  ",
            #       (x * self.ground_width) - self.scroll * 2.5)
            self.WIN.blit(self.background, ((x * self.ground_width) -
                                            self.scroll * 2.5, self.handler.game.HEIGHT - self.ground_height))

    def tick(self):
        self.handler.characterManager.tick()
        if self.hero.moveLeft and self.scroll > 0:
            self.scroll -= 5
        if self.hero.moveRight and self.scroll < 3000:
            self.scroll += 5
        # print(self.scroll)

    def draw(self):
        # self.handler.game.WIN.blit(
        #     self.background, (0 - self.camera.xOffset, 0 - self.camera.yOffset))
        self.parallax()
        self.handler.characterManager.draw()
