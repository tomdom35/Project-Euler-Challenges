f = open("input.txt")
num_tree = []
for line in f:
    temp_list = list(map(int,line.split()))
    num_tree.append(temp_list)

for i in range(len(num_tree)-1):
    cur_index = (len(num_tree)-2) - i
    for j in range(len(num_tree[cur_index])):
        left = num_tree[cur_index+1][j]
        left_sum = (num_tree[cur_index][j]) + (left)
        right = num_tree[cur_index+1][j+1]
        right_sum = (num_tree[cur_index][j]) + (right)
        num_sum = max(right_sum, left_sum)
        num_tree[cur_index][j] = num_sum

print(num_tree[0][0])
