import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if keys[pygame.K_SPACE]:
                self.jump()
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            if keys[pygame.K_SPACE]:
                self.jump()
            self.direction.x = -1
        elif keys[pygame.K_SPACE]:
            self.jump()
        else:
            self.direction.x = 0

    def update(self):
        self.get_input()
        # self.apply_gravity()
