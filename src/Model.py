import mesa
import Predator
import Prey
import Food


class Sim_Model(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, prey_num, pred_num, food, width, height):
        self.num_prey = prey_num
        self.num_pred = pred_num
        self.food_num = food
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        # Create agents
        count = 0
        for i in range(self.num_pred):
            a = Predator.PredatorAgent(count, self)
            count += 1
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        for i in range(self.num_prey):
            a = Prey.PreyAgent(count, self)
            count += 1
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        for i in range(self.food_num):
            a = Food.FoodAgent(count, self)
            count += 1
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))


    def step(self):
        self.schedule.step()
