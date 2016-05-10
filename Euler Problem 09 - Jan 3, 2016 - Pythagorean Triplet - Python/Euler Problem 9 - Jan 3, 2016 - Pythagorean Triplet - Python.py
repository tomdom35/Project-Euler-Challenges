import math

def findPythagoreanTriplet(n):
    a = 1
    b = 1
    c = 1
    done = False
    while(not done):
        b+=1
        c = math.sqrt(a*a + b*b)
        if(a+b+c>n):
            a+=1
            b=a+1
            c = math.sqrt(a*a + b*b)
            if(a+b+c>n):
                print('No Pythagorean Triplet Found')
                done = True
        if(c.is_integer()):
            if(a+b+c == n):
                print('a = ',a)
                print('b = ',b)
                print('c = ',c)
                done = True

findPythagoreanTriplet(1000)
