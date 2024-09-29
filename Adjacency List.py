class Graph:
    #using adjacency list
    def __init__(self): 
        self.graph={}
        self.directed=False
    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def addEdge(self,src,dest):
        self.addVertex(src)
        self.addVertex(dest)
        self.graph[src].append(dest)
        if not self.directed:
            self.graph[dest].append(src)
            
    def displayGraph(self):
        for vertex in self.graph:
            print(f"{vertex}--->{self.graph[vertex]}")
            
G=Graph()
G.addEdge('A','B')
G.addEdge('C','A')
G.addEdge('B','D')
G.addEdge('A','D')
G.addEdge('B','D')
G.displayGraph()

