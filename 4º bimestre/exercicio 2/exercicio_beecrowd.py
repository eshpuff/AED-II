import sys
import heapq

class City:
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

    def __lt__(self, other):  # Necessário para o heapq
        return self.id < other.id

class Flight:
    def __init__(self):
        self.vertList = {}

    def addCity(self, key):
        if key not in self.vertList:
            self.vertList[key] = City(key)

    def getCity(self, key):
        return self.vertList.get(key, None)

    def addEdge(self, f, t, weight=0):
        self.addCity(f)
        self.addCity(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

def dijkstra(flightGraph, start, end):
    if start not in flightGraph.vertList or end not in flightGraph.vertList:
        return None, None

    priorityQueue = []
    start_City = flightGraph.getCity(start)
    heapq.heappush(priorityQueue, (0, start_City, [start]))

    distancias = {city: float('inf') for city in flightGraph.getVertices()}
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

        flightGraph = Flight()

        for _ in range(N):
            cityOrigin, cityDestination, time = fin.readline().strip().split()
            time = float(time)
            flightGraph.addEdge(cityOrigin, cityDestination, time)

        route, totalTime = dijkstra(flightGraph, origin, destination)

        fout.write(f"Origem: {origin} Destino: {destination}\n")

        if route is None:
            fout.write("Não há rota possível.\n")
        else:
            for i in range(len(route) - 1):
                originRoute = route[i]
                destinoRoute = route[i + 1]
                time = flightGraph.getCity(originRoute).getWeight(flightGraph.getCity(destinoRoute))
                fout.write(f"{originRoute} {destinoRoute} {time:.1f}\n")
            fout.write(f"Tempo total: {totalTime:.1f} horas.\n")

        fout.write("\n")

if __name__ == "__main__":
    main()
