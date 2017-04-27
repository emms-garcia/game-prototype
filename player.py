import pygame

from colors import GREEN
from common import OBJECT_SIZE, SmartSprite

SIZE = (OBJECT_SIZE, OBJECT_SIZE)


class Player(SmartSprite):
    def __init__(self, map):
        SmartSprite.__init__(self)
        self.image = pygame.Surface(SIZE)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.map = map
        self.move(1, 1)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, dx, dy):
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
