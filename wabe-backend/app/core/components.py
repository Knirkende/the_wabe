from app.model.terrain import Undefined, TERRAIN

class Region:
    
    size: int
    seed: int
    terrain: list[list[str]]

    def __init__(self, size: int):
        self.terrain = [[Undefined() for _ in range(size)] for _ in range(size)]