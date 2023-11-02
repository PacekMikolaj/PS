import sys
from model import Vector2d, MoveDirection
from controller import Simulation
from Options_parser import OptionsParser

directions: list[MoveDirection] = OptionsParser.parse_options(
    sys.argv[1:], MoveDirection
)
positions: list[Vector2d] = [
    Vector2d(2, 2),
    Vector2d(3, 4),
]  # Pozycje początkowe dla zwierząt, odpowiednio, (2,2) oraz (3,4)
simulation: Simulation = Simulation(directions, positions)
simulation.run()
