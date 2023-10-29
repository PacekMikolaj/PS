from enum import Enum
from animal2 import MoveDirection


class MapDirection(Enum):
    NORTH = {"arrow": "↑", "index": 0, "directions": [0, 1]}
    EAST = {"arrow": "→", "index": 1, "directions": [1, 0]}
    SOUTH = {"arrow": "↓", "index": 2, "directions": [0, -1]}
    WEST = {"arrow": "←", "index": 3, "directions": [-1, 0]}

    def __str__(self):
        return self.value["arrow"]

    def next(self):
        directionIndex = (self.value["index"] + 1) % 4
        return MapDirection(list(MapDirection)[directionIndex])

    def previous(self):
        directionIndex = (self.value["index"] - 1) % 4
        return MapDirection(list(MapDirection)[directionIndex])

    def toUnitVector(self):
        return Vector2d(self.value["directions"][0], self.value["directions"][1])


# class MapDirection(Enum):
#     NORTH = "NORTH"
#     EAST = "EAST"
#     SOUTH = "SOUTH"
#     WEST = "WEST"

#     def __init__(self) -> None:
#         if self.value == "NORTH":
#             self.arrow = "↑"
#             self.index = 0
#             self.directions = [0, 1]
#             return
#         if self.value == "EAST":
#             self.arrow = "→"
#             self.index = 1
#             self.directions = [1, 0]
#             return
#         if self.value == "SOUTH":
#             self.arrow = "↓"
#             self.index = 2
#             self.directions = [0, -1]
#             return
#         if self.value == "WEST":
#             self.arrow = "←"
#             self.index = 3
#             self.directions = [-1, 0]
#             return

#     def __str__(self):
#         return self.arrow

#     def next(self):
#         directionIndex = (self.index + 1) % 4
#         return list(MapDirection)[directionIndex]

#     def previous(self):
#         directionIndex = (self.index - 1) % 4
#         return list(MapDirection)[directionIndex]

#     def toUnitVector(self):
#         return Vector2d(self.directions[0], self.directions[1])


class Vector2d:
    def __init__(self, x, y):
        self.__x = int(x)
        self.__y = int(y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return f"({self.__x},{self.__y})"

    def precedes(self, other_Vector2d):
        if not isinstance(other_Vector2d, Vector2d):
            return TypeError
        else:
            if (
                self.__x <= other_Vector2d.get_x()
                and self.__y <= other_Vector2d.get_y()
            ):
                return True
            else:
                return False

    def follows(self, other_Vector2d):
        if not isinstance(other_Vector2d, Vector2d):
            return TypeError
        else:
            if (
                self.__x >= other_Vector2d.get_x()
                and self.__y >= other_Vector2d.get_y()
            ):
                return True
            else:
                return False

    def add(self, other_Vector2d):
        if not isinstance(other_Vector2d, Vector2d):
            return TypeError
        else:
            return Vector2d(
                self.__x + other_Vector2d.get_x(), self.__y + other_Vector2d.get_y()
            )

    def subtract(self, other_Vector2d):
        if not isinstance(other_Vector2d, Vector2d):
            return TypeError
        else:
            return Vector2d(
                self.__x - other_Vector2d.get_x(), self.__y - other_Vector2d.get_y()
            )

    def upperRight(self, other_Vector2d):
        if not isinstance(other_Vector2d, Vector2d):
            return TypeError
        else:
            x = self.__x
            if x < other_Vector2d.get_x():
                x = other_Vector2d.get_x()

            y = self.__y
            if y < other_Vector2d.get_y():
                y = other_Vector2d.get_y()

            return Vector2d(x, y)

    def lowerLeft(self, other_Vector2d):
        if not isinstance(other_Vector2d, Vector2d):
            return TypeError
        else:
            x = self.__x
            if x > other_Vector2d.get_x():
                x = other_Vector2d.get_x()

            y = self.__y
            if y > other_Vector2d.get_y():
                y = other_Vector2d.get_y()

            return Vector2d(x, y)

    def opposite(self):
        return Vector2d(self.__x * (-1), self.__y * (-1))

    def __eq__(self, other_Vector2d):
        if not isinstance(other_Vector2d, Vector2d):
            return TypeError
        else:
            return (
                self.__x == other_Vector2d.get_x()
                and self.__y == other_Vector2d.get_y()
            )


class Animal:
    def __init__(
        self,
        position: Vector2d = Vector2d(0, 0),
        direction: MapDirection = MapDirection.NORTH,
    ):
        self.orientation = direction
        self.position = position

    def __str__(self):
        return f"{self.position} {self.orientation}"

    def __repr__(self):
        return str(self)

    def isAt(self, position: Vector2d):
        return position == self.position

    def move(self, direction: MoveDirection):
        if direction == MoveDirection.RIGHT:
            self.orientation = self.orientation.next()
        if direction == MoveDirection.LEFT:
            self.orientation = self.orientation.previous()
        if direction == MoveDirection.FORWARD:
            newPosition = self.position.add(self.orientation.toUnitVector())
        if direction == MoveDirection.BACKWARD:
            newPosition = self.position.subtract(self.orientation.toUnitVector())
        if newPosition.upperRight(Vector2d(4, 4)) == Vector2d(
            4, 4
        ) and newPosition.lowerLeft(Vector2d(0, 0) == Vector2d(0, 0)):
            self.position = newPosition
