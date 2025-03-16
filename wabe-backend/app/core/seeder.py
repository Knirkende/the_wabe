from app.core.components import Region
from app.model.terrain import TERRAIN, Mountain, GrassLand
from app.model.archetypes import Terrain
from random import randint, choice
from copy import copy

class RegionFactory:
    """Region map generation tool"""

    REGION_SIZE = 17

    def __init__(self):
        pass
    
    def build_region(self):
        region = Region(self.REGION_SIZE)
        tile = TERRAIN[0]() #TODO allow specifying initial seed
        for i in range(self.REGION_SIZE - 1):
            for j in range(0, self.REGION_SIZE - 1, 2): # TODO generate final col and fix bugs near end
                self._seed(region.terrain, i, j, tile)
                tile = self._grow(region, i, j)
        return region
    
    def _seed(self, terrain, target_row, target_col, tile):
        terrain[target_row][target_col] = tile
    
    def _grow(self, region: Region, origin_row, origin_col):
        # TODO raise chance of forest based on distance from edges
        region.terrain[origin_row + 1][origin_col + 1] = self._generate_next_tile(region, origin_row, origin_col)

        if origin_row % 2 == 0:
            region.terrain[origin_row][origin_col + 1] = self._generate_next_tile(region, origin_row, origin_col)
        else:
            region.terrain[origin_row + 1][origin_col] = self._generate_next_tile(region, origin_row, origin_col)
        return self._generate_next_tile(region, origin_row, origin_col)
    
    def _generate_next_tile(self, region: Region, origin_row: int, origin_col:int):
        origin_tile: Terrain = region.terrain[origin_row][origin_col]
        terrain_switch = randint(0, 100) > origin_tile.seed_strength

        if terrain_switch:
            choices = copy(TERRAIN)
            choices.remove(origin_tile.__class__)
            tile: Terrain = choice(choices)()
        else:
            tile: Terrain = origin_tile.__class__()
        
        tile.seed_strength *= self._determine_seed_strength(region, origin_row, origin_col)
        return tile

    def _determine_seed_strength(self, region: Region, target_row, target_col):
        return (self.REGION_SIZE // 5) / region.get_biome_size(target_row, target_col)