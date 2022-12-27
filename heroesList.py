from character import Character


class HeroKnight(Character):

    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.heroknight, 100, 100, 8, 8)  # (5, 5)#3.5
        self.health_bar_offset = (5, 5)
        self.handler = handler
        self.name = "hero knight"
        self.rightHurtAnimation.speed = 0.2
        self.leftHurtAnimation.speed = 0.2
        self.rightDeathAnimation.speed = 0.12
        self.leftDeathAnimation.speed = 0.12
        self.attack_rad = 35

# class EvilWizard(Character):

#     def __init__(self, handler):
#         super().__init__(handler, handler.game.assets.evilwizard, 110, 110, 10, 7) #(-80, -80)
#         self.health_bar_offset = (-80, -80)
#         self.handler = handler
#         self.name = "evil wizard"
#         self.rightHurtAnimation.speed = 0.3
#         self.leftHurtAnimation.speed = 0.3
#         self.rightDeathAnimation.speed = 0.14
#         self.leftDeathAnimation.speed = 0.14

# class Ronin(Character):

#     def __init__(self, handler):
#         super().__init__(handler, handler.game.assets.ronin, 90, 90, 12, 9) #(5, 5)
#         self.handler = handler
#         self.health_bar_offset = (10,0)
#         self.name = "ronin"
