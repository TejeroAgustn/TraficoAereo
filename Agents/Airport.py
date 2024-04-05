from mesa import Agent
import random

class Airport(Agent):
    def __init__(self, unique_id, model, num_airstrips, cooldown_airstrip):
        super().__init__(unique_id, model)
        self.num_airstrips = num_airstrips
        self.location = self.random_location()
        self.cooldown_airstrip = cooldown_airstrip
        self.airstrips = self.init_airstrip_cooldown()
        self.queue = []

    def init_airstrip_cooldown(self):
        # al principio no hay cooldown entre los aviones ya que no puede haber mas aviones que pista con todos los aviones para despegar (esto tendriamos que forzarlo en el init)
        for i in self.num_airstrips:
            self.cooldown_airstrip[i] = 0

    def random_location(self):
        return random.randrange(self.model.grid.width), random.randrange(self.model.grid.height)

    def request_airstrip(self, plane):
        self.queue.append(plane)
    
    def confirm_airstrip(self):
        self.airstrips += 1

    def step(self):
        for plane in self.queue:
            for airstrip in self.airstrips:
                # si no hay cooldown
                if airstrip == 0:
                    #damos luz verde
                    plane.waiting = False
                    #si esta en tierra despega y si no ateriza
                    plane.vueling = not plane.vueling
                    #reiniciamos cooldown y pasamos al siguiente avion
                    airstrip = self.cooldown_airstrip
                    break

        pass
