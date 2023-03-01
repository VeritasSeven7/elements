import sys
import pygame

class Events:
    def __init__(self, el_game):
        pass

    def kb_events(self, el_game):
        # window close click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # keyboard key strokes
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        elif keys[pygame.K_RIGHT]:
            el_game.player.no_action = False
            el_game.player.walk_animation()

        else:
            el_game.player.no_action = True

    def joystick(self, el_game):
        joystick = pygame.joystick.Joystick(0)
        #for event in pygame.event.get():
           # if event.type == pygame.joystick.J
