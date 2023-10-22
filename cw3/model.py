class Vector2d:
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

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
