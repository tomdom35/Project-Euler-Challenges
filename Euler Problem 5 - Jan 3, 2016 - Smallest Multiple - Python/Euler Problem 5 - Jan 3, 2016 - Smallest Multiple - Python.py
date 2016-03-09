def findSmallestMultiple(n):
    m = n
    found=False
    while(not found):
        for i in range(1,n+1):
            if(m%i!=0):
                m+=n
                break
            elif(i==n):
                found=True
                return m
        
print(findSmallestMultiple(20))
