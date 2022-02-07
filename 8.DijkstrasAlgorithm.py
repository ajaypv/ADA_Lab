import sys
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[[0 for column in range(vertices)]
        for rows in range(vertices)]

    def print_solution(self,dist):
        for node in range(self.v):
            print(node,"\t",dist[node]) 
            

    def distance(self,dist,sptSet):
        min = sys.maxsize
 
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.v):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
        

    def dijkstras(self,src):
        dist=[sys.maxsize]*self.v 
        dist[src]=0
        sptSet=[False]*self.v 
        for i in range(self.v):
            x=self.distance(dist,sptSet)
            sptSet[x]=True
            for y in range(self.v):
                if self.graph[x][y]>0 and sptSet[y]==False and dist[y] > dist[x]+self.graph[x][y]:
                    dist[y]=dist[x]+self.graph[x][y]
        self.print_solution(dist)

g=Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
g.dijkstras(0)