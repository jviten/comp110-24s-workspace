"""A skateboard boardsliding a rail!"""

__author__ = "730677545"

from turtle import Turtle, colormode, done


def main() -> None:
    """The Main Function."""
    # Draw the rail
    rail = Turtle()
    i = 0
    colormode(255)
    rail.penup()
    rail.goto(-250, -235)
    rail.left(45)
    rail.pendown()
    rail.color(0, 0, 100)
    rail.begin_fill()
    while i < 2:
        rail.forward(700)
        rail.right(90)
        rail.forward(20)
        rail.right(90)
        i += 1
    rail.end_fill()

    def rail_legs(rail: Turtle, xpos: float, ypos: float) -> None:
        """Draw the legs of the rail of same size in different locations."""
        rail.penup()
        rail.goto(xpos, ypos)
        rail.pendown()
        rail.color(0, 0, 100)
        rail.setheading(0.0)
        rail.begin_fill()
        rail.right(45)
        i: int = 0
        while i < 2:
            rail.forward(200)
            rail.right(90)
            rail.forward(10)
            rail.right(90)
            i += 1
        rail.end_fill()

    rail_legs(rail, -220.0, -80.0)
    rail_legs(rail, 20.0, 180.0)

    def skateboard_semicircle(rail: Turtle) -> None:
        i = 0
        while i < 180:
            rail.forward(1)
            rail.right(1)
            i += 1

    rail.penup()
    rail.goto(-90.0, 110.0)
    rail.color(100, 100, 100)
    rail.setheading(0.0)
    rail.pendown()
    rail.begin_fill()
    rail.right(45)
    rail.forward(300)
    skateboard_semicircle(rail)
    rail.forward(300)
    skateboard_semicircle(rail)
    rail.forward(5)
    rail.end_fill
    done()


if __name__ == "__main__":
    main()