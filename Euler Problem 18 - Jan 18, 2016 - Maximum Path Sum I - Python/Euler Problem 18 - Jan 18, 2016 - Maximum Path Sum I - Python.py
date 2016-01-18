layers = []
with open('input.txt') as file:
    for line in file:
        layers.append(line.rstrip().split())

for layer in layers:
    print(layer)

layer = 0
index = 0
total = 0

def maxSum(layers):
    total = 0
    index = 0
    for i in range(0,len(layers)):
        print(i,index)
        total+=int(layers[i][index])
        if(not i==len(layers)-1):
            if(int(layers[i+1][index])<int(layers[i+1][index+1])):
                index+=1
    return total

print(maxSum(layers))
