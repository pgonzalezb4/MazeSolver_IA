#Depth-first-search
from collections import defaultdict

class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # Create LIFO structure
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def aux_func(self, v, visited, objective):

        # Mark the current node as visited
        visited.add(v)
        print(v, end=' ')           #PRINT

        # If found, stop the process
        if v == objective:
            return True

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                status = self.aux_func(neighbour, visited, objective)
                print(" UP ")       #PRINT
                if status:
                    return True

    def DFS(self, v, objective):
        visited = set()
        self.aux_func(v, visited, objective)

# Test drive
if __name__ == "__main__":
    g = Graph()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)
    g.addEdge(2, 0)
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(4, 5)

    inicio = 2
    objetivo = 5
    print(f"Recorrido desde {inicio} hasta {objetivo}")
    g.DFS(inicio, objetivo)
