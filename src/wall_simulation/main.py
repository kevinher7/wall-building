import pygame

from wall_simulation.game import GameEnv


def main():
    environment = GameEnv()
    environment.init_render()

    running = True

    while running:
        environment.clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        environment.render()

    pygame.quit()
