import time
from model.core import Vector2d, MoveDirection
from model.animalV2 import Animal
from model.interface import IWorldMap


class OptionsParser:
    @staticmethod
    def parse_options(directions):
        valid_directions = []
        for direction in directions:
            print(direction)
            try:
                valid_directions.append(MoveDirection(direction))
            except ValueError:
                print(f"{direction} is not legal move specification")
        return valid_directions


class Simulation:
    def __init__(
        self,
        directions: list[MoveDirection],
        positions: list[Vector2d],
        iwmap: IWorldMap,
    ) -> None:
        self.directions = directions
        self.positions = positions
        self.animals: list[Animal] = []
        self.iwmap = iwmap

        for vector in self.positions:
            if self.iwmap.place(Animal(vector)):
                self.animals.append(Animal(vector))

    def run(self) -> None:
        print(self.iwmap)
        time.sleep(1)
        for i in range(len(self.directions)):
            n = i % len(self.animals)
            self.iwmap.move(self.animals[n], self.directions[i])
            print(self.iwmap)
            time.sleep(1)
