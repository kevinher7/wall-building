import pygame

from wall_simulation.geometry.vector import Vector


class Triangle:
    def __init__(self, pos: Vector, vec1: Vector, vec2: Vector):
        self.pos = pos
        self.edges = [vec1.translate(pos), vec2.translate(pos)]

        last_edge = self.edges[1] - self.edges[0]
        self.edges.append(last_edge.translate(self.edges[0]))

    def draw(self, window):
        for edge in self.edges:
            pygame.draw.line(window, (255, 255, 255), (edge.x_0, edge.y_0), (edge.x_f, edge.y_f), 3)
