matrix = []
with open('input.txt') as file:
    for line in file:
        l = line.rstrip().split(' ')
        matrix.append(l)

def checkRightDiag(row,col,n,m):
    total = 1
    for i in range(0,n):
        total*=int(m[row+i][col+i])
    return total

def checkLeftDiag(row,col,n,m):
    total = 1
    for i in range(0,n):
        total*=int(m[row+i][col-i])
    return total

def checkRight(row,col,n,m):
    total = 1
    for i in range(0,n):
        total*=int(m[row][col+i])
    return total

def checkDown(row,col,n,m):
    total = 1
    for i in range(0,n):
        total*=int(m[row+i][col])
    return total

def findMaxProduct(n,m):
    total = horz = vert = leftDiag = rightDiag = 0
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            if(i<len(m)-(n-1)):
                horz = checkDown(i,j,n,m)
                if(j<len(m[i])-(n-1)):
                    rightDiag = checkRightDiag(i,j,n,m)
                if(j>=(n-1)):
                    leftDiag = checkLeftDiag(i,j,n,m)
            if(j<len(m[i])-(n-1)):
                vert = checkRight(i,j,n,m)
            total = max(total,horz,vert,leftDiag,rightDiag)
    return total

print(findMaxProduct(4,matrix))
