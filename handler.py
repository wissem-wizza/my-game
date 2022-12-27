from characterManager import CharacterManager
from inputManager import InputManager
# from sounds import SoundManager


class Handler:

    def __init__(self, game):
        self.game = game
        # self.inputManager = InputManager(self)

    def initializer(self):
        self.characterManager = CharacterManager(self)
        self.inputManager = InputManager(self)
        # self.soundManager = SoundManager(self)
