#Depth-first-search
# import sys
# import os

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

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

    def DFS(self, start, objective):

        # Ingreso de nodos
        start = self.find_node(start)
        target = self.find_node(objective)

        # Verificacion
        if (start is None) or (target is None):
            print(f'No hay nodos con coordenadas {start} o {objective}')
            return

        # Start queue
        queue = []
        queue.append(start)

        self.opened.append(start)

        while True:
            if len(self.opened) == 0:
                return { 'solutionPath': [] }

            
            # FIFO structure
            current_node = self.opened.pop()
            self.closed.append(current_node)
            
            if current_node == target:
                solution_path = self.unwrap_path(target)
                exploration_paths = list(map(self.unwrap_path, self.closed))

                return {
                    'solutionPath': solution_path,
                    'explorationPaths': exploration_paths,
                }
            
            # Traverse through children
            if len(current_node.neighbors) > 0:
                for node in current_node.neighbors:
                    if node not in self.opened and node not in self.closed:
                        node.parent = current_node
                        self.opened.append(node)

# Test drive
if __name__ == "__main__":
    g = Graph ()

    g.add_node((0, 0))
    g.add_node((0, 1))
    g.add_node((0, 3))
    g.add_node((1, 0))
    g.add_node((1, 1))
    g.add_node((1, 2))
    g.add_node((1 ,3))
    g.add_node((2, 0))
    g.add_node((2, 3))
    g.add_node((3, 0))
    g.add_node((3, 1))
    g.add_node((3, 2))
    g.add_node((3, 3))

    g.add_edge((0, 0), (0, 1))
    g.add_edge((0, 0), (1, 0))
    g.add_edge((0, 1), (1, 1))
    g.add_edge((0, 3), (1, 3))
    g.add_edge((1, 0), (1, 1))
    g.add_edge((1, 0), (2, 0))
    g.add_edge((1, 1), (1, 2))
    g.add_edge((1, 2), (1, 3))
    g.add_edge((1, 3), (2, 3))
    g.add_edge((2, 0), (3, 0))
    g.add_edge((2, 3), (3, 3))
    g.add_edge((3, 0), (3, 1))
    g.add_edge((3, 1), (3, 2))
    g.add_edge((3, 2), (3, 3))

    print(g.DFS((0,0), (3,2)))
