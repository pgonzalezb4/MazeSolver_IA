# IDS Search
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from domain.node import Node
 
class Graph:
    
    # Constructor
    def __init__(self):
        self.nodes = []
        self.opened = []
        self.closed = []

    def add_node(self, coords):
        self.nodes.append(Node(coords))

    def find_node(self, coord):
        for node in self.nodes:
            if (node.x == coord[0]) and (node.y == coord[1]):
                return node
        return None

    def add_edge(self, coord1, coord2):
        node1 = self.find_node(coord1)
        node2 = self.find_node(coord2)
        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor(node2)
            node2.add_neighboor(node1)
        else:
            print(f'No hay nodos con coordenadas {coord1} o {coord2}')

    def unwrap_path(self, node):
        path = [(node.x, node.y)]
        node = node.parent
        while True:
            if node is None:
                break
            path.append((node.x, node.y))
            if node.parent is None:
                break
            node = node.parent
        path.reverse()

        return path
 
    def aux_func(self,start,objective,maxDepth):
        if start == objective : return True
 
        # Stop when at bottom
        if maxDepth <= 0 : return False
 
        # FIFO structure
        for i in self.graph[start]:
                print(i)                        #PRINT
                if(self.aux_func(i,objective,maxDepth-1)):
                    return True
        return False
 
    def IDS(self,start, objective, maxDepth):

        # Ingreso de nodos
        start = self.find_node(start)
        target = self.find_node(objective)
        maxDepth = 1

        # Verificacion
        if (start is None) or (target is None):
            print(f'No hay nodos con coordenadas {start} o {objective}')
            return

        self.opened.append(start)

        while True:
            maxDepth +=1
            if len(self.opened) == 0:
                return { 'solutionPath': [] }

            current_node = self.opened.pop(0)
            self.closed.append(current_node)

            if current_node == target:
                solution_path = self.unwrap_path(target)
                exploration_paths = list(map(self.unwrap_path, self.closed))

                return {
                    'solutionPath': solution_path,
                    'explorationPaths': exploration_paths,
                }
            
            for node in current_node.neighbors:
                small_queue = []
                if node not in self.opened and node not in self.closed:
                        node.parent = current_node
                        small_queue.append(node)



        # Reccur for all depths
        for i in range(maxDepth):
            print(f'Depth: {i}')                #PRINT
            if (self.aux_func(start, objective, i)):
                return True
        return False
 
# Test drive
if __name__ == "__main__":
    g = Graph ()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    g.addEdge(3, 7)
    g.addEdge(3, 8)
    g.addEdge(5, 9)
    g.addEdge(5, 10)
    
    objective = 9; maxDepth = 4; start = 0

    print(f"Recorrido desde {start} hasta {objective}")

    g.IDS(start, objective, maxDepth)