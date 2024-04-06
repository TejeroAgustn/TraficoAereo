from Representation.AirTrafficServer import AirTrafficServer
from Model.AirTrafficModel import AirTrafficModel
import random

if __name__ == "__main__":
    # Caso 1 Todos los aeropuertos tendrán una única pista de aterrizaje/despegue. La velocidad de todos los aviones es la misma.
    #server = AirTrafficServer(AirTrafficModel, 2, 10, 1, 1)
    # Caso 2 Cada aeropuerto tendrá un número diferente de pistas, generado aleatoriamente al comienzo de la simulación. 
    # Este valor deberá estar comprendido entre el máximo y mínimo valor establecidos
    server = AirTrafficServer(AirTrafficModel, tam_cuadricula=70, tiempo_simulacion=200, num_airports=10, 
                              num_planes=1000, max_num_aisrstrips=5, max_plane_speed=5)
    server.launch()
