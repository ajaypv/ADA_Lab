graph = {
    'a' : ['b','c'],
    'b':['a','b','e'],
    'c':['a','e'],
    'd':['b','e','f'],
    'e':['b','c','d','f'],
    'f':['d','f']
}

visited =[]
queue =[]

def bfs(visited,graph,node):
    print(node)
    visited.append(node)
    queue.append(node)
    print(queue)
    while queue:
        s =queue.pop(0)
        print(s)
        for n in graph[s]:
            print('this is graph[s]',graph[s])
            print('this is n value',n)
            if n not in visited:
                visited.append(n)
                queue.append(n)
bfs(visited,graph,'a')