class Island:
    def __init__(self):
        self.sum_height = 0
        self.number_of_tiles = 0
        self.tiles = dict()

    def average_height(self):
        return self.sum_height / self.number_of_tiles

    def add_tile(self, tile):
        tile.island = self
        self.tiles[(tile.x, tile.y)] = tile
        self.sum_height += tile.height
        self.number_of_tiles += 1

    def merge(self, other, my_map):
        if self == other:
            return

        self.sum_height += other.sum_height
        self.number_of_tiles += other.number_of_tiles
        for tile in other.tiles.values():
            tile.island = self
        self.tiles.update(other.tiles)
        my_map.islands.remove(other)

    def select(self):
        #print(self.average_height())
        for tile in self.tiles.values():
            tile.select()

    def deselect(self):
        for tile in self.tiles.values():
            tile.deselect()