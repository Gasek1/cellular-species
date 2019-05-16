"""Build ecosystems with specimen of various species in it."""

from random import randint

from cell_spec.cellular_automata import CellGrid
from cell_spec.agents import Agent
from cell_spec.animal_generator import generate_name

class Specimen(Agent):
    """A type of agent that represents a species of animals in an ecosystem."""

    def take_turn(self):
        """Perform the action for a time step."""
        self.move()

class Ecosystem:
    """Assemble a CellGrid to represent a biosphere and spawn specimens in it."""

    def __init__(self, x_size, y_size, population):
        self.grid = CellGrid(y_size, x_size)
        self.animals = []
        for _ in range(population):
            position = (randint(0, x_size-1), randint(0, y_size-1))
            self.spawn_specimen(position)

    def spawn_specimen(self, position):
        """Create a new specimen and place it in the ecosystem."""
        cell = self.grid[position]
        specimen = Specimen(generate_name(3), cell)
        cell.agents.append(specimen)
        self.animals.append(specimen)

    def time_step(self):
        """Progress one step in time."""
        for animal in self.animals:
            # We could come up with some initiative system here.
            animal.move()
