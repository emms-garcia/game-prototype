import csv
import os
import pygame

from common import Constants
from sprites.tiles import resolve_tile_type

SIZE = (Constants.OBJECT_SIZE, Constants.OBJECT_SIZE)
MAPS_DIR = os.path.join(Constants.ASSETS_DIR, 'maps')


class Map(pygame.sprite.RenderPlain):
    N_TILES = 8
    SIZE = N_TILES * Constants.OBJECT_SIZE
    WALL = '1'

    def __init__(self, map_id):
        pygame.sprite.RenderPlain.__init__(self)

        self.map_dict = {}
        self.tile_groups = {}

        # Load the map from the file
        with open(os.path.join(MAPS_DIR, map_id, 'map.csv')) as csv_file:
            for dy, row in enumerate(csv.reader(csv_file, delimiter=',')):
                self.map_dict[int(dy)] = {}
                for dx, tile_type in enumerate(row):
                    tile = resolve_tile_type(tile_type)
                    tile.set_position(
                        dx * Constants.OBJECT_SIZE, dy * Constants.OBJECT_SIZE
                    )
                    self.add(tile)
                    self.map_dict[int(dy)][int(dx)] = tile
                    if tile_type not in self.tile_groups:
                        self.tile_groups[tile_type] = pygame.sprite.Group()
                        self.tile_groups[tile_type].add(tile)

    def trigger_event(self, player):
        for tile in pygame.sprite.spritecollide(
            player, self, False, collided=pygame.sprite.collide_rect_ratio(0.5)
        ):
            tile.trigger()

    def valid_movement(self, player):
        return all([
            tile.CAN_STEP
            for tile in pygame.sprite.spritecollide(
                player, self, False
            )
        ])
