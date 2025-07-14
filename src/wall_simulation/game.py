import pygame

from wall_simulation.geometry.vector import Vector
from wall_simulation.utils.generate_triangles import generate_triangles

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
PLAY_AREA_WIDTH = 400
PLAY_AREA_HEIGHT = 500
FIGURE_AVERAGE_SIZE = 50


class GameEnv:
    def __init__(self):
        self.play_area_x = WINDOW_WIDTH / 2 - PLAY_AREA_WIDTH / 2
        self.play_area_y = 100

    def init_render(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        # Generate random triangles
        pos = Vector(self.play_area_x + 50, self.play_area_y + 50)
        self.triangles = generate_triangles(1, FIGURE_AVERAGE_SIZE, pos)

    def render(self):
        self.window.fill((0, 0, 0))
        # Draw the playing box
        self._draw_play_area()

        for t in self.triangles:
            t.draw(self.window)

        pygame.display.update()

    def _draw_play_area(self):
        # Horizontal Base
        pygame.draw.line(
            self.window,
            (255, 255, 255),
            (self.play_area_x, self.play_area_y + PLAY_AREA_HEIGHT),
            (self.play_area_x + PLAY_AREA_WIDTH, self.play_area_y + PLAY_AREA_HEIGHT),
            2,
        )
        # Left Wall
        pygame.draw.line(
            self.window,
            (255, 255, 255),
            (self.play_area_x, self.play_area_y),
            (self.play_area_x, self.play_area_y + PLAY_AREA_HEIGHT),
            2,
        )
        # Right Wall
        pygame.draw.line(
            self.window,
            (255, 255, 255),
            (self.play_area_x + PLAY_AREA_WIDTH, self.play_area_y),
            (self.play_area_x + PLAY_AREA_WIDTH, self.play_area_y + PLAY_AREA_HEIGHT),
            2,
        )
