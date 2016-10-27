names = []

f = open("input.txt")
for line in f:
    names = line.split(',')

for i in range(len(names)):
    names[i] = names[i][1:-1]

names.sort()
total = 0

for index, i in enumerate(names):
    score = 0
    for j in i:
        score += ord(j) - 64
    score *= index+1
    total += score

print(total)
        
