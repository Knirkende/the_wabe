from app.core.components import Region
from app.model.terrain import TERRAIN, Mountain, GrassLand

class RegionFactory:
    """Region map generation tool"""

    REGION_SIZE = 16

    def __init__(self):
        pass
    
    def build_region(self):
        region = Region(self.REGION_SIZE)
        terrain_type = 0 #TODO allow specifying initial seed
        for i in range(self.REGION_SIZE - 1):
            self.seed(region.terrain, i, 0, TERRAIN[terrain_type])
            terrain_type = self.grow(region.terrain, i, 0, terrain_type)
        return region
    
    def seed(self, terrain, target_row, target_col, type):
        terrain[target_row][target_col] = type()
    
    def grow(self, terrain, origin_row, origin_col, origin_type):
        #TODO algo to make biome boundaries organically
        #for now just make everything grassland for concept check
        terrain[origin_row + 1][origin_col + 1] = TERRAIN[origin_type]()
        if origin_row % 2 == 0:
            terrain[origin_row][origin_col + 1] = TERRAIN[origin_type]()
        else:
            terrain[origin_row + 1][origin_col] = TERRAIN[origin_type]()
        return 0 #TODO