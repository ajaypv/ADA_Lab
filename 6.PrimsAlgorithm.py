inf =999
v =5
g = [ [0,9,75,0,0],
      [9,0,95,19,42],
        [75,95,0,0,66],
        [0,19,51,0,31],
        [0,42,66,31,0]]

selected =[0,0,0,0,0]
no_edge = 0
selected[0]= True
while no_edge < v-1:
    x=0
    y=0
    min =inf
    for i in range(v):
        if selected[i]:
            for j in range(v):
                if not selected[j] and g[i][j]:
                    if min>g[i][j]:
                        min = g[i][j]
                        x=i
                        y=j
    print(x,y,g[x][y])
    selected[y]=True
    no_edge += 1


