import pygame
from pygame.math import Vector2 as Vec2

from wall_simulation.geometry.polygon import Polygon

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
PLAY_AREA_WIDTH = 400
PLAY_AREA_HEIGHT = 500


class GameEnv:
    def __init__(self):
        self.play_area_x = WINDOW_WIDTH / 2 - PLAY_AREA_WIDTH / 2
        self.play_area_y = 100

    def init_render(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

    def render(self):
        self.window.fill((0, 0, 0))
        # Draw the playing box
        self._draw_play_area()

        v1 = Vec2(0, 200)
        v2 = Vec2(300, 0)
        v3 = Vec2(400, 500)

        p = Polygon([v1, v2, v3])
        pos = Vec2(self.play_area_x + 50, self.play_area_y + 50)

        p.draw(self.window)

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
