from mesa import Agent

class Plane(Agent):
    def __init__(self, unique_id, model, origin, destination, wait_time_airport, wait_time_takeoff, wait_time_landing):
        super().__init__(unique_id, model)
        self.origin = origin
        self.destination = destination
        self.location = origin.location
        self.wait_time_airport = wait_time_airport
        self.vueling = False
        self.waiting = False

    def request_airstrip(self):
        self.origin.request_airstrip(self)

    def travel(self):
        # move towards destination
        pass

    

    def step(self):

        if self.location == self.destination:
            if self.vueling and not self.waiting:
                # Vamos a pedir aterrizaje
            elif self.vueling and self.waiting:
                # Hemos pedido pero no nos lo han dado aún
            elif self.wait_time_airport > 0 and not self.vueling and not self.waiting:
                # Nos han dado el permiso
            else # self.wait_time_airport = 0 and not self.vueling and not self.waiting:
                # Esto quiere decir que hemos aterrizado, hacemos cambios para volver a despegar
                
            
        elif self.location == self.origin:
            if self.wait_time_airport > 0 and not self.vueling and not self.waiting:
                # Acabamos de aterrizar
            elif not self.vueling and not self.waiting:
                # Vamos a pedir despegue
            elif not self.vueling and self.waiting:
                # Hemos pedido pero no nos lo han dado
            else:
                # Hemos despegao y hay que moverse
        else:
            # Nos movemos