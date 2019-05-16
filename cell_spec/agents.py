"""Deep Q Learning agents that interact with each other in a cellular automaton."""

from random import choice

from cell_spec.cells import Cell


class Agent:
    """Have an agent take actions and learn from them."""

    def __init__(self, name: str, cell: Cell):
        self.name = name
        self.cell = cell

    def move(self) -> None:
        """Move to a random neighbouring cell."""
        destination = choice(tuple(self.cell.get_neighbourhood()))
        destination.agents.append(self)
        self.cell.agents.remove(self)
        self.cell = destination
        print(f"{self.name} moved 1 space in a random direction.")
