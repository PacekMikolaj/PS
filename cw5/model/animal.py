from model.core import MoveDirection, Vector2d, MapDirection

class Animal:
    def __init__(
        self,
        position: Vector2d = Vector2d(0, 0),
        direction: MapDirection = MapDirection.NORTH,
    ):
        self.orientation = direction
        self.position = position

    def __str__(self):
        return f"{self.orientation}"

    def __repr__(self):
        return str(self)

    def isAt(self, position: Vector2d):
        return position == self.position

    def move(self, direction: MoveDirection, validator):
        if direction.name == MoveDirection.RIGHT.name:
            self.orientation = self.orientation.next()

        elif direction.name == MoveDirection.LEFT.name:
            self.orientation = self.orientation.previous()

        if direction.name == MoveDirection.FORWARD.name or direction.name == MoveDirection.BACKWARD.name:
            if direction.name == MoveDirection.FORWARD.name:
                target: Vector2d = self.position.add(self.orientation.toUnitVector())
            else:
                target = self.position.subtract(self.orientation.toUnitVector())

            if validator.canMoveTo(target):
                self.position = target
