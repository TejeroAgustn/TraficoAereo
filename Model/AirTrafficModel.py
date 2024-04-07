from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from Agents.Airport import Airport
from Agents.Plane import Plane
import sys
from mesa.datacollection import DataCollector

class AirTrafficModel(Model):
    def __init__(self, width, height, num_airports, num_planes, max_num_aisrstrips, max_plane_speed, 
                 tiempo_simulacion, tiempo_entre_despegues_aterrizajes, max_time_waiting):
        
        super().__init__()
        self.num_airports = num_airports
        self.num_planes = num_planes
        self.grid = MultiGrid(width, height, False)

        self.width = width
        self.height = height

        self.tiempo_simulacion = tiempo_simulacion
        self.tiempo_entre_despegues_aterrizajes = tiempo_entre_despegues_aterrizajes
        self.max_time_waiting = max_time_waiting

        self.datacollector = DataCollector(
            # Define las variables que deseas recopilar
            agent_reporters={"Num_Airports": lambda m: m.num_airports,
                             "Num_Planes": lambda m: m.num_planes}
        )

        self.schedule = RandomActivation(self)
        self._steps = 1  # Inicializamos el contador de pasos
        
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
            
            max_airstrips = 0
            min_airstrips = sys.maxsize
            mean_airstrips = 0

            max_airport_takeoffs = 0
            min_airport_takeoffs = sys.maxsize
            mean_airport_takeoffs = 0
            
            
            max_airport_landings = 0
            min_airport_landings = sys.maxsize
            mean_airport_landings = 0

            for airport in self.schedule.agents:
                if isinstance(airport, Airport):
                    if len(airport.airstrips) > max_airstrips:
                        max_airstrips = len(airport.airstrips)
                    if len(airport.airstrips) < min_airstrips:
                        min_airstrips = len(airport.airstrips)
                    mean_airstrips += len(airport.airstrips)

                    if airport.total_takeoffs > max_airport_takeoffs:
                        max_airport_takeoffs = airport.total_takeoffs
                    if airport.total_takeoffs < min_airport_takeoffs:
                        min_airport_takeoffs = airport.total_takeoffs
                    mean_airport_takeoffs += airport.total_takeoffs

                    if airport.total_landings > max_airport_landings:
                        max_airport_landings = airport.total_landings
                    if airport.total_landings < min_airport_landings:
                        min_airport_landings = airport.total_landings
                    mean_airport_landings += airport.total_landings

            mean_airstrips = mean_airstrips / self.num_airports
            mean_airport_takeoffs = mean_airport_takeoffs / self.num_airports
            mean_airport_landings = mean_airport_landings / self.num_airports


            variables = f"""
                  Tiempo total en minutos: {self._steps}
                  Número de vuelos totales: #suma de cuanto ha volado cada avion
                  Número de aeropuertos: {self.num_airports}
                  Número de aviones: {self.num_planes}
                  Dimensiones de la cuadrícula: {self.width} x {self.height}
                  Máximo, mínimo y valor medio de pistas de aeropuertos: {max_airstrips} , {min_airstrips} , {mean_airstrips}
                  Máximo, mínimo y valor medio de despegues por aeropuerto: {max_airport_takeoffs} , {min_airport_takeoffs} , {min_airport_takeoffs}
                  Máximo, mínimo y valor medio de despegues por avion: 
                  Máximo, mínimo y valor medio de aterrizajes por aeropuerto: {max_airport_landings} , {min_airport_landings} , {min_airport_landings}
                  Máximo, mínimo y valor medio de aterrizajes por avion:
                  Máximo, mínimo y valor medio de retrasos en despegues por aeropuerto:
                  Máximo, mínimo y valor medio de retrasos en despegues por avion:
                  Máximo, mínimo y valor medio de retrasos en aterrizajes por aeropuerto: 
                  Máximo, mínimo y valor medio de retrasos en aterrizajes por avion: 
                """
            print(variables)
            sys.exit()
