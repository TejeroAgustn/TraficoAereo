from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from Agents.Airport import Airport
from Agents.Plane import Plane
from mesa.datacollection import DataCollector

class AirTrafficModel(Model):
    def __init__(self, width, height, num_airports, num_planes, max_num_aisrstrips, max_plane_speed, 
                 tiempo_simulacion, tiempo_entre_despegues_aterrizajes, max_time_waiting):
        
        super().__init__()
        self.num_airports = num_airports
        self.num_planes = num_planes
        self.grid = MultiGrid(width, height, False)

        self.tiempo_simulacion = tiempo_simulacion
        self.tiempo_entre_despegues_aterrizajes = tiempo_entre_despegues_aterrizajes
        self.max_time_waiting = max_time_waiting

        self.schedule = RandomActivation(self)
        self._steps = 0  # Inicializamos el contador de pasos
        # Define el DataCollector para recopilar datos de interés
        self.datacollector = DataCollector(
            # Define las variables que deseas recopilar
            agent_reporters={"Num_Airports": lambda m: m.num_airports,
                             "Num_Planes": lambda m: m.num_planes}
        )
        # Crear aeropuertos
        for i in range(num_airports):
            airport = Airport(i, self, random.randint(1, max_num_aisrstrips), random.randint(1, 5))
            self.grid.place_agent(airport, airport.pos)
            self.schedule.add(airport)

        # Crear aviones
        for i in range(num_planes):
            origin = random.choice([agent for agent in self.schedule.agents if isinstance(agent, Airport)])
            destination = random.choice([agent for agent in self.schedule.agents if isinstance(agent, Airport) and agent != origin])

            plane = Plane(i, self, destination, origin, random.randint(0, 10), random.randint(1, 5), random.randint(1, 5), random.randint(1, max_plane_speed))
            self.grid.place_agent(plane, origin.pos)
            self.schedule.add(plane)
    
    def step(self):
        if(self._steps < self.tiempo_simulacion):
            self.schedule.step()
        elif (self._steps == self.tiempo_simulacion):
            print("mis muertos")
