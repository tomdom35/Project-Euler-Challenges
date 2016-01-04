matrix = []
with open('input.txt') as file:
    for line in file:
        l = line.rstrip().split(' ')
        matrix.append(l)

def swapMatrix(m):
    swappedMatrix = []
    for i in range(0,len(m[0])):
        swappedMatrix.append([])
        for row in range(0,len(m)):
            swappedMatrix[i].append(m[row][i])
    return swappedMatrix

def flipMatrix(m):
    flippedMatrix = list(m)
    for row in flippedMatrix:
        row.reverse()
    return flippedMatrix
        

def findAdjacentProduct(n,m):
    total = 0
    for row in m:
        index = 0
        while(n+index<=len(row)):
            curTotal = 1
            for i in range(index,n+index):
                curTotal*=int(row[i])
            if curTotal>total:
                total=curTotal
            index+=1
    return total

def findDiagonalProduct(n,m):
    index = len(m)-1
    

def printMatrix(m):
    for row in m:
        print(row)

printMatrix(matrix)
print()
printMatrix(flipMatrix(matrix))


