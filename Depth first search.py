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
        if not self.directed:
            self.graph[dest].append(src)
            
    #depth first search
    def dfs(self,vertex,visited=None):
        if visited is None:
            visited = {}
        if vertex not in visited:
            print(vertex,end='')
            visited[vertex]=True
            for neighbour in self.graph[vertex]:
                self.dfs(neighbour,visited)
                
G=Graph()#creating an object
G.addEdge('A','B')
G.addEdge('C','A')
G.addEdge('B','D')
G.addEdge('A','D')
G.addEdge('B','D')
G.dfs('A')
                
