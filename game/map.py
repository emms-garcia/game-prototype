import csv
import os
import pygame

from common import Colors, Constants
from events import CustomEvents, EventHandler
from sprites import SmartSprite

SIZE = (Constants.OBJECT_SIZE, Constants.OBJECT_SIZE)
MAPS_DIR = os.path.join(Constants.ASSETS_DIR, 'maps')


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


class Map(pygame.sprite.RenderPlain):
    N_TILES = 8
    SIZE = N_TILES * BaseTile.SIZE
    WALL = '1'

    def __init__(self, map_id):
        pygame.sprite.RenderPlain.__init__(self)

        self.map_dict = {}
        self.tile_groups = {}

        with open(os.path.join(MAPS_DIR, map_id, 'map.csv')) as csv_file:
            for dy, row in enumerate(csv.reader(csv_file, delimiter=',')):
                self.map_dict[int(dy)] = {}
                for dx, tile_type in enumerate(row):
                    tile = resolve_tile_type(tile_type)
                    tile.move(dx, dy)
                    self.add(tile)

                    self.map_dict[int(dy)][int(dx)] = tile
                    if tile_type not in self.tile_groups:
                        self.tile_groups[tile_type] = pygame.sprite.Group()
                        self.tile_groups[tile_type].add(tile)

    def is_valid_cell(self, x, y):
        try:
            tile = self.map_dict[y][x]
            tile.trigger()
            return tile.CAN_STEP
        except KeyError:
            return False
