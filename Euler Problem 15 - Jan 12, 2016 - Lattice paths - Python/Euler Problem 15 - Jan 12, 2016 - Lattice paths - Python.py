import time

def getGrid(n):
    grid = []
    row = []
    for i in range(0,n):
        row.append(0)
    for i in range(0,n):
        grid.append(list(row))
    grid[0][0] = 1
    return grid

def printGrid(grid):
    for i in grid:
        print(i)

def topological(n,grid):
    verticies = [(0,0)]
    while(len(verticies) > 0):
        tempVert = []
        for i in verticies:
            if(i[0] < n - 1):
                newVert = (i[0]+1,i[1])
                grid[newVert[0]][newVert[1]] += grid[i[0]][i[1]]
                if(newVert not in tempVert):
                    tempVert.append(newVert)
            if(i[1] < n -1):
                newVert = (i[0],i[1]+1)
                grid[newVert[0]][newVert[1]] += grid[i[0]][i[1]]
                if(newVert not in tempVert):
                    tempVert.append(newVert)
        verticies = list(tempVert)
    print(grid[n-1][n-1])

size = 20
grid = getGrid(size+1)
#printGrid(grid)
topological(size+1,grid)
#printGrid(grid)


        
