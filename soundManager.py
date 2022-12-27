import pygame

class SoundManager():
    
    def __init__(self, handler):
        self.handler = handler
        self.sounds = {}

    
    def init(self):
        
        self.sounds = {
            'menu_state' : pygame.mixer.Sound('Assets/Sounds/menu_state.mp3')
            # 'game_state' : pygame.mixer.Sound('Assets/Sounds/game_state.mp3')
        }

    def play(self, name):
        self.sounds[name].play()