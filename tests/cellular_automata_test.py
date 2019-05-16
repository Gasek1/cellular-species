from cell_spec.cells import Cell, CellGrid

class TestCells:

    grid = CellGrid(10, 10)

    def test_get_second_order_neighbours(self):
        neighbourhood = self.grid[5][5].get_neighbourhood(2)
        g = self.grid
        assert neighbourhood == {
                              g[3][5],
                     g[4][4], g[4][5], g[4][6],
            g[5][3], g[5][4],          g[5][6], g[5][7],
                     g[6][4], g[6][5], g[6][6],
                              g[7][5]
        }

    def test_periodic_boundaries(self):
        assert self.grid[9][9].neighbours == {
            self.grid[0][9], self.grid[8][9], self.grid[9][0], self.grid[9][8]
        }

    def test_get_distance(self):
        assert self.grid[2][1].get_distance(self.grid[2][5], 10) == 4
        assert self.grid[2][1].get_distance(self.grid[2][9], 10) == 2 # periodic