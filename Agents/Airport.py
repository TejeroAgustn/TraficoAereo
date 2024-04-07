from mesa import Agent
import random

class Airport(Agent):
    def __init__(self, unique_id, model, num_airstrips, cooldown_airstrip):
        super().__init__(unique_id, model)
        self.pos = self.random_location()
        self.cooldown_airstrip = cooldown_airstrip
        self.airstrips = self.init_airstrip_cooldown(num_airstrips)
        self.queue = []
        self.total_landings = 0
        self.total_takeoffs = 0
        self.total_landing_waiting_time = 0
        self.total_takeoff_waiting_time = 0

    def init_airstrip_cooldown(self, num_airstrips):
        # al principio no hay cooldown entre los aviones ya que no puede haber mas aviones que pista con todos los aviones para despegar (esto tendriamos que forzarlo en el init)
        airstrips = []
        for _ in range(num_airstrips):
            airstrips.append(0)

        return airstrips

    def random_location(self):
        return random.randrange(self.model.grid.width), random.randrange(self.model.grid.height)

    def request_airstrip(self, plane):
        self.queue.append(plane)

    def confirm_takeoff(self, airstrip):
        self.airstrips[airstrip] = self.cooldown_airstrip
        self.total_takeoffs+=1

    def confirm_landing(self, airstrip):
        self.airstrips[airstrip] = self.cooldown_airstrip
        self.total_landings+=1

    def step(self):
        #print('Aeropuerto: ' + str(self.unique_id))
        for i in range(len(self.airstrips)):
            if self.airstrips[i] > 0:
                self.airstrips[i] -= 1

        for plane in self.queue:
            for i in range(len(self.airstrips)):
                # si no hay cooldown
                if self.airstrips[i] == 0:
                    plane.accept_request(i)
                    self.airstrips[i] = -1 # Pista ocupada hasta que el avion confirme que ha terminado
                    self.queue.remove(plane)
                    break

