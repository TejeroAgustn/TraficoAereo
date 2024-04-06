from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from Model.AirTrafficModel import AirTrafficModel
from Agents.Airport import Airport
from Agents.Plane import Plane

class AirTrafficServer:
    def __init__(self, model_cls, tam_cuadricula, num_airports, num_planes, max_num_aisrstrips, max_plane_speed):
        self.model_cls = model_cls
        self.width = tam_cuadricula
        self.height = tam_cuadricula
        self.num_airports = num_airports
        self.num_planes = num_planes
        self.max_num_aisrstrips = max_num_aisrstrips
        self.max_plane_speed = max_plane_speed

    def agent_portrayal(self, agent):
        if isinstance(agent, Airport):
            return {
                "Shape": "rect",
                "Color": "blue",
                "Filled": "true",
                "Layer": 0,
                "w": 1,
                "h": 1
            }
        elif isinstance(agent, Plane):
            return {
                "Shape": "circle",
                "Color": "red",
                "Filled": "true",
                "Layer": 1,
                "r": 0.5
            }

    def launch(self):
        grid = CanvasGrid(self.agent_portrayal, self.width, self.height, self.width*10, self.height*10)

        chart = ChartModule([{"Label": "Paso de simulación", "Color": "Black"}],
                            data_collector_name='datacollector')

        server = ModularServer(self.model_cls,
                       [grid, chart],
                       "Air Traffic Model",
                       {"width": self.width,
                        "height": self.height,
                        "num_airports": self.num_airports,
                        "num_planes": self.num_planes,
                        "max_num_aisrstrips": self.max_num_aisrstrips,
                        "max_plane_speed":self.max_plane_speed
                        })

        server.port = 8521  # The default
        server.launch()
