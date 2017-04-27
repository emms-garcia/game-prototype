import pygame

from common import Colors, Constants
from sprites import SmartSprite


class Player(SmartSprite):
    """
        Class that handles the player display data and movement
    """

    def __init__(self, map):
        SmartSprite.__init__(self)
        self.image = pygame.Surface(
            (Constants.OBJECT_SIZE, Constants.OBJECT_SIZE)
        )
        self.image.fill(Colors.GREEN)
        self.rect = self.image.get_rect()
        self.map = map
        self.move(1, 1)

    def move(self, dx, dy):
        # Override the move method to check if the next movement is valid
        if self.map.is_valid_cell(self.x + dx, self.y + dy):
            super(Player, self).move(dx, dy)

    def move_down(self):
        self.move(0, 1)

    def move_left(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(1, 0)

    def move_up(self):
        self.move(0, -1)
