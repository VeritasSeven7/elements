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
        # Escape key
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        # Key arrows for movement
        elif keys[pygame.K_a] and not keys[pygame.K_s]:
            self._move_left(el_game)
        elif keys[pygame.K_d] and not keys[pygame.K_s]:
            self._move_right(el_game)
        elif keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            self._crouch(el_game)
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            self._right_crouch_walk(el_game)
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self._left_crouch_walk(el_game)

        elif keys[pygame.K_SPACE]:
            self._jump(el_game)



        else:
            el_game.player.no_action = True

    # working out controller support later :/
    """def joystick(self, el_game):
        for event in pygame.event.get():
            if event.type == pygame.JOYHATMOTION:
                print(event)
                self.hat = el_game.joystick.get_hat(0)
                if self.hat == (-1, 0):
                    self._move_left(el_game)"""

    def _move_left(self, el_game):
        el_game.player.facing_left = True
        el_game.player.no_action = False
        el_game.player.walk_animation()

    def _move_right(self, el_game):
        el_game.player.facing_left = False
        el_game.player.no_action = False
        el_game.player.walk_animation()

    def _crouch(self, el_game):
        el_game.player.no_action = False
        el_game.player.crouch_animation()

    def _right_crouch_walk(self, el_game):
        el_game.player.facing_left = False
        el_game.player.no_action = False
        el_game.player.crouch_walk_animation()

    def _left_crouch_walk(self, el_game):
        el_game.player.facing_left = True
        el_game.player.no_action = False
        el_game.player.crouch_walk_animation()

    def _jump(self, el_game):
        el_game.player.no_action = False
        el_game.player.jump_animation()