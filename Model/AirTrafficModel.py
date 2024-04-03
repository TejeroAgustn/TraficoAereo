from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from Agents.Airport import Airport
from Agents.Plane import Plane
from mesa.datacollection import DataCollector

class AirTrafficModel(Model):
    def __init__(self, num_airports, num_planes, width, height):
        super().__init__()
        self.num_airports = num_airports
        self.num_planes = num_planes
        self.grid = MultiGrid(width, height, False)
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
            airport = Airport(i, self)
            self.grid.place_agent(airport, airport.location)
            self.schedule.add(airport)

        # Crear aviones
        for i in range(num_planes):
            origin = random.choice(self.schedule.agents)
            destination = random.choice(self.schedule.agents)
            while origin == destination:
                destination = random.choice(self.schedule.agents)
            plane = Plane(i, self, origin, destination)
            self.grid.place_agent(plane, origin.location)
            self.schedule.add(plane)
    
    def step(self):
        print("Paso de simulación:", self._steps)
        print(self.grid)
        self.schedule.step()
