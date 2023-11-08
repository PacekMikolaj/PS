from Options_parser import OptionsParser
from enum import Enum
import sys


class MoveDirection(Enum):
    FORWARD = "f"
    BACKWARD = "b"
    RIGHT = "r"
    LEFT = "l"


def run(moves, move_descriptions):
    result = []
    valid_moves = OptionsParser.parse_options(moves, MoveDirection)
    for move in valid_moves:
        result.append(move_descriptions.get(move.value, ""))
    return result


def display(args, show_index):
    for i, arg in enumerate(args):
        if show_index:
            print(f"args[{i}] = {arg}")
        else:
            print(arg)


def main():
    moves = sys.argv[1:]
    move_descriptions = {
        MoveDirection.FORWARD.value: "Zwierzak idzie do przodu",
        MoveDirection.BACKWARD.value: "Zwierzak idzie do tyłu",
        MoveDirection.RIGHT.value: "Zwierzak skręca w prawo",
        MoveDirection.LEFT.value: "Zwierzak skręca w lewo",
    }

    opisy_ruchow = run(moves, move_descriptions)
    display(opisy_ruchow, show_index=False)


# Odkomentować, żęby działało
# print("Start")
# main()
# print("Stop")
