from mesa import Agent

class Plane(Agent):
    def __init__(self, unique_id, model, origin, destination):
        super().__init__(unique_id, model)
        self.origin = origin
        self.destination = destination
        self.location = origin.location
        self.wait_time = 0

    def request_takeoff(self):
        self.origin.accept_request(self)

    def travel(self):
        # move towards destination
        pass

    def step(self):
        pass