class Vector:
    def __init__(self, x_f: float, y_f: float, x_0: float = 0, y_0: float = 0):
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_f = x_f
        self.y_f = y_f

    @property
    def dx(self):
        """X component of the vector"""
        return self.x_f - self.x_0

    @property
    def dy(self):
        """Y component of the vector"""
        return self.y_f - self.y_0

    def translate(self, vector):
        if isinstance(vector, Vector):
            return Vector(
                self.x_f + vector.dx,
                self.y_f + vector.dy,
                self.x_0 + vector.dx,
                self.y_0 + vector.dy,
            )
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Vector):
            # Add vectors by their components
            return Vector(self.x_f + other.dx, self.y_f + other.dy, self.x_0, self.y_0)

        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            # Subtract vectors by their components
            return Vector(self.x_f - other.dx, self.y_f - other.dy, self.x_0, self.y_0)
        elif isinstance(other, (int, float)):
            # Subtract scalar from end point
            return Vector(self.x_f - other, self.y_f - other, self.x_0, self.y_0)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            # Scale the vector components
            return Vector(
                self.x_0 + self.dx * scalar, self.y_0 + self.dy * scalar, self.x_0, self.y_0
            )
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            # Scale the vector components
            return Vector(
                self.x_0 + self.dx / scalar, self.y_0 + self.dy / scalar, self.x_0, self.y_0
            )
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (
                self.x_0 == other.x_0
                and self.y_0 == other.y_0
                and self.x_f == other.x_f
                and self.y_f == other.y_f
            )
        return False

    def __repr__(self):
        return f"Vector ({self.x_0}, {self.y_0}) -> ({self.x_f}, {self.y_f})"
