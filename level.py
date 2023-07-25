import pygame
from tiles import Tile
from player import Player
from settings import tile_size


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    p1 = Player((x, y))
                    self.player.add(p1)

    def scroll_x(self):
        player = self.player.sprites()[0]
        player_x = player.rect.x
        player_direction = player.direction.x

        if player_x < 200 and player_direction < 0:
            player.speed = 0
            self.world_shift = 8
        elif player_x > 1000 and player_direction > 0:
            player.speed = 0
            self.world_shift = -8
        else:
            player.speed = 8
            self.world_shift = 0

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()
