import sys
import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill('black')
