from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from Model.AirTrafficModel import AirTrafficModel
from Agents.Airport import Airport
from Agents.Plane import Plane

class AirTrafficServer:
    def __init__(self, model_cls, width, height):
        self.model_cls = model_cls
        self.width = width
        self.height = height

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
                       {"num_airports": 5,  # Aquí debes especificar el número deseado de aeropuertos
                        "num_planes": 20,   # Aquí debes especificar el número deseado de aviones
                        "width": self.width,
                        "height": self.height})

        server.port = 8521  # The default
        server.launch()
