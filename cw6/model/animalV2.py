from model.core import MoveDirection, Vector2d, MapDirection


class Animal:
    def __init__(self, position: Vector2d, orientation=MapDirection.NORTH) -> None:
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return f"{self.orientation}"

    def __repr__(self) -> str:
        return str(self)

    def isAt(self, position: Vector2d) -> bool:
        return (
            self.position.get_x == position.get_x
            and self.position.get_y == position.get_y
        )

    def move(self, direction: MoveDirection, validator):
        direction_moves = {
            "RIGHT": lambda: self.orientation.next(),
            "LEFT": lambda: self.orientation.previous(),
            "FORWARD": lambda: self.position.add(self.orientation.toUnitVector()),
            "BACKWARD": lambda: self.position.subtract(self.orientation.toUnitVector()),
        }

        def update_orientation(orientation, direction):
            move = direction_moves.get(direction.name)

            if direction.name in [
                "LEFT",
                "RIGHT",
            ]:
                return move()

            return orientation

        def update_position(position, direction, validator):
            move = direction_moves.get(direction.name)

            if direction.name in [
                "FORWARD",
                "BACKWARD",
            ]:
                if validator.canMoveTo(move()):
                    return move()

            return position

        self.orientation = update_orientation(self.orientation, direction)
        self.position = update_position(self.position, direction, validator)
