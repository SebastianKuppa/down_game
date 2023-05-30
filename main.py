import pygame

WIDTH = 800
HEIGHT = 600
BACKGROUND = (0, 0, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        screen.fill(BACKGROUND)
        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()