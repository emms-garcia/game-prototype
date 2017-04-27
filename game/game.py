
"""
    Game Engine Prototipe
    By Emmanuel Garcia
"""
import pygame
import pygame.locals
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
        if event.type == pygame.locals.QUIT:
            sys.exit()

        # KEYBOARD EVENTS
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_RIGHT:
                self.player.move_right()
            if event.key == pygame.locals.K_LEFT:
                self.player.move_left()
            if event.key == pygame.locals.K_UP:
                self.player.move_up()
            if event.key == pygame.locals.K_DOWN:
                self.player.move_down()

        # GAME EVENTS
        elif event.type == CustomEvents.WARP_EVENT_ID:
            self.map.empty()
            self.map = Map(event.there)
            self.player.map = self.map

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

            screen.blit(bg, (0, 0))
            self.draw(screen)
            pygame.display.flip()


def main():
    Game().game_loop()

if __name__ == '__main__':
    main()
