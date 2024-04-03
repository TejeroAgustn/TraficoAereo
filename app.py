from Representation.AirTrafficServer import AirTrafficServer
from Model.AirTrafficModel import AirTrafficModel

if __name__ == "__main__":
    server = AirTrafficServer(AirTrafficModel, 10, 10)
    server.launch()
