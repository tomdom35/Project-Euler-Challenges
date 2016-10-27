import time

def print_known(known):
    for i in range(len(known)):
        print(i+1,"has",len(known[i]),"combos")
        for combo in known[i]:
            print(combo)
        print()

def print_known_combos(known,i):
    print(i,"has",len(known[i-1]),"combos")
    for combo in known[i-1]:
        print(combo)
    print()

def print_known_num_combos(known,i):
     print(i,"has",len(known[i-1]),"combos")

def div(root, coins, cur_coins, combos, known):
    new_coins = cur_coins[:]
    if root == 0:
        new_coins = sorted(new_coins)
        if new_coins not in combos:
            combos.append(new_coins)
    else:
        for coin in coins:
            if root < coin:
                break
            new_root = root - coin
            new_coins.append(coin)
            if(new_root > 0 and new_root <= len(known)):
                prev = known[new_root-1]
                for combo in prev:
                    temp_coins = new_coins[:]
                    temp_coins.extend(combo)
                    temp_coins = sorted(temp_coins)
                    if temp_coins not in combos:
                        combos.append(temp_coins)
            else:
                div(new_root,coins, new_coins, combos, known)
            new_coins.pop()
    return combos

c = [1,2,5,10,20,50,100,200]
r = int(input("Enter a number:"))
known = []
start = time.time()

for i in range(1,r+1):
    known.append(div(i,c,[],[],known))

#print_known(known)
#print_known_combos(known,r)
print_known_num_combos(known,i)
end = time.time()
print(end-start)

