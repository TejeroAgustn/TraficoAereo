from mesa import Agent
import random

class Airport(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.location = self.random_location()
        self.queue = []

    def random_location(self):
        return random.randrange(self.model.grid.width), random.randrange(self.model.grid.height)

    def accept_request(self, plane):
        self.queue.append(plane)

    def step(self):
        pass
