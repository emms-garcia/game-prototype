import pygame

from common import Colors, Constants
from sprites import SmartSprite


class Player(SmartSprite):
    """
        Class that handles the player display data and movement
    """
    INITIAL_POSITION = (150, 150)

    def __init__(self, map):
        SmartSprite.__init__(self)
        self.image = pygame.Surface(
            (Constants.OBJECT_SIZE, Constants.OBJECT_SIZE)
        )
        self.image.fill(Colors.GREEN)
        self.rect = self.image.get_rect()
        self.map = map
        self.set_initial_position()

        # Player attributes
        self.speed = 5

    def move(self, dx, dy):
        super(Player, self).move(dx, dy)

        # If the new position is invalid, revert it
        if not self.map.valid_movement(self):
            super(Player, self).move(-dx, -dy)

        # Check if the current position triggers an event
        # on the map
        self.map.trigger_event(self)

    def move_down(self):
        self.move(0, self.speed)

    def move_left(self):
        self.move(-self.speed, 0)

    def move_right(self):
        self.move(self.speed, 0)

    def move_up(self):
        self.move(0, -self.speed)

    def set_initial_position(self):
        self.set_position(*Player.INITIAL_POSITION)
