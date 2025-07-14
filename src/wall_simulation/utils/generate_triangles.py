import random

from wall_simulation.geometry.triangles import Triangle
from wall_simulation.geometry.vector import Vector

random.seed(67)


def generate_vectors(num: int, avg_size: int) -> list[Vector]:
    vectors = []
    for index in range(num):
        # (x_0, y_0) is set to (0, 0) by default
        vectors.append(Vector(random.randint(0, avg_size), random.randint(-1 * avg_size, avg_size)))

    return vectors


def generate_triangles(num: int, avg_size: int, pos: Vector) -> list[Triangle]:
    """Generate random triangles within a certain size range"""
    triangles = []
    # 2 * num is the number of required vectors to generate num triangles
    random_vectors = generate_vectors(2 * num, avg_size)

    for index in range(num):
        triangles.append(Triangle(pos, random_vectors.pop(), random_vectors.pop()))

    return triangles
