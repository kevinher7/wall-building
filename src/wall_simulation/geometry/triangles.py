import pygame

from wall_simulation.geometry.vector import Vector


class Triangle:
    def __init__(self, pos: Vector, vec1: Vector, vec2: Vector):
        self.pos = pos
        self.edges = [vec1.translate(pos), vec2.translate(pos)]
        self.vec1 = vec1
        self.vec2 = vec2
        self.pos = pos
        last_edge = self.edges[1] - self.edges[0]
        # last_edge = self.edges[0] - self.edges[1]
        self.edges.append(last_edge.translate(self.edges[0]))
        # self.edges.append(last_edge)

    def draw(self, window):
        for index, edge in enumerate(self.edges):
            pygame.draw.line(window, (255, 255, 255), (edge.x_0, edge.y_0), (edge.x_f, edge.y_f), 3)
