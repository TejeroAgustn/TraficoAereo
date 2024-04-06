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
        self.total_landing_waiting_time = 0

    def init_airstrip_cooldown(self, num_airstrips):
        # al principio no hay cooldown entre los aviones ya que no puede haber mas aviones que pista con todos los aviones para despegar (esto tendriamos que forzarlo en el init)
        airstrips = []
        for _ in range(num_airstrips):
            airstrips.append(0)

        return airstrips

    def random_location(self):
        return random.randrange(self.model.grid.width), random.randrange(self.model.grid.height)

    def request_airstrip(self, plane):
        self.queue.append([plane,0])

    def confirm_takeoff(self, airstrip):

        pass

    def confirm_landing(self, airstrip):
        pass

    def step(self):
        #print('Aeropuerto: ' + str(self.unique_id))
        for i in range(len(self.airstrips)):
            if self.airstrips[i] > 0:
                self.airstrips[i] -= 1

        for plane,waiting in self.queue:
            
            for i in range(len(self.airstrips)):
                # si no hay cooldown
                if self.airstrips[i] == 0:
                    #reiniciamos cooldown y pasamos al siguiente avion
                    self.airstrips[i] = self.cooldown_airstrip + plane.accept_request(i)
                    self.queue.remove(plane)
                    break

            if [plane,waiting] in self.queue:
                self.queue[self.queue.index([plane,waiting])][1] += 1 #this is cancer and should not be allowed please report us
