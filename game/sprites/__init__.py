import pygame

from game.common import Constants


class SmartSprite(pygame.sprite.Sprite):
    """
        Sprite with more functionality than the basic pygame Sprite.
    """
    SIZE = 50

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, x, y):
        self.rect.move_ip(x * Constants.OBJECT_SIZE, y * Constants.OBJECT_SIZE)
        self.x += x
        self.y += y

    def set_position(self, x, y):
        self.x = x
        self.y = y

        self.rect = pygame.Rect(
            self.x, self.y, Constants.OBJECT_SIZE, Constants.OBJECT_SIZE
        )
