from app.core.components import Region
from app.core.seeder import RegionFactory
from app.model.terrain import Undefined

def test_init_region():
    region = Region(5)

    assert(len(region.terrain) == 5)
    for row in region.terrain:
        assert(len(row) == 5)
        for x in row:
            assert isinstance(x, Undefined)

def test_region_factory():
    factory = RegionFactory()
    region = factory.build_region()
    assert(len(region.terrain) == 16)
    for row in region.terrain:
        assert(len(row) == 16)
        for x in row:
            assert not isinstance(x, Undefined)
