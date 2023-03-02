import sys
import pygame

from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, el_game):
        super().__init__()
        self.screen = el_game.screen
        self.settings = el_game.settings
        self.screen_rect = el_game.screen.get_rect()

        """animations for player"""
        # set animation indexes
        self.cast_index = 0
        self.crouch_index = 0
        self.crouch_walk_index = 0
        self.die_index = 0
        self.fall_index = 0
        self.get_up_index = 0
        self.hurt_index = 0
        self.idle_index = 0
        self.jump_index = 0
        self.knock_down_index = 0
        self.walk_index = 0

        # set animation frame speed limits
        self.frame_interval = 175  # milliseconds
        self.last_update = 0  # initialize frame spacing for get_tick()

        # animation flags
        self.no_action = True
        self.facing_left = False

        # load frames into lists
        self.cast_cycle = []
        for i in range(0, 4):
            self.cast_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/cast/adventurer-cast-0'+str(i)+'.png'), (200, 148)))

        self.crouch_cycle = []
        for i in range(0, 4):
            self.crouch_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/crouch/adventurer-crouch-0'+str(i)+'.png'), (200, 148)))

        self.crouch_walk_cycle = []
        for i in range(0, 6):
            self.crouch_walk_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/crouch/adventurer-crouch-walk-0'+str(i)+'.png'), (200, 148)))

        self.die_cycle = []
        for i in range(0, 7):
            self.die_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/die/adventurer-die-0'+str(i)+'.png'), (200, 148)))

        self.fall_cycle = []
        for i in range(0, 2):
            self.fall_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/fall/adventurer-fall-0'+str(i)+'.png'), (200, 148)))

        self.get_up_cycle = []
        for i in range(0, 7):
            self.get_up_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/get up/adventurer-get-up-0'+str(i)+'.png'), (200, 148)))

        self.hurt_cycle = []
        for i in range(0, 3):
            self.hurt_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/hurt/adventurer-hurt-0'+str(i)+'.png'), (200, 148)))

        self.idle_cycle = []
        for i in range(0, 4):
            self.idle_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/idle/adventurer-idle-0'+str(i)+'.png'), (200, 148)))

        self.jump_cycle = []
        for i in range(0, 4):
            self.jump_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/jump/adventurer-jump-0'+str(i)+'.png'), (200, 148)))

        self.knock_down_cycle = []
        for i in range(0, 4):
            self.knock_down_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/knock down/adventurer-knock-dwn-0'+str(i)+'.png'), (200, 148)))

        self.walking_cycle = []
        for i in range(0, 6):
            self.walking_cycle.append(pygame.transform.scale(
                pygame.image.load('assets/Player/walk/adventurer-walk-0'+str(i)+'.png'), (200, 148)))

    def cast_animation(self):
        self.cast_image = self.cast_cycle[self.cast_index]
        self.cast_rect = self.cast_image.get_rect()

        if self.facing_left:
            self.cast_image = pygame.transform.flip(self.cast_image, True, False)

        while self.cast_index < len(self.cast_cycle) - 1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.cast_index += 1
                self.last_update = pygame.time.get_ticks()

        # reset index for next cast
        self.cast_index = 0
        self.screen.blit(self.cast_image, self.cast_rect)

    def crouch_animation(self):
        self.crouch_image = self.crouch_cycle[self.crouch_index]
        self.crouch_rect = self.crouch_image.get_rect()

        if self.facing_left:
            self.crouch_image = pygame.transform.flip(self.crouch_image, True, False)

        if self.crouch_index < len(self.crouch_cycle) - 1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.crouch_index += 1
                self.last_update = pygame.time.get_ticks()
        else:
            self.crouch_index = 0

        self.screen.blit(self.crouch_image, self.crouch_rect)

    def crouch_walk_animation(self):
        self.crouch_walk_image = self.crouch_walk_cycle[self.crouch_walk_index]
        self.crouch_walk_rect = self.crouch_walk_image.get_rect()

        if self.facing_left:
            self.crouch_walk_image = pygame.transform.flip(self.crouch_walk_image, True, False)

        if self.crouch_walk_index < len(self.crouch_walk_cycle) - 1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.crouch_walk_index += 1
                self.last_update = pygame.time.get_ticks()
        else:
            self.crouch_walk_index = 0

        self.screen.blit(self.crouch_walk_image, self.crouch_walk_rect)

    def die_animation(self):
        self.die_image = self.die_cycle[self.die_index]
        self.die_rect = self.die_image.get_rect()

        if self.facing_left:
            self.die_image = pygame.transform.flip(self.die_image, True, False)

        while self.die_index < len(self.die_cycle) - 1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.die_index += 1
                self.last_update = pygame.time.get_ticks()

        self.die_index = 0
        self.screen.blit(self.die_image, self.die_rect)

    def fall_animation(self):
        self.fall_image = self.fall_cycle[self.fall_index]
        self.fall_rect = self.fall_image.get_rect()

        if self.facing_left:
            self.fall_image = pygame.transform.flip(self.fall_image, True, False)

        if self.fall_index < len(self.fall_cycle) - 1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.fall_index += 1
                self.last_update = pygame.time.get_ticks()
        else:
            self.fall_index = 0

        self.screen.blit(self.fall_image, self.fall_rect)

    def get_up_animation(self):
        self.get_up_image = self.get_up_cycle[self.get_up_index]
        self.get_up_rect = self.get_up_image.get_rect()

        if self.facing_left:
            self.get_up_image = pygame.transform.flip(self.get_up_image, True, False)

        while self.get_up_index < len(self.get_up_cycle) - 1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.get_up_index += 1
                self.last_update = pygame.time.get_ticks()

        self.get_up_index = 0
        self.screen.blit(self.get_up_image, self.get_up_rect)

    def hurt_animation(self):
        self.hurt_image = self.hurt_cycle[self.hurt_index]
        self.hurt_rect = self.hurt_image.get_rect()

        if self.facing_left:
            self.hurt_image = pygame.transform.flip(self.hurt_image, True, False)

        while self.hurt_index < len(self.hurt_cycle) - 1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.hurt_index += 1
                self.last_update = pygame.time.get_ticks()

        self.hurt_index = 0
        self.screen.blit(self.get_up_image, self.get_up_rect)

    def idle_animation(self):
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

    def jump_animation(self):
        self.jump_image = self.jump_cycle[self.jump_index]
        self.jump_rect = self.jump_image.get_rect()

        if self.facing_left:
            self.jump_image = pygame.transform.flip(self.jump_image, True, False)

        while self.jump_index < len(self.jump_cycle) - 1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.jump_index += 1
                self.last_update = pygame.time.get_ticks()

        self.jump_index = 0
        self.screen.blit(self.jump_image, self.jump_rect)

    def knock_down_animation(self):
        self.knock_down_image = self.knock_down_cycle[self.knock_down_index]
        self.knock_down_rect = self.knock_down_image.get_rect()

        if self.facing_left:
            self.knock_down_image = pygame.transform.flip(self.knock_down_image, True, False)

        while self.knock_down_index < len(self.knock_down_cycle) - 1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.knock_down_index += 1
                self.last_update = pygame.time.get_ticks()

        self.knock_down_index = 0
        self.screen.blit(self.knock_down_image, self.knock_down_rect)

    def walk_animation(self):
        self.no_action = False

        self.walking_image = self.walking_cycle[self.walk_index]

        if self.facing_left:
            self.walking_image = pygame.transform.flip(self.walking_image, True, False)

        self.walking_rect = self.walking_image.get_rect()
        if self.walk_index < len(self.walking_cycle)-1:
            if pygame.time.get_ticks() - self.last_update > self.frame_interval:
                self.walk_index += 1
                self.last_update = pygame.time.get_ticks()

        else:
            self.walk_index = 0

        self.screen.blit(self.walking_image, self.walking_rect)

    def update(self):
        pass
