# IDS Search
from collections import defaultdict
 
class Graph:
    
    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
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