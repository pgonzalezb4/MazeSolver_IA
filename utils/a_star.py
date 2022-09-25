# A-Star Search
class Node:

    # Constructor
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]
        self.distance = -1
        self.neighbors = []
        self.parent = None

    def add_neighboor(self, neighboor):
        self.neighbors.append(neighboor)

    # Para comparar
    def __gt__(self, other):
        if isinstance(other, Node):
            if self.distance > other.distance:
                return True
            if self.distance <= other.distance:
                return False

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y


    # Para imprimir
    def __str__(self):
        """
            Define that a node is printed with its value. 
            Returns
            -------
                str
        """
        return f'({self.x}, {self.y})'

class Graph:

    # Constructor
    def __init__(self):
        self.nodes = []
        self.opened = []
        self.closed = []

    def add_node(self, node):
        self.nodes.append(node)

    def find_node(self, coord):
        for node in self.nodes:
            if (node.x == coord[0]) and (node.y == coord[1]):
                return node
        return None

    def add_edge(self, coord1, coord2, weight=1):
        node1 = self.find_node(coord1)
        node2 = self.find_node(coord2)
        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor(node2)
            node2.add_neighboor(node1)
        else:
            print(f'No hay nodos con coordenadas {coord1} o {coord2}')

    def distance(self, node1, node2):
        return abs(node1.x - node2.x) + abs(node1.y - node2.y)

    def astar(self, start_coord, target_coord):

        # Ingreso de nodos
        start = self.find_node(start_coord)
        target = self.find_node(target_coord)

        # Verificacion
        if (start is None) or (target is None):
            print(f'No hay nodos con coordenadas {start_coord} o {target_coord}')
            return

        # Init
        start.distance = self.distance(start, start)
        self.opened.append(start)

        while True:
            if len(self.opened) == 0:
                print(f'No hay solución')
                break

            # Add to closed, remove from opened, organize opened by heuristic
            self.opened.sort()
            selected_node = self.opened.pop(0)
            self.closed.append(selected_node)

            if (selected_node.x == target_coord[0]) and (selected_node.y == target_coord[1]):
                print(f'Found solution!')
                # for i in self.closed:
                #     print(i, end=' ')
                #     print(f'Parent: {i.parent}\n')
                path = [(target.x, target.y)]
                node = target.parent
                while True:
                    if node is None:
                        break
                    path.append((node.x, node.y))
                    if node.parent is None:
                        break
                    node = node.parent
                path.reverse()
                print(path)
                break
            
            # Examinar paths por minima euristica
            if len(selected_node.neighbors) > 0:
                for node in selected_node.neighbors:
                    new_distance = selected_node.distance + self.distance(target, node)
                    if node not in self.opened and node not in self.closed:
                        node.parent = selected_node
                        node.distance = new_distance
                        self.opened.append(node)
                    elif node in self.opened and node.parent != selected_node:
                        if new_distance < node.distance:
                            node.parent = selected_node
                            node.distance = new_distance

# Test drive
if __name__ == "__main__":
    g = Graph ()

    g.add_node(Node((0, 0)))
    g.add_node(Node((0, 1)))
    g.add_node(Node((0, 3)))
    g.add_node(Node((1, 0)))
    g.add_node(Node((1, 1)))
    g.add_node(Node((1, 2)))
    g.add_node(Node((1 ,3)))
    g.add_node(Node((2, 0)))
    g.add_node(Node((2, 3)))
    g.add_node(Node((3, 0)))
    g.add_node(Node((3, 1)))
    g.add_node(Node((3, 2)))
    g.add_node(Node((3, 3)))

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

    g.astar((0,0), (3,2))