from Model import Sim_Model
import Predator
import Prey
import Food
import matplotlib.pyplot as plt
import numpy as np



rows, cols = (15, 15)


sim = Sim_Model(5, 1, 6, 15, 15)
for i in range(10):
    grid = [["  " for i in range(cols)] for j in range(rows)]
    sim.step()

    for cell in sim.grid.coord_iter():
        cell_content, x, y = cell
        for thing in cell_content:
            if isinstance(thing, Predator.PredatorAgent):
                grid[x][y] = "pd"
            elif isinstance(thing, Prey.PreyAgent):
                grid[x][y] = "py"
            elif isinstance(thing, Food.FoodAgent) and grid[x][y] == "  ":
                grid[x][y] = "fd"
            else:
                grid[x][y] = "  "

    print("-------------------------------------------------")
    for i in range(len(grid)):
        print(i, end="\t:")
        for j in range(len(grid[i])):
            print(grid[i][j], end="|")
        print()
    print("-------------------------------------------------")
    input()
