from mesa import Agent
import random

class Airport(Agent):
    def __init__(self, unique_id, model, num_airstrips, cooldown_airstrip):
        super().__init__(unique_id, model)
        self.location = self.random_location()
        self.cooldown_airstrip = cooldown_airstrip
        self.airstrips = [] #Es un array porque cada pista tiene cooldown
        self.queue = []

    def random_location(self):
        return random.randrange(self.model.grid.width), random.randrange(self.model.grid.height)

    def request_airstrip(self, plane):
        self.queue.append(plane)
    
    def confirm_airstrip(self):
        self.airstrips += 1

    def step(self):
        for plane in self.queue:
            # Manejo de pistas
            pass

        pass
