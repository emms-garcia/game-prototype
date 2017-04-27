
"""
    Game Engine Prototipe
    By Emmanuel Garcia
"""
import pygame
import sys

from common import Colors
from events import CustomEvents
from map import Map
from player import Player


class Game(object):
    FPS = 30

    def __init__(self):
        self.current_map_id = '1'

        self.map = Map(self.current_map_id)
        self.player = Player(self.map)

    def draw(self, screen):
        """
            Draw all the stuff in the game
        """
        self.map.draw(screen)
        self.player.draw(screen)

    def event(self, event):
        """
            Handle events
        """
        if event.type == pygame.QUIT:
            sys.exit()

        # GAME EVENTS
        elif event.type == CustomEvents.WARP_EVENT_ID:
            self.map.empty()
            self.map = Map(event.there)
            self.player.map = self.map
            self.player.set_initial_position()

    def game_loop(self):
        """
            Main game loop
        """
        pygame.init()
        screen = pygame.display.set_mode((Map.SIZE, Map.SIZE))
        pygame.display.set_caption('Game Prototype')

        bg = pygame.Surface(screen.get_size())
        bg.convert()
        bg.fill(Colors.WHITE)

        clock = pygame.time.Clock()
        while True:
            clock.tick(Game.FPS)
            for event in pygame.event.get():
                self.event(event)

            self.keyboard()

            screen.blit(bg, (0, 0))
            self.draw(screen)
            pygame.display.flip()

    def keyboard(self):
        # KEYBOARD EVENTS
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_UP]:
            self.player.move_up()
        if keys[pygame.K_DOWN]:
            self.player.move_down()
