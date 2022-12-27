import pygame
# from heroesList import *


class Player:

    def __init__(self, handler):
        self.handler = handler
        self.hero = None
        # self.handler.game.gameState.gameDisplayer.current_world.camera.centerOnEntity(
        # self.hero)

    def keyManager(self):

        if self.handler.inputManager.pressed.get(pygame.K_d):
            self.hero.orderedToAttack = True
        else:
            self.hero.orderedToAttack = False

        if self.handler.inputManager.pressed.get(pygame.K_q):
            self.hero.orderedToJump = True
            # self.hero.pos_float[1] -= self.hero.velocity
            # self.hero.pos_float[1] += self.hero.velocity
        else:
            self.hero.orderedToJump = False

        if not self.hero.isAttacking and not self.hero.dead:
            if self.handler.inputManager.pressed.get(pygame.K_RIGHT):
                self.hero.moveRight = True
            else:
                self.hero.moveRight = False
            if self.handler.inputManager.pressed.get(pygame.K_LEFT):
                self.hero.moveLeft = True
            else:
                self.hero.moveLeft = False
            # if self.handler.inputManager.pressed.get(pygame.K_UP):
            #     self.hero.moveUp = True
            # else:
            #     self.hero.moveUp = False
            # if self.handler.inputManager.pressed.get(pygame.K_DOWN):
            #     self.hero.moveDown = True
            # else:
            #     self.hero.moveDown = False
        else:
            self.hero.moveRight = False
            self.hero.moveLeft = False
            # self.hero.moveUp = False
            # self.hero.moveDown = False

        if self.handler.inputManager.pressed.get(pygame.K_s):
            self.hero.sprint = True
        else:
            self.hero.sprint = False

        if all(key == False for key in self.handler.inputManager.pressed.values()):
            self.hero.notOrdered = True
        else:
            self.hero.notOrdered = False

    # def allowCollisionWithStairs(self):
    #     group = pygame.sprite.Group()
    #     group.add(self.hero)
    #     for player in group:
    #         collision = pygame.sprite.spritecollide(
    #             player, self.handler.game.gameState.gameDisplayer.stairGroup, False, pygame.sprite.collide_mask)
    #         if len(collision) > 0:
    #             self.hero.allowMove = True
    #         else:
    #             self.hero.allowMove = False

    def tick(self):
        self.keyManager()
        self.handler.game.gameState.gameDisplayer.current_world.camera.centerOnEntity(
            self.hero)
        self.hero.tick()
        # print("player x = " + str(self.hero.rect.center[0]))
        # print("player y = " + str(self.hero.rect.center[1]))
        # self.allowCollisionWithStairs()

    def draw(self):
        self.hero.draw()
