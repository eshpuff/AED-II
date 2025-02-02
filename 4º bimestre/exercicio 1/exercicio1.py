import sys
import heapq

class Vertex:
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

    def __lt__(self, other):
        return self.id < other.id

class Graph:
    def __init__(self):
        self.vertList = {}

    def addVertex(self, key):
        if key not in self.vertList:
            self.vertList[key] = Vertex(key)

    def getVertex(self, key):
        return self.vertList.get(key, None)

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

def dijkstra(graph, start, end):
    priorityQueue = []
    start_vertex = graph.getVertex(start)
    heapq.heappush(priorityQueue, (0, start_vertex, [start]))

    distances = {vertex: float('inf') for vertex in graph.getVertices()}
    distances[start] = 0

    while priorityQueue:
        currentDistance, currentVertex, path = heapq.heappop(priorityQueue)

        if currentVertex.getId() == end:
            return path, currentDistance

        if currentDistance > distances[currentVertex.getId()]:
            continue

        for neighbor in currentVertex.getConnections():
            distance = currentDistance + currentVertex.getWeight(neighbor)

            if distance < distances[neighbor.getId()]:
                distances[neighbor.getId()] = distance
                heapq.heappush(priorityQueue, (distance, neighbor, path + [neighbor.getId()]))

    return None, None

def main():
    M = int(sys.stdin.readline().strip())

    for _ in range(M):
        origin, destination = sys.stdin.readline().strip().split()
        N = int(sys.stdin.readline().strip())

        graph = Graph()

        for _ in range(N):
            city_origin, city_destination, time = sys.stdin.readline().strip().split()
            time = float(time)
            graph.addEdge(city_origin, city_destination, time)

        path, timeTotal = dijkstra(graph, origin, destination)

        print(f"Origem:{origin} Destino:{destination}")

        if path is None:
            print("Não há rota possível.")
        else:
            for i in range(len(path) - 1):
                origin_path = path[i]
                destino_path = path[i + 1]
                time = graph.getVertex(origin_path).getWeight(graph.getVertex(destino_path))
                print(f"{origin_path} {destino_path} {time:.2f}")
            print(f"Tempo total: {timeTotal:.1f} horas.")

        print()

if __name__ == "__main__":
    main()
