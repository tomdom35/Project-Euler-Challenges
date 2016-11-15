def find_word_value(word):
    alpha_vals = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    total = 0
    for letter in word:
        total += alpha_vals.index(letter)
    return total

def get_triangular_numbers(x):
    nums = [0]
    total = 0
    n = 1
    while total < x:
        total = int(0.5*n*(n+1))
        nums.append(total)
        n += 1
    return nums

with open('words.txt', 'r') as myfile:
    words = myfile.read().split(',')

max_word_value = 0
word_values = []

for i in range(len(words)):
    words[i] = words[i][1:-1]
    word_value = find_word_value(words[i])
    word_values.append(word_value)
    if word_value > max_word_value:
        max_word_value = word_value

triangular_numbers = get_triangular_numbers(max_word_value)

count = 0
for val in word_values:
    if val in triangular_numbers:
        count+=1

print(count)



