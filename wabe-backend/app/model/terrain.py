from app.model.archetypes import Terrain

class Undefined(Terrain):

    UNDEFINED = 'Undefined'

    def __init__(self, **kwargs):
        super().__init__(terrain_type = self.UNDEFINED, **kwargs)

    def __repr__(self):
        return 'X'

class GrassLand(Terrain):
    
    GRASSLAND = 'Grassland'

    def __init__(self, **kwargs):
        super().__init__(terrain_type = self.GRASSLAND, **kwargs)

    def __repr__(self):
        return 'O'

class Mountain(Terrain):

    MOUNTAIN = "Mountain"

    def __init__(self, **kwargs):
        super().__init__(terrain_type = self.MOUNTAIN, **kwargs)
    
    def __repr__(self):
        return '^'


TERRAIN = [GrassLand, Mountain]