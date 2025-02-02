import sys
import heapq
import os

class City: # vertex no slide eduardo
    def __init__(self, id):
        self.id = id 
        self.connectedTo = {} 

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys() 

    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo.get(nbr, float('inf')) 

    def __lt__(self, other): #less than
        return self.id < other.id

class Flight: # graph no slide eduardo
    def __init__(self):
        self.vertList = {} 
        self.numVertices = 0

    def addCity(self, key):
        if key not in self.vertList:
            self.vertList[key] = City(key)

    def getCity(self, key):
        return self.vertList.get(key, None)

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            self.addCity(f)
        if t not in self.vertList:
            self.addCity(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

def dijkstra(Flight, start, end):
    priorityQueue = []
    start_City = Flight.getCity(start)
    heapq.heappush(priorityQueue, (0, start_City, [start]))

    distancias = {City: float('inf') for City in Flight.getVertices()}
    distancias[start] = 0

    while priorityQueue:
        currentDistance, currentCity, route = heapq.heappop(priorityQueue)

        if currentCity.getId() == end:
            return route, currentDistance

        if currentDistance > distancias[currentCity.getId()]:
            continue

        for neighbor in currentCity.getConnections():
            distance = currentDistance + currentCity.getWeight(neighbor)

            if distance < distancias[neighbor.getId()]:
                distancias[neighbor.getId()] = distance
                heapq.heappush(priorityQueue, (distance, neighbor, route + [neighbor.getId()]))

    return None, None 

def main():
    fin = sys.stdin
    fout = sys.stdout

    M = int(fin.readline().strip())

    for _ in range(M):
        origin, destination = fin.readline().strip().split()
        N = int(fin.readline().strip())

        Flight = Flight()

        for _ in range(N):
            city_origin, city_destination, time = fin.readline().strip().split()
            time = float(time)
            Flight.addEdge(city_origin, city_destination, time)

        route, totalTime = dijkstra(Flight, origin, destination)
        fout.write(f"Origem: {origin} Destino: {destination}\n")

        if route is None:
            fout.write("Não há rota possível.\n")

        else:
            for i in range(len(route) - 1):
                origin_route = route[i]
                destino_route = route[i + 1]
                time = Flight.getCity(origin_route).getWeight(Flight.getCity(destino_route))
                fout.write(f"{origin_route} {destino_route} {time:.2f}\n")
            fout.write(f"Tempo total: {totalTime:.1f} horas.\n")

        fout.write("\n")
    
    print("foi!")

if __name__ == "__main__":
    main()