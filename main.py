import sys
import pygame

from settings import Settings
from player import Player
from events import Events


class Elementals:
    """class for main game management"""
    def __init__(self):
        pygame.init()
        # set controllers



        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.player = Player(self)
        self.events = Events(self)

    def run_game(self):


        while True:
            self.screen.fill(self.settings.background)

            self.events.kb_events(self)

            if self.player.no_action:
                self.player.idle_animation()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    'start the game if this is the main file ran'
    el = Elementals()
    el.run_game()
