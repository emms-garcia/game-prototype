import os
import pygame

ASSETS_DIR = os.path.join('assets')
OBJECT_SIZE = 50  # Size in pixels for a single object


class SmartSprite(pygame.sprite.Sprite):
    """
        Sprite that moves between tiles.
    """
    SIZE = 50

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.rect.move_ip(x * OBJECT_SIZE, y * OBJECT_SIZE)
        self.x += x
        self.y += y

    def set_position(self, x, y):
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, OBJECT_SIZE, OBJECT_SIZE)
