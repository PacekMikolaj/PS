from model import Vector2d
from animal2 import MoveDirection
from Options_parser import OptionsParser
import importlib

# if importlib.util.find_spec("pytest") is not None:
try:

    def test_precedes():
        v1 = Vector2d(2, 4)
        v2 = Vector2d(3, 4)
        assert v1.precedes(v2) is True
        assert v2.precedes(v1) is False

    def test_follows():
        v1 = Vector2d(1, 3)
        v2 = Vector2d(3, 4)
        assert v1.follows(v2) is False
        assert v2.follows(v1) is True

    def test_add():
        v1 = Vector2d(1, 2)
        v2 = Vector2d(12, -4)
        result = v1.add(v2)
        assert result.get_x() == 13
        assert result.get_y() == -2

    def test_subtract():
        v1 = Vector2d(1, 2)
        v2 = Vector2d(-3, -4)
        result = v1.subtract(v2)
        assert result.get_x() == 4
        assert result.get_y() == 6

    def test_upperRight():
        v1 = Vector2d(1, 200)
        v2 = Vector2d(3, 4)
        result = v1.upperRight(v2)
        assert result.get_x() == 3
        assert result.get_y() == 200

    def test_lowerLeft():
        v1 = Vector2d(1, 2)
        v2 = Vector2d(-3, 4)
        result = v1.lowerLeft(v2)
        assert result.get_x() == -3
        assert result.get_y() == 2

    def test_opposite():
        v = Vector2d(1, 2)
        result = v.opposite()
        assert result.get_x() == -1
        assert result.get_y() == -2

    def test_eq():
        v1 = Vector2d(1, 2)
        v2 = Vector2d(1, 2)
        v3 = Vector2d(3, 4)
        assert v1 == v2
        assert v1 != v3

    def test_parse_options():
        options = ["f", "b", "r", "q", "l"]
        result = OptionsParser.parse_options(options, MoveDirection)
        assert result == [
            MoveDirection.FORWARD,
            MoveDirection.BACKWARD,
            MoveDirection.RIGHT,
            MoveDirection.LEFT,
        ]

except:
    import unittest

    # unittest = importlib.import_module("unittest")

    class TestVector2dMethods(unittest.TestCase):
        def test_precedes(self):
            v1 = Vector2d(1, 2)
            v2 = Vector2d(3, 4)
            self.assertTrue(v1.precedes(v2))
            self.assertFalse(v2.precedes(v1))

        def test_follows(self):
            v1 = Vector2d(1, 2)
            v2 = Vector2d(3, 4)
            self.assertFalse(v1.follows(v2))
            self.assertTrue(v2.follows(v1))

        def test_add(self):
            v1 = Vector2d(1, 2)
            v2 = Vector2d(3, 4)
            result = v1.add(v2)
            self.assertEqual(result.get_x(), 4)
            self.assertEqual(result.get_y(), 6)

        def test_subtract(self):
            v1 = Vector2d(1, 2)
            v2 = Vector2d(3, 4)
            result = v1.subtract(v2)
            self.assertEqual(result.get_x(), -2)
            self.assertEqual(result.get_y(), -2)

        def test_upperRight(self):
            v1 = Vector2d(1, 2)
            v2 = Vector2d(3, 4)
            result = v1.upperRight(v2)
            self.assertEqual(result.get_x(), 3)
            self.assertEqual(result.get_y(), 4)

        def test_lowerLeft(self):
            v1 = Vector2d(1, 2)
            v2 = Vector2d(3, 4)
            result = v1.lowerLeft(v2)
            self.assertEqual(result.get_x(), 1)
            self.assertEqual(result.get_y(), 2)

        def test_opposite(self):
            v = Vector2d(1, 2)
            result = v.opposite()
            self.assertEqual(result.get_x(), -1)
            self.assertEqual(result.get_y(), -2)

        def test_eq(self):
            v1 = Vector2d(1, 2)
            v2 = Vector2d(1, 2)
            v3 = Vector2d(3, 4)
            self.assertEqual(v1, v2)
            self.assertNotEqual(v1, v3)

    class TestOptionsParserMethods(unittest.TestCase):
        def test_parse_options_valid(self):
            options = ["f", "b", "r", "l"]
            result = OptionsParser.parse_options(options, MoveDirection)
            self.assertEqual(
                result,
                [
                    MoveDirection.FORWARD,
                    MoveDirection.BACKWARD,
                    MoveDirection.RIGHT,
                    MoveDirection.LEFT,
                ],
            )

        def test_parse_options_invalid(self):
            options = ["x", "y", "z"]
            result = OptionsParser.parse_options(options, MoveDirection)
            self.assertEqual(result, [])

    if __name__ == "_main_":
        unittest.main()
