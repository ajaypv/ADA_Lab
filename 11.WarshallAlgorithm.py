class Graph:
    def __init__(self,vertices):
        self.v =vertices
    def printsolution(self,reach):
        for i in range(self.v):
            for j in range(self.v):
                if i==j:
                    print(1 ,'\t',end='')
                else:
                    print(reach[i][j],'\t',end='')
                    print()
    def warsh(self,graph):
        reach =[i[:] for i in graph]
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    reach[i][j]= reach[i][j] or reach[i][k] and (reach[k][j] or reach[k][j])
        self.printsolution(reach)
g = Graph(4)
graph = [[1,1,0,1],[0,1,1,0],[0,0,1,1],[0,0,0,1]]
g.warsh(graph)

