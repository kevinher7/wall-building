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
        self.gravity = 2  # Reduced gravity for slower fall
        self.is_dropping = False

    def init_render(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        # Generate random triangles
        pos = Vector(self.play_area_x + 50, self.play_area_y + 50)
        self.triangles = generate_triangles(1, FIGURE_AVERAGE_SIZE, pos)

        self.current_triangle = self.triangles[-1]

    def render(self):
        self.window.fill((0, 0, 0))
        # Draw the playing box
        self._draw_play_area()

        for t in self.triangles:
            t.draw(self.window)

        pygame.display.update()

    def drop(self):
        if not self.is_dropping:
            self.triangle_velocity = Vector(0, 0)
            self.fall_time = 0
            self.is_dropping = True

        self.current_triangle.move(self.triangle_velocity)
        # Update time and velocity
        self.fall_time += 1 / 30
        self.triangle_velocity.y_f += self.gravity * self.fall_time

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
