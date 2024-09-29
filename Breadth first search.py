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
    #breadth first search        
    def bfs(self,StartVertex):
        queue=[StartVertex]
        visited={StartVertex:True}
        while queue:
            CurrentVertex=queue.pop(0)
            print(CurrentVertex,end='')
            for neighbour in self.graph[CurrentVertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited[neighbour]=True
            
G=Graph()#creating an object
G.addEdge('A','B')
G.addEdge('C','A')
G.addEdge('B','D')
G.addEdge('A','D')
G.addEdge('B','D')
G.bfs('A')
        
        