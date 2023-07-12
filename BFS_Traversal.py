from collections import defaultdict
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.visited=[]
 # Function to print a BFS of graph
    def BFS(self, s):
 
        # Create a queue for BFS
        queue = []
        queue.append(s)
        self.visited.append(s)
 
        while queue:
            s = queue.pop(0)
            print (s, end = " ")
 
            
            for i in self.graph[s]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.append(s)
  
# Create a graph given in
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)