from enum import Enum

class Vector2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __hash__(self) -> int:
        return self.__x

    def __eq__(self, other_Vector2d) -> bool:
        return self.__x == other_Vector2d.__x and self.__y == other_Vector2d.__y
    
    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y

    def precedes(self, other_Vector2d):
        if self.__x <= other_Vector2d.__x and self.__y <= other_Vector2d.__y:
            return True
        else:
            return False

    def follows(self, other_Vector2d):
        if self.__x >= other_Vector2d.__x and self.__y >= other_Vector2d.__y:
            return True
        else:
            return False

    def add(self, other_Vector2d):
        newObj = Vector2d(self.__x + other_Vector2d.__x,
                          self.__y + other_Vector2d.__y)

        return newObj

    def subtract(self, other_Vector2d):
        newObj = Vector2d(self.__x - other_Vector2d.__x,
                          self.__y - other_Vector2d.__y)

        return newObj

    def upperRight(self, other_Vector2d):
        max_x = self.__x if self.__x > other_Vector2d.__x else other_Vector2d.__x
        max_y = self.__y if self.__y > other_Vector2d.__y else other_Vector2d.__y

        newObj = Vector2d(max_x, max_y)
        return newObj

    def lowerLeft(self, other_Vector2d):
        min_x = self.__x if self.__x < other_Vector2d.__x else other_Vector2d.__x
        min_y = self.__y if self.__y < other_Vector2d.__y else other_Vector2d.__y

        newObj = Vector2d(min_x, min_y)
        return newObj

    def opposite(self):
        return Vector2d(self.__x * (-1), self.__y * (-1))



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
        


class MoveDirection(Enum):
    FORWARD = 'f'
    BACKWARD = 'b'
    LEFT = 'l'
    RIGHT = 'r'
