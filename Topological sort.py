from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  
        self.vertices = vertices        

    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v"""
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        """A recursive helper function to perform DFS and store the topological order"""
        visited[v] = True  
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

     
        stack.append(v)

    def topological_sort(self):
        """Perform topological sort"""
        visited = [False] * self.vertices  
        stack = []                         

        
        for i in range(self.vertices):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack[::-1]

# Example:
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

topological_order = g.topological_sort()
print("Topological Sort of the given graph is:", topological_order)
