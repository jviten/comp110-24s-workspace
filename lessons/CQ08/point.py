"""Making a class of Point and creating scale by funct."""

from __future__ import annotations

author: "730677545"


class Point:
    """A point."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initialize the class: Point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scale up a Point by given factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Scale up a point and return a new point."""
        new_point: Point = Point 
        new_point(self.x, self.y)
        new_point.x *= factor
        new_point.y *= factor
        return new_point
