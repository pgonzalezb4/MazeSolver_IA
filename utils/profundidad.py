#Depth-first-search
from collections import defaultdict

class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited, objective):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        if v == objective:
            return True

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                status = self.DFSUtil(neighbour, visited, objective)
                print(" UP ")
                if status:
                    return True

    def DFS(self, v, objective):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited, objective)

# in the above diagram
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
