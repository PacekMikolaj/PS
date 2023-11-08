from model import MoveDirection, Vector2d, Animal


class Simulation:
    def __init__(
        self, directions: list[MoveDirection], positions: list[Vector2d]
    ) -> None:
        self.directions = directions
        self.positions = positions
        self.animals = []
        for position in positions:
            self.animals.append(Animal(position))

    def run(self):
        numberOfAnimals = len(self.animals)
        for indexOfMove, direction in enumerate(self.directions):
            animal = self.animals[indexOfMove % numberOfAnimals]
            animal.move(direction)
            print(f"Zwierzę {indexOfMove % numberOfAnimals} : {animal}")
