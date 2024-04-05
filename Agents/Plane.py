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

    def travel(self):
        if abs(self.destination.location[0] - self.location[0]) > abs(self.destination.location[1] - self.location[1]):
            self.location[0] = self.location[0] + 1 if self.destination.location[0] > self.location[0] else self.location[0] - 1
        else:
            self.location[1] = self.location[1] + 1 if self.destination.location[1] > self.location[1] else self.location[1] - 1
    
    def accept_request(self):
        self.waiting = False

        if self.location == self.destination:
            self.wait_time_airport = self.wait_time_landing 
            self.vueling = False
        else:
            self.wait_time_airport = self.wait_time_takeoff
            self.vueling = True

    def step(self):

        if self.location == self.destination:
            if self.vueling and not self.waiting:
                # Vamos a pedir aterrizaje
                self.destination.request_airstrip(self)
                self.waiting = True
            elif self.vueling and self.waiting:
                # Hemos pedido pero no nos lo han dado aún
                pass
            elif self.wait_time_airport > 0:
                # Nos han dado el permiso
                self.wait_time_airport -= 1
            else: # self.wait_time_airport = 0 and not self.vueling and not self.waiting:
                # Esto quiere decir que hemos aterrizado, hacemos cambios para volver a despegar
                self.destination, self.origin = self.origin, self.destination
                self.origin.request_airstrip(self)
                self.waiting = True



        elif self.location == self.origin:
            # He quitado esto porque cuando aterrizamos e intercambiamos las variable va a ser cuando pidamos ya para despegar y nos quedemos esperando
            #if self.wait_time_airport > 0 and not self.vueling and not self.waiting:
                # Acabamos de aterrizar
            #    pass
            #if not self.vueling and not self.waiting:
                # Vamos a pedir despegue
            #    pass
            if not self.vueling and self.waiting:
                # Hemos pedido pero no nos lo han dado
                pass
            elif self.wait_time_airport > 0:
                # Nos han dado el permiso
                self.wait_time_airport -= 1
            else: # self.wait_time_airport = 0 and self.vueling and not self.waiting:
                # Hemos despegao y hay que moverse
                self.travel()
        else:
            self.travel()