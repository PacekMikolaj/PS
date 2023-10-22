#!/usr/bin/python3
import sys


def run(moves, move_descriptions):
    result = []
    for move in moves:
        if move == "f":
            result.append(move_descriptions.get("f", ""))
        elif move == "b":
            result.append(move_descriptions.get("b", ""))
        elif move == "r":
            result.append(move_descriptions.get("r", ""))
        elif move == "l":
            result.append(move_descriptions.get("l", ""))
    return result


def display(args, show_index):
    for i, arg in enumerate(args):
        if show_index:
            print(f"args[{i}] = {arg}")
        else:
            print(arg)


moves = sys.argv[1:]
move_descriptions = {
    "f": "Zwierzak idzie do przodu",
    "b": "Zwierzak idzie do tyłu",
    "r": "Zwierzak skręca w prawo",
    "l": "Zwierzak skręca w lewo",
}

print("Start")
opisy_ruchow = run(moves, move_descriptions)
display(opisy_ruchow, show_index=False)
print("Stop")
