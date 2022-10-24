import mesa
import Food
import Predator


class PreyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        neighbors = self.model.grid.get_neighbors(self.pos, False)
        if len(neighbors) > 0:
            for ele in neighbors:
                print(self.pos, end=" start")
                print(self)
                print(ele)
                print(ele.pos)
                if isinstance(ele, Food.FoodAgent):
                    self.model.grid.move_agent(self, ele.pos)
                    self.model.grid.remove_agent(ele)
                elif isinstance(ele, Predator.PredatorAgent):
                    x, y = self.pos
                    pred_x, pred_y = ele.pos
                    if x < pred_x:
                        self.model.grid.move_agent(self, (x-1, y))
                    elif x > pred_x:
                        self.model.grid.move_agent(self, (x+1, y))
                    elif y < pred_y:
                        self.model.grid.move_agent(self, (x, y-1))
                    else:
                        self.model.grid.move_agent(self, (x, y+1))
                else:
                    new_position = self.random_move()
                    self.model.grid.move_agent(self, new_position)
            print(self.pos, end=" ")
            print(self)
                # elif isinstance(ele, Predator.PredatorAgent):
        else:
            new_position = self.random_move()
            self.model.grid.move_agent(self, new_position)

    def random_move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        return new_position

    def step(self):
        self.move()