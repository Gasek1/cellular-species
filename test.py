from cellular_automata import CellGrid
from agents import Agent

grid = CellGrid(10, 10)
start_cell = grid.cells[5][5]
bob = Agent("Bob", start_cell)
start_cell.agents.append(bob)
while True:
    print("Printing grid:")
    print(grid)
    action = input("Move or quit [q]: ")
    if action == "q":
        break
    bob.move()
