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
            return self.distance > other.distance

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
