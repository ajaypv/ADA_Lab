graph = {
    'a' : ['b','c'],
    'b':['a','b','e'],
    'c':['a','e'],
    'd':['b','e','f'],
    'e':['b','c','d','f'],
    'f':['d','f']
}

def dfs(graph,node,visted):
    if node not in visted:
        visted.append(node)
        for k in graph[node]:
            dfs(graph,k,visted)
        return visted
visted = dfs(graph,'a',[])
for i in visted:
    print(i)