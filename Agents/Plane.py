from mesa import Agent

class Plane(Agent):
    def __init__(self, unique_id, model, origin, destination, wait_time_airport, wait_time_takeoff, wait_time_landing, spid):
        super().__init__(unique_id, model)
        self.origin = origin
        self.destination = destination
        self.pos = destination.pos 
            # La localización inicial está puesta como destino cuando en realidad desde el modelo está puesto el origen como destino
            # es una ñapa para que en el caso inicial piense que está en el caso en el que acaba de aterrizar y lo que haga sea 
            # intercambiar origen y destino  y pedir permiso para salir
        self.airstrip = -1
        self.wait_time_airport = wait_time_airport
        self.wait_time_takeoff = wait_time_takeoff
        self.wait_time_landing = wait_time_landing
        self.vueling = False
        self.waiting = False
        self.total_landig_waiting_time = 0
        self.total_takeoff_waiting_time = 0
        self.total_landings = -1
        self.total_takeoffs = 0

        self.spid = spid

    def travel(self):
        x, y = self.pos

        dist_x = self.destination.pos[0] - x
        dist_y = self.destination.pos[1] - y

        if abs(dist_x) > abs(dist_y):
            if (abs(dist_x) >= self.spid):
                x = x + self.spid  if self.destination.pos[0] > x else x - self.spid 
            else:
                x = x + dist_x
        else:
            if (abs(dist_y) >= self.spid):
                y = y + self.spid  if self.destination.pos[1] > y else y - self.spid 
            else:
                y = y + dist_y
            

        self.model.grid.move_agent(self, (x, y)) 
    
    def accept_request(self, airstrip):
        self.airstrip = airstrip
        self.waiting = False

        if self.pos == self.destination.pos:
            self.wait_time_airport = self.wait_time_landing 
            self.vueling = False
        else:
            self.wait_time_airport = self.wait_time_takeoff
            self.vueling = True
            
        return self.wait_time_airport

    def step(self):
        if self.pos == self.destination.pos:
            if self.vueling and not self.waiting:
                # Vamos a pedir aterrizaje
                self.destination.request_airstrip(self)
                self.waiting = True
            elif self.vueling and self.waiting:
                # Hemos pedido pero no nos lo han dado aún
                self.total_landig_waiting_time += 1
            elif self.wait_time_airport > 0:
                # Nos han dado el permiso
                self.wait_time_airport -= 1
            else: # self.wait_time_airport = 0 and not self.vueling and not self.waiting:
                # Esto quiere decir que hemos aterrizado, hacemos cambios para volver a despegar
                self.destination.confirm_landing(self.airstrip)
                self.total_landings += 1
                self.airstrip = -1
                self.destination, self.origin = self.origin, self.destination
                self.origin.request_airstrip(self)
                self.waiting = True



        elif self.pos == self.origin.pos:
            # He quitado esto porque cuando aterrizamos e intercambiamos las variable va a ser cuando pidamos ya para despegar y nos quedemos esperando
            #if self.wait_time_airport > 0 and not self.vueling and not self.waiting:
                # Acabamos de aterrizar
            #    pass
            #if not self.vueling and not self.waiting:
                # Vamos a pedir despegue
            #    pass
            if not self.vueling and self.waiting:
                # Hemos pedido pero no nos lo han dado
                self.total_takeoff_waiting_time += 1
            elif self.wait_time_airport > 0:
                # Nos han dado el permiso
                self.wait_time_airport -= 1
            else: # self.wait_time_airport = 0 and self.vueling and not self.waiting:
                # Hemos despegao y hay que moverse
                self.origin.confirm_takeoff(self.airstrip)
                self. total_takeoffs += 1
                self.airstrip = -1
                self.travel()
        else:
            self.travel()