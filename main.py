import sys
import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    pygame.display.update()
    clock.tick(60)
