
class GameCamera:

    def __init__(self, handler, world_width):
        self.handler = handler
        self.xOffset = 0
        self.yOffset = 0
        self.world_width = world_width

    def checkBlankSpace(self):
        if self.xOffset < 0:
            self.xOffset = 0
        elif self.xOffset > self.world_width - self.handler.game.WIDTH:  # 1920 = background width "3836"
            self.xOffset = self.world_width - self.handler.game.WIDTH

        if self.yOffset < 0:
            self.yOffset = 0
        elif self.yOffset > 656 - self.handler.game.HEIGHT:  # 1289 = background height
            self.yOffset = 656 - self.handler.game.HEIGHT

    def centerOnEntity(self, character):
        if character != None:
            self.xOffset = character.rect.x - self.handler.game.WIDTH / 2 + character.rect.w / 2
            self.yOffset = character.rect.y - \
                self.handler.game.HEIGHT / 2 + character.rect.h / 2
        self.checkBlankSpace()

    def move(self, xAmt, yAmt):
        self.xOffset += xAmt
        self.yOffset += yAmt
        self.checkBlankSpace()
