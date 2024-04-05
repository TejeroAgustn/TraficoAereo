from mesa import Agent

class Plane(Agent):
    def __init__(self, unique_id, model, origin, destination, wait_time_airport, wait_time_takeoff, wait_time_landing):
        super().__init__(unique_id, model)
        self.origin = origin
        self.destination = destination
        self.location = origin.location
        self.wait_time_airport = wait_time_airport
        self.wait_time_takeoff = wait_time_takeoff
        self.wait_time_landing = wait_time_landing
        self.vueling = False
        self.waiting = False

    def request_airstrip(self):
        self.origin.request_airstrip(self)

    def travel(self):
        if abs(self.destination.location[0] - self.location[0]) > abs(self.destination.location[1] - self.location[1]):
            self.location[0] = self.location[0] + 1 if self.destination.location[0] > self.location[0] else self.location[0] - 1
        else:
            self.location[1] = self.location[1] + 1 if self.destination.location[1] > self.location[1] else self.location[1] - 1
    

    def step(self):

        if self.location == self.destination:
            if self.vueling and not self.waiting:
                # Vamos a pedir aterrizaje
                self.destination.request_airstrip(self)
                self.waiting = True
            elif self.vueling and self.waiting:
                # Hemos pedido pero no nos lo han dado aún
                pass
            elif self.wait_time_airport > 0 and not self.vueling and not self.waiting:
                # Nos han dado el permiso
                self.wait_time_airport -= 1
            else # self.wait_time_airport = 0 and not self.vueling and not self.waiting:
                # Esto quiere decir que hemos aterrizado, hacemos cambios para volver a despegar
                
            
        elif self.location == self.origin:
            if self.wait_time_airport > 0 and not self.vueling and not self.waiting:
                # Acabamos de aterrizar
            elif not self.vueling and not self.waiting:
                # Vamos a pedir despegue
            elif not self.vueling and self.waiting:
                # Hemos pedido pero no nos lo han dado
                pass
            else:
                # Hemos despegao y hay que moverse
        else:
            # Nos movemos