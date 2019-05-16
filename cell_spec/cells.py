"""Create a Grid of Cells for a cellular automaton."""


class Cell:
    """A cell that holds references to its neighbours and the agents it contains."""

    def __init__(self, neighbours: set = None, agents: list = None):
        self.neighbours = set() if neighbours is None else neighbours
        self.agents = [] if agents is None else agents

    def get_neighbourhood(self, radius: int = 1) -> set:
        """Return all cells within a given radius."""
        if radius == 0:
            return set()
        result = self.neighbours.copy()
        if radius > 1:
            # Recursively get neighbours of neighbours.
            for neighbour in self.neighbours:
                result |= neighbour.get_neighbourhood(radius - 1)
        return result - {self}

    def get_distance(self, other, max_distance) -> int:
        """Return the distance between two cells."""
        if self == other:
            return 0
        # Iteratively check larger neighbourhoods, until other is in it
        distance = 1
        while True:
            if other in self.get_neighbourhood(distance):
                return distance
            distance += 1
            if distance > max_distance:
                break

    def get_perimeter(self, radius: int = 1) -> set:
        """Return all cells at a given distance to self."""
        return self.get_neighbourhood(radius) - self.get_neighbourhood(radius - 1)

    def get_shortest_path(self, other: "Cell") -> set:
        """Return the smallest set of neighbouring cells including both self and other."""
        result = {self, other}
        if other in self.neighbours:
            return result
        # Recurse through shortest paths from neighbours to other.
        paths = []
        for neighbour in self.neighbours:
            paths.append(result.union(neighbour.get_shortest_path(other)))
        return min(paths)


class CellGrid:
    """Create a grid of cells."""

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        # Initialize cell array.
        self.cells = [[Cell() for _ in range(self.columns)] for _ in range(self.rows)]
        # Add neighouring cells with periodic boundaries.
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                cell.neighbours |= {
                    self.cells[(i - 1) % rows][j],
                    self.cells[(i + 1) % rows][j],
                    self.cells[i][(j - 1) % columns],
                    self.cells[i][(j + 1) % columns],
                }

    def __getitem__(self, index):
        """Allow to access cells in a CellGrid directly.

        This 'magic method' allows to access a cell like this:
        `cell_grid[i][j]` or this `cell_grid[j, i]` instead of
        only like this: `cell_grid.cells[i][j]`.

        """
        if isinstance(index, (tuple, list)) and len(index) == 2:
            return self.cells[index[1]][index[0]]
        return self.cells[index]

    def get_position(self, cell) -> tuple:
        """Return the position of a cell in the grid."""
        for i, row in enumerate(self.cells):
            if cell in row:
                return row.index(cell), i
        if not isinstance(cell, Cell):
            raise TypeError(f"Argument should be of type 'Cell', not '{cell.__class__.__name__}'.")
        raise ValueError("The given cell is not a part of the grid.")

    def moore_neighbourhood(self, grid_position: tuple, radius: int) -> list:
        """I don't quite understand what this method does?"""
        result = []
        u = [grid_position[0] - radius, grid_position[1] - radius]
        for i in range(2 * radius + 1):
            for j in range(2 * radius + 1):
                # This does not make much sense, since u is a list and i and j are integers
                result.append([u + i, u + j])
        return result

    def von_neumann_neighbourhood(self, radius: int):
        """Missing implementation."""
        raise NotImplementedError

    def __str__(self) -> str:
        """Generate an ASCII represenation of the grid and agents in it."""
        output = self.columns * " __" + "\n"
        for i in range(self.rows):
            for j in range(self.columns):
                filling = "__"
                if len(self.cells[i][j].agents) == 1:
                    filling = "_§"
                elif len(self.cells[i][j].agents) == 2:
                    filling = "§§"
                elif len(self.cells[i][j].agents) > 2:
                    filling = "++"
                output += "|" + filling
                if j == self.columns - 1:
                    output += "|"
            output += "\n"
        return output
