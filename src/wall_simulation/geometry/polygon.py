import pygame
from pygame.math import Vector2 as Vec2


class Polygon:
    def __init__(self, points: list[Vec2]):
        self.points = points
        self.num_vertices = len(points)

        self.color = (255, 255, 255)
        self.width = 0

    @property
    def vertices(self):
        return [(p.x, p.y) for p in self.points]

    @property
    def rect(self) -> pygame.Rect:
        xs = [p.x for p in self.points]
        ys = [p.y for p in self.points]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)

        return pygame.Rect(minx, miny, maxx - minx, maxy - miny)

    def move_ip(self, dx: float, dy: float) -> None:
        for i in range(self.num_vertices):
            self.points[i].x += dx
            self.points[i].y += dy

    # def rotate_ip(self, angle_deg: float, pivot=None) -> None:
    #     if pivot is None:
    #         pivot = sum(self.points, Vec2(0, 0)) / 3.0  # centroid
    #     pivot = Vec2(pivot)
    #     for i, p in enumerate(self.points):
    #         self.points[i] = (p - pivot).rotate(angle_deg) + pivot

    def draw(
        self,
        surf: pygame.Surface,
        color: tuple[int] | None = None,
        width: int | None = None,
    ) -> None:
        color = color or self.color
        width = self.width if width is None else width

        pygame.draw.polygon(surf, color, self.vertices, width)

    # def draw_outline(self, surf: pygame.Surface, color=(255, 255, 255), width=2) -> None:
    #     pygame.draw.polygon(surf, color, self.vertices, width)

    # Optional: create a mask matching current shape (for collisions)
    def make_mask(self) -> tuple[pygame.Surface, pygame.mask.Mask, pygame.Rect]:
        r = self.rect
        # rebase points to a local transparent surface
        offset = Vec2(-r.left, -r.top)
        local_pts = [(p + offset) for p in self.points]
        img = pygame.Surface(r.size, pygame.SRCALPHA)
        pygame.draw.polygon(img, (100, 100, 255, 255), [(p.x, p.y) for p in local_pts])
        mask = pygame.mask.from_surface(img)
        return img, mask, r.copy()
