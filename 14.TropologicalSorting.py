from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.N=n
        self.graph=defaultdict(list)

    def add_edje(self,m,n):
        self.graph[m].append(n)

    def sort(self,n,visited,stack):
        visited[n]=True
        for i in self.graph[n]:
            if visited[i]==False:
                self.sort(i,visited,stack)
        stack.insert(0,n)

    def top(self):
        visited=[False]*self.N
        stack=[]
        for i in range(self.N):
            if visited[i]==False:
                self.sort(i,visited,stack)
        print(stack)
g=Graph(5)
g.add_edje(0,1)
g.add_edje(0,3)
g.add_edje(1,2)
g.add_edje(2,3)
g.add_edje(2,4)
g.add_edje(3,4)
g.top()