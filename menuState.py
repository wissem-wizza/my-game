import pygame
import sys
import math
# from animation import Animation
# from heroesList import *


class MenuState():

    def __init__(self, handler):
        self.handler = handler
        self.WIN = self.handler.game.WIN
        self.center = self.WIN.get_rect().center
        self.WHITE = (255, 255, 255)
        self.alpha = 1

    def initializer(self):
        self.handler.initializer()
        # self.handler.soundManager.init()
        # self.handler.soundManager.play('menu_state')
        self.assets = self.handler.game.assets
        self.assets.initAssets()

        self.newGame_rect = self.rect_pos(self.assets.newGame, 2.5, 10)
        self.options_rect = self.rect_pos(self.assets.options, 2.5, 2.5)
        self.quit_rect = self.rect_pos(self.assets.quit, 2.5, 4)
        self.right_rect = self.rect_pos(self.assets.right, 1.3, 5)
        self.left_rect = self.rect_pos(self.assets.left, 7, 5)
        self.start_rect = self.rect_pos(self.assets.start, 2.6, 1.8)
        self.back_rect = self.rect_pos(self.assets.back, 2.6, 1.4)
        # self.pg_rect = self.rect_pos(self.assets.pygame, 2.6, 1.4)

        # self.heroes = [Animation(self.handler.game.assets.heroknight[0], 0.07),
        #                Animation(self.handler.game.assets.evilwizard[0], 0.07),
        #                Animation(self.handler.game.assets.ronin[0], 0.07)]
        # self.currentAnimation = self.heroes[0]
        # self.choosenHero = self.heroes.index(self.currentAnimation)
        # self.rect = self.currentAnimation.frames[0].get_rect()
        # self.offset = (0, 0)
        # self.rect.x = 300 + self.assets.grid.get_rect().w / 2 - self.rect.w / 2
        # self.rect.y = 0 + self.assets.grid.get_rect().h / 2 - self.rect.h / 2

        font = pygame.font.SysFont(None, 34)
        self.text = font.render('press Enter to start', True, (0, 0, 255))

        self.displayer = {
            "pygame": True,
            "entry": False,
            "launch": False,
            "newgame": False,
            "options": False
        }

    def pg_alpha(self, alpha):
        for curr_alpha in range(1, alpha + 1):
            self.assets.pygame.set_alpha(curr_alpha)
            pg_center = self.assets.pygame.get_rect().center
            self.WIN.blit(self.assets.pygame,
                          (self.center[0] - pg_center[0], self.center[1] - pg_center[1]))
            pygame.display.update()
            if curr_alpha == 1:
                pygame.time.delay(500)
            else:
                pygame.time.delay(20)
            curr_alpha += 1
            self.alpha = curr_alpha

    def elements_draw(self, elements):
        for i in elements:
            self.WIN.blit(i[0], i[1])

    def screen_draw(self, screen_name):
        # if screen_name != "pygame":

        if screen_name == "pygame":
            self.WIN.fill(self.WHITE)
            self.pg_alpha(100)
        if screen_name == "entry":
            self.elements_draw([[self.assets.background, (0, 60)],
                                [self.text, (600, 600)]])
        if screen_name == "launch":
            self.elements_draw([[self.assets.background, (0, 60)],
                                [self.assets.newGame, self.newGame_rect],
                                [self.assets.quit, self.quit_rect],
                                [self.assets.options, self.options_rect]])
        elif screen_name == "newgame":
            self.elements_draw([[self.assets.background, (0, 60)],
                                [self.assets.grid, (300, 0)],
                                [self.assets.start, self.start_rect],
                                [self.assets.back, self.back_rect],
                                [self.assets.right, self.right_rect],
                                [self.assets.left, self.left_rect],
                                # [self.currentAnimation.getCurrentFrame(), (self.rect.x - self.offset[0], self.rect.y - self.offset[1])]
                                ])
        elif screen_name == "options":
            self.elements_draw([[self.assets.background, (0, 60)],
                                [self.assets.back, self.back_rect]])

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
        if self.displayer["pygame"]:
            if self.alpha == 101:
                self.switch_displayer("entry")
        if self.displayer["entry"]:
            if self.handler.inputManager.pressed.get(pygame.K_KP_ENTER) or self.handler.inputManager.pressed.get(pygame.K_RETURN):
                # print("pressed")
                self.switch_displayer("launch")
        if self.displayer["launch"]:
            if self.check_clicked_button(self.newGame_rect):
                self.switch_displayer("newgame")

            elif self.check_clicked_button(self.options_rect):
                self.switch_displayer("options")

            elif self.check_clicked_button(self.quit_rect):
                pygame.quit()
                print('game closed')
                sys.exit()

        elif self.displayer["newgame"]:

            if self.check_clicked_button(self.right_rect):
                return
                # print("right")
                # self.choosenHero += 1
                # if self.choosenHero >= len(self.heroes):
                #     self.choosenHero = 0

            if self.check_clicked_button(self.left_rect):
                return
                # print("left")
                # self.choosenHero -= 1
                # if self.choosenHero < 0:
                #     self.choosenHero = len(self.heroes) - 1

            # self.currentAnimation = self.heroes[self.choosenHero]

            if self.check_clicked_button(self.start_rect):
                # self.handler.game.gameState.gameDisplayer.player.hero = self.playerHero()
                # self.handler.characterManager.characterGroup.add(
                #     self.handler.game.gameState.gameDisplayer.player.hero)
                self.handler.game.currentState = self.handler.game.gameState
                print("game start")
                # return

            if self.check_clicked_button(self.back_rect):
                self.switch_displayer("launch")

        elif self.displayer["options"] == True:
            if self.check_clicked_button(self.back_rect):
                self.switch_displayer("launch")

    # def playerHero(self):
    #     if self.choosenHero == 0:
    #         return HeroKnight(self.handler)
    #         # self.rect.x = 400
    #         # self.rect.y = 100

    #     elif self.choosenHero == 1:
    #         return EvilWizard(self.handler)
    #         # self.rect.x = 320
    #         # self.rect.y = 0.5

    #     elif self.choosenHero == 2:
    #         return Ronin(self.handler)
    #         # self.rect.x = 320
    #         # self.rect.y =50

    # def hero_offset(self):
    #     if self.currentAnimation == self.heroes[0]:
    #         self.offset = (0, 0)
    #     if self.currentAnimation == self.heroes[1]:
    #         self.offset = (80, 100)
    #     if self.currentAnimation == self.heroes[2]:
    #         self.offset = (-15, -10)
    #     return self.offset

    def rect_pos(self, button, a, b):
        button_rect = button.get_rect()
        button_rect.x = math.ceil(self.WIN.get_width()/a)
        button_rect.y = math.ceil(self.handler.game.WIN.get_height()/b + 60)
        return button_rect

    def draw(self):
        currentdisplayer = ""
        for k, v in self.displayer.items():
            if v == True:
                currentdisplayer = k
        self.screen_draw(currentdisplayer)

    def tick(self):
        self.current_tick()
        # self.hero_offset()
        # self.currentAnimation.tick()
