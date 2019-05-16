from cell_spec.ecosystem import Ecosystem

ecosystem = Ecosystem(10, 10, 5)
while True:
    print("Printing grid:")
    print(ecosystem.grid)
    action = input("time step or quit [q]: ")
    if action == "q":
        break
    ecosystem.time_step()
