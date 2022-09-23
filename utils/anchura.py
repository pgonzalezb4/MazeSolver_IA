# Breadth-First-Search
from collections import defaultdict
import numpy as np

class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.graph[v]:
            self.graph[v]

    def BFS(self, start, objective):

        # Visited nodes
        print(self.graph)                       #PRINT
        visited = np.zeros(len(self.graph)+1, dtype=int)

        # Start queue
        queue = []
        queue.append(start)

        while queue:
            # FIFO structure
            current_node = queue.pop(0)
            visited[current_node] = 1
            print(current_node, end=' ')        #PRINT
            
            if current_node == objective:
                return True
            
            # Traverse through children
            for node in self.graph[current_node]:
                if visited[node] == 0:
                    queue.append(node)



if __name__ == "__main__":
    g = Graph()
    g.addEdge(0,1)
    g.addEdge(0,6)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(2,4)
    g.addEdge(1,5)
    g.addEdge(6,7)

    g.BFS(0, 0)