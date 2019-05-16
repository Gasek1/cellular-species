class Cell:
    """A cell with properties that holds references to its neighbours and agents it contains."""

    def __init__(self, neighbours: set = None, agents: list = None):
        self.neighbours = set() if neighbours is None else neighbours
        self.agents = [] if agents is None else agents

    def get_neighbourhood(self, radius: int = 1):
        """Return all cells within a given radius."""
        if radius == 0:
            return set()
        result = self.neighbours.copy()
        if radius > 1:
            # Recursively get neighbours of neighbours.
            for neighbour in self.neighbours:
                result |= neighbour.get_neighbourhood(radius - 1)
        return result - {self}

    def get_distance(self, other):
        """Return the distance between two cells."""
        if self == other:
            return 0
        distance = 1
        while True:
            if other in self.get_neighbourhood(distance):
                return distance
            distance += 1
            if distance > 10:
                break

    def get_perimeter(self, radius: int = 1):
        """Return all cells at a given distance to self."""
        return self.get_neighbourhood(radius) - self.get_neighbourhood(radius - 1)

    def get_shortest_path(self, other):
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
        return self.cells[index]

    def moore_neighbourhood(self, grid_position: tuple, radius: int):
        # I don't quite understand what this method does?
        result = []
        u = [grid_position[0] - radius, grid_position[1] - radius]
        for i in range(2 * radius + 1):
            for j in range(2 * radius + 1):
                result.append([u + i, u + j])
        return result

    def von_neumann_neighbourhood(self, radius: int):
        pass

    def __str__(self):
        output = self.columns * " ___" + "\n"
        for i in range(self.rows):
            for j in range(self.columns):
                filling = "_"
                if self.cells[i][j].agents:
                    filling = "§"
                output += "|_" + filling + "_"
                if j == self.columns - 1:
                    output += "|"
            output += "\n"
        return output
