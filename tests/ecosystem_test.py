from cell_spec.ecosystem import Ecosystem

class TestEcosystem:
    def test_initialization(self):
        ecosystem = Ecosystem(5, 5, 3)
        assert len(ecosystem.grid.cells) == 5
        for row in ecosystem.grid.cells:
            assert len(row) == 5
        assert len(ecosystem.animals) == 3

    def test_time_step(self):
        ecosystem = Ecosystem(5, 5, 3)
        old_positions = [ecosystem.grid.get_position(animal.cell) for animal in ecosystem.animals]
        ecosystem.time_step()
        for i, animal in enumerate(ecosystem.animals):
            new_position = ecosystem.grid.get_position(animal.cell)
            old_position = old_positions[i]
            assert (
                {abs(new_position[0]-old_position[0]), abs(new_position[1]-old_position[1])} == {0, 1}
                or
                {abs(new_position[0]-old_position[0]), abs(new_position[1]-old_position[1])} == {0, 4}
            )
