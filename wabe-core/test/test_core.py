from app.core.components import Region
from app.core.seeder import RegionFactory
from app.model.terrain import Undefined, Mountain, GrassLand

def test_init_region():
    region = Region(5)

    assert(len(region.terrain) == 5)
    for row in region.terrain:
        assert(len(row) == 5)
        for x in row:
            assert isinstance(x, Undefined)

def test_get_biome_size():
    region = Region(5)
    for x, row in enumerate(region.terrain):
        for y, _ in enumerate(row):
            region.terrain[x][y] = Mountain()
    # Only do this in test context; all tiles are the same grassland instance
    region.terrain[0][0] = region.terrain[0][1] = region.terrain[1][1] = region.terrain[1][2] = region.terrain[2][2] = region.terrain[3][3] = GrassLand()
    region.terrain[3][4] = GrassLand()
    assert(region.get_biome_size(0,0) == 5) #left corner
    assert(region.get_biome_size(1,2) == 5) #non-zero origin
    assert(region.get_biome_size(0,4) == 7) #right corner

def test_region_factory():
    factory = RegionFactory()
    region = factory.build_region()
    assert(len(region.terrain) == 17)
    for row in region.terrain:
        assert(len(row) == 17)
        for x in row:
            assert not isinstance(x, Undefined)
