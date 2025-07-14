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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    environment.drop()

        if environment.is_dropping:
            environment.drop()

        environment.render()

    pygame.quit()
