from random import choice

from cell_spec.cellular_automata import Cell


class Agent:
    def __init__(self, name: str, cell: set):
        self.name = name
        self.cell = cell

    def move(self):
        destination = choice(tuple(self.cell.get_neighbourhood()))
        destination.agents.append(self)
        self.cell.agents.remove(self)
        self.cell = destination
        print(f"{self.name} moved 1 space in a random direction.")
