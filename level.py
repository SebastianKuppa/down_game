import pygame
from tiles import Tile
from player import Player
from settings import tile_size, screen_width


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

        if player_x < screen_width/4 and player_direction < 0:
            player.speed = 0
            self.world_shift = 8
        elif player_x > screen_width - (screen_width/4) and player_direction > 0:
            player.speed = 0
            self.world_shift = -8
        else:
            player.speed = 8
            self.world_shift = 0

    def horizontal_movement_and_collision(self):
        player = self.player.sprites()[0]
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_and_collision(self):
        player = self.player.sprites()[0]
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.horizontal_movement_and_collision()
        self.vertical_movement_and_collision()
        self.player.update()
        self.player.draw(self.display_surface)
