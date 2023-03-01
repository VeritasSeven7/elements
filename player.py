import sys
import pygame

from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, el_game):
        super().__init__()
        self.screen = el_game.screen
        self.settings = el_game.settings
        self.screen_rect = el_game.screen.get_rect()

        # base player stats
        self.attack = 10
        self.defence = 10
        self.magic = 10
        self.willpower = 10
        self.health = 100
        self.ap = 5

        """load images"""
        # set animation indexes
        self.idle_index = 0
        self.walking_index = 0

        # set animation frame speed limits
        self.frame_interval = 175
        self.last_update = 0

        # animation flags
        self.sword_out = False
        self.no_action = True

        # idle frames
        self.idle_cycle = []
        for i in range (0, 4):
            self.idle_cycle.append(pygame.transform.scale(pygame.image.load('assets/Player/idle/adventurer-idle-0'+str(i)+'.png'), (200, 148)))

        self.idle_sword = []
        for i in range (0, 4):
            self.idle_sword.append(pygame.transform.scale(pygame.image.load('assets/Player/idle/adventurer-idle-2-0'+str(i)+'.png'), (200, 148)))

        # walking frames
        self.walking_cycle = []
        for i in range (0, 6):
            self.walking_cycle.append(pygame.transform.scale(pygame.image.load('assets/Player/walk/adventurer-walk-0'+str(i)+'.png'), (200, 148)))


        # direction flag
        self.facing_left = False

    def idle_animation(self):
        if self.sword_out:
            self.idle_image = self.idle_sword[self.idle_index]
            self.idle_rect = self.idle_image.get_rect()
            if self.facing_left:
                self.idle_image = pygame.transform.flip(self.idle_image, True, False)

            if self.idle_index < len(self.idle_sword) - 1:
                if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                    self.idle_index += 1
                    self.last_update = pygame.time.get_ticks()
            else:
                self.idle_index = 0
        else:
            self.idle_image = self.idle_cycle[self.idle_index]
            self.idle_rect = self.idle_image.get_rect()
            if self.facing_left:
                self.idle_image = pygame.transform.flip(self.idle_image, True, False)

            if self.idle_index < len(self.idle_cycle) - 1:
                if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                    self.idle_index += 1
                    self.last_update = pygame.time.get_ticks()
            else:
                self.idle_index = 0

        self.screen.blit(self.idle_image, self.idle_rect)

    def walk_animation(self):
        self.no_action = False
        self.walking_image = self.walking_cycle[self.walking_index]
        self.walking_rect = self.walking_image.get_rect()
        if self.walking_index < len(self.walking_cycle)-1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.walking_index += 1
                self.last_update = pygame.time.get_ticks()

        else:
            self.walking_index = 0


        self.screen.blit(self.walking_image, self.walking_rect)


    def update(self):
        pass
