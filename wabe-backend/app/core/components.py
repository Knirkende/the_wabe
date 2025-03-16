from app.model.terrain import Undefined
from app.model.archetypes import Terrain

class Region:
    
    size: int
    seed: int
    terrain: list[list[Terrain]]

    def __init__(self, size: int):
        self.terrain = [[Undefined() for _ in range(size)] for _ in range(size)]
    
    def get_biome_size(self, from_x: int, from_y: int) -> int:
        """returns the number of tiles of same type connected to tile at given coordinates"""
        return self._do_get_biome_size(from_x, from_y, 0, set())
    
    def _do_get_biome_size(self, from_x: int, from_y: int, size: int, visited: set) -> int:
        
        if (from_x, from_y) in visited:
            return 0
        
        visited.add((from_x, from_y))
        size = 1
        
        #look left
        if from_x > 0 and isinstance(self.terrain[from_x - 1][from_y], self.terrain[from_x][from_y].__class__):
            size += self._do_get_biome_size(from_x - 1, from_y, size, visited)
        #look right
        if from_x < len(self.terrain) - 1 and isinstance(self.terrain[from_x + 1][from_y], self.terrain[from_x][from_y].__class__):
            size += self._do_get_biome_size(from_x + 1, from_y, size, visited)
        #look up
        if from_y > 0 and isinstance(self.terrain[from_x][from_y - 1], self.terrain[from_x][from_y].__class__):
            size += self._do_get_biome_size(from_x, from_y - 1, size, visited)
        #look down
        if from_y < len(self.terrain) - 1 and isinstance(self.terrain[from_x][from_y + 1], self.terrain[from_x][from_y].__class__):
            size += self._do_get_biome_size(from_x, from_y + 1, size, visited)
        return size