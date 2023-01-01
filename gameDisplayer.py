import pygame
from player import Player
# from versusPlayer import VersusPlayer
from world import World
# from enemiesList import *
# from enemyController import EnemyController
from heroesList import *
# from gameObject import GameObject
# from gameCamera import GameCamera


class GameDisplayer():

    def __init__(self, handler):
        self.handler = handler
        self.WIN = self.handler.game.WIN

        self.player = Player(self.handler)

        ## just for test ##
        self.player.hero = HeroKnight(self.handler)
        self.handler.characterManager.characterGroup.add(
            self.player.hero)
        ##################
        self.world_1 = World(self.handler, self.player.hero, "Assets/parallax/ground.png", [
            "parallax/plx-1.png", "parallax/plx-2.png", "parallax/plx-3.png", "parallax/plx-4.png", "parallax/plx-5.png"])
        # self.world_1.initializer()
        self.current_world = self.world_1

    def initializer(self):
        self.handler.initializer()
        self.assets = self.handler.game.assets
        self.assets.initAssets()
        # self.camera = GameCamera(self.handler)
        # self.stairGroup = pygame.sprite.Group()
        # self.stair1 = GameObject(self.handler,'stairFL', 185,242)
        # self.stairGroup.add(self.stair1, self.stair2, self.stair3, self.stair4)

        # self.win_x_center = self.handler.game.WIDTH/2
        # self.win_y_center = self.handler.game.HEIGHT/2
        # self.victory = GameObject(self.handler,'victory', self.win_x_center, self.win_y_center)
        # self.defeat = GameObject(self.handler,'defeat', self.win_x_center,self.win_y_center)

        # , "battle_arena.png"
        # self.world_1 = World(self.handler)

        # self.world_1 = World(self.handler, "Assets/parallax/ground.png", [
        #     "parallax/plx-1.png", "parallax/plx-2.png", "parallax/plx-3.png", "parallax/plx-4.png", "parallax/plx-5.png"])
        # # self.world_1.initializer()
        # self.current_world = self.world_1

        # self.player = Player(self.handler)

        # ## just for test ##
        # self.player.hero = HeroKnight(self.handler)
        # self.handler.characterManager.characterGroup.add(
        #     self.player.hero)
        # ##################

        # self.tower_1 = Tower(self.handler)
        # self.tower_1.controller = EnemyController(self.handler, self.tower_1)
        # self.handler.characterManager.enemy_spawn(self.tower_1, 25, -20)

        # self.tower_2 = Tower(self.handler)
        # self.tower_2.controller = EnemyController(self.handler, self.tower_2)
        # self.handler.characterManager.enemy_spawn(self.tower_2, 3700, 0)

        # self.minotaur_1 = Minotaur(self.handler)
        # self.minotaur_1.controller = EnemyController(
        #     self.handler, self.minotaur_1)
        # self.handler.characterManager.enemy_spawn(self.minotaur_1, 700, 250)

        # self.skeleton_1 = Skeleton(self.handler)
        # self.skeleton_1.controller = EnemyController(
        #     self.handler, self.skeleton_1)
        # self.handler.characterManager.enemy_spawn(self.skeleton_1, 1000, 250)

        # self.evil = EvilWizard(self.handler)
        # self.versusPlayer = VersusPlayer(self.handler, self.evil)

        # # self.heroknight = HeroKnight(self.handler)
        # # self.heroknight.controller = EnemyController(self.handler, self.heroknight)
        # # self.handler.characterManager.enemy_spawn(self.heroknight, 2500, 250)

    def tick(self):
        # print("game state tick")
        # return
        self.current_world.tick()  # include characterManager
        self.player.tick()
        # # self.stair1.tick()
        # # self.versusPlayer.tick()

    def draw(self):
        self.current_world.draw()
        # self.stair1.draw()
        self.player.draw()
        # if self.tower_2.dead and self.tower_2.rightDeathAnimation.index > 15:
        #     self.handler.game.WIN.blit(
        #         self.victory.image, (75 - self.camera.xOffset, 0 - self.camera.yOffset))
        # if self.tower_1.dead and self.tower_1.rightDeathAnimation.index > 15:
        #     self.handler.game.WIN.blit(
        #         self.defeat.image, (75 - self.camera.xOffset, -10 - self.camera.yOffset))
        # # self.versusPlayer.tick()
