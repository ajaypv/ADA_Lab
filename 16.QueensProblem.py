global N 
N=4
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j])
        print()
def issafe(board,row,col):
    for i in range(col):
        if board[row][i] ==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,N,1), range(col,-1,-1)):
        if board[i][j] ==1:
            return False
        return True
def sloveNQutil(board,col):
    if col>=N:
        return True
    for i in range(N):
        if issafe(board,i,col):
            board[i][col]= 1
            if sloveNQutil(board,col+1) ==True:
                return True
            board[i][col]=0
    return False

def solveNQ():
    board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    if sloveNQutil(board,0) ==False:
        print('solution does not exitst')
        return False
    printSolution(board)
    return True
solveNQ()
            
            