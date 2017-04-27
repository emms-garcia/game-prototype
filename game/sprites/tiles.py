import pygame

from game.events import CustomEvents, EventHandler
from game.common import Constants, Colors
from game.sprites import SmartSprite


class BaseTile(SmartSprite):
    COLOR = Colors.BLACK
    TYPE = None

    def __init__(self):
        SmartSprite.__init__(self)
        self.image = pygame.Surface(
            (Constants.OBJECT_SIZE, Constants.OBJECT_SIZE)
        )
        self.image.fill(self.COLOR)
        self.rect = self.image.get_rect()

    def trigger(self):
        pass


class WallTile(BaseTile):
    CODE = '1'
    COLOR = Colors.RED
    CAN_STEP = False


class EmptyTile(BaseTile):
    CODE = '0'
    CAN_STEP = True


class WarpTile(BaseTile):
    CODE = '1'
    COLOR = Colors.BLUE
    CAN_STEP = True

    def __init__(self, here, there):
        BaseTile.__init__(self)
        self.here = here
        self.there = there

    def trigger(self):
        EventHandler.post_event(
            CustomEvents.WARP_EVENT_ID, here=self.here, there=self.there
        )


SIMPLE_TILE_TYPES = {
    WallTile.CODE: WallTile,
    EmptyTile.CODE: EmptyTile,
}


def resolve_tile_type(tile_type):
    if '.' in tile_type:
        return WarpTile(*tile_type.split('.'))

    if SIMPLE_TILE_TYPES.get(tile_type):
        return SIMPLE_TILE_TYPES[tile_type]()
