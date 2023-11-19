import sys
from model.core import Vector2d, MoveDirection
from controller_new import Simulation, OptionsParser
from model.map import RectangularMap   

directions: list[MoveDirection] = OptionsParser.toList(sys.argv[1:])
positions: list[Vector2d] = [Vector2d(2, 2), Vector2d(3, 4)]
simulation: Simulation = Simulation(directions, positions, RectangularMap(10, 10))
simulation.run()
