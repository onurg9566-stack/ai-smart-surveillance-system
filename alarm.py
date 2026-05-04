import pygame

class Alarm:
    def __init__(self):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("alarm.wav")

    def trigger(self):
        self.sound.play()