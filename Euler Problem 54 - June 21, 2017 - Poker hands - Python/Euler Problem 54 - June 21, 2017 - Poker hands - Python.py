def get_face_card(val):
    if val == 10:
        c = 'T'
    if val == 11:
        c = 'J'
    if val == 12:
        c = 'Q'
    if val == 13:
        c = 'K'
    if val == 14:
        c = 'A'
    return c

def get_face_card_value(x):
    cards = ['T','J','Q','K','A']
    return str(cards.index(x) + 10)

def is_face_card(x):
    cards = ['T','J','Q','K','A']
    return x in cards
    
def royal_flush(hand):
    if(not flush(hand)):
        return False
    
    t = 'T' in hand
    j = 'J' in hand
    q = 'Q' in hand
    k = 'K' in hand
    a = 'A' in hand
    
    return t and j and q and k and a

def compare_royal_flush(p1_hand, p2_hand):
    if(royal_flush(p1_hand)):
        if(royal_flush(p2_hand)):
            return 0
        else:
            return 1
    elif(royal_flush(p2_hand)):
        return 2
    else:
        return 0

def straight_flush(hand):
    return flush(hand) and straight(hand)

def compare_straight_flush(p1_hand, p2_hand):
    if(straight_flush(p1_hand)):
        if(straight_flush(p2_hand)):
            return compare_high_card(p1_hand, p2_hand)
        else:
            return 1
    elif(straight_flush(p2_hand)):
         return 2
    else:
         return 0


def flush(hand):
    s = hand[1]
    for i in range(0,5):
        index = (3*i) + 1
        if(hand[index] != s):
            return False
    return True

def compare_flush(p1_hand, p2_hand):
    if(flush(p1_hand)):
        if(flush(p2_hand)):
            return compare_high_card(p1_hand, p2_hand)
        else:
            return 1
    elif(flush(p2_hand)):
         return 2
    else:
         return 0

def straight(hand):
    nums = []
    done = False
    x = ['T','J','Q','K','A']
    
    for i in range(0,5):
        index = 3*i
        value = hand[index]
        if is_face_card(value):
            value = get_face_card_value(value)
        nums.append(value)
        
    nums = sorted(nums)
    old_num = int(nums[0])
    
    for i in range(1,5):
        new_num = int(nums[i])
        if(new_num != old_num+1):
            return False
        old_num = new_num
        
    return True

def compare_straight(p1_hand, p2_hand):
    if(straight(p1_hand)):
        if(straight(p2_hand)):
            return compare_high_card(p1_hand, p2_hand)
        else:
            return 1
    elif(straight(p2_hand)):
        return 2
    else:
         return 0

def x_of_a_kind(hand,x,y):
    nums = []
    r = int(len(hand)/3)
    for i in range(r):
        num = hand[i*3]
        nums.append(num)
        
    for i in range(r + 1 - x):
        index = i*3
        val = hand[index]
        if nums.count(val) == x and val != y:
            if(is_face_card(val)):
                return get_face_card_value(val)
            return val
    return 0

def compare_x_of_a_kind(p1_hand, p2_hand, x):
    p1 = int(x_of_a_kind(p1_hand,x,0))
    p2 = int(x_of_a_kind(p2_hand,x,0))
    if(p1 > 0):
        if(p2 > 0):
            if(p1 > p2):
                return 1
            elif(p2 > p1):
                return 2
            else:
                if(p1>9):
                    p1 = get_face_card(p1)
                if(p2>9):
                    p2 = get_face_card(p2)
                p1h = get_excluded_hand(p1_hand, str(p1))
                p2h = get_excluded_hand(p2_hand, str(p2))
                return compare_high_card(p1h, p2h)
        else:
            return 1
    elif(p2 > 0):
        return 2
    else:
        return 0

def full_house(hand):
    three = x_of_a_kind(hand,3,0)
    two = x_of_a_kind(hand,2,three)
    return three != 0 and two != 0

def compare_full_house(p1_hand, p2_hand):
    if(full_house(p1_hand)):
        if(full_house(p2_hand)):
            three = compare_x_of_a_kind(p1_hand, p2_hand,3)
            if(three != 0):
                return three
            else:
                return compare_x_of_a_kind(p1_hand, p2_hand,2)
        else:
            return 1
    elif(full_house(p2_hand)):
        return 2
    else:
        return 0

def two_pairs(hand):
    x = x_of_a_kind(hand,2,0)
    y = x_of_a_kind(hand,2,x)
    return x != 0 and y != 0

def compare_two_pairs(p1_hand, p2_hand):
    p1 = int(x_of_a_kind(p1_hand,2,0))
    p2 = int(x_of_a_kind(p2_hand,2,0))
    if(p1 > 0):
        if(p2 > 0):
            if(p1>9):
                p1 = get_face_card(p1)
            if(p2>9):
                p2 = get_face_card(p2)
            p1h = get_excluded_hand(p1_hand, str(p1))
            p2h = get_excluded_hand(p2_hand, str(p2))
            return compare_x_of_a_kind(p1h, p2h, 2)
        else:
            return 1
    elif(p2 > 0):
        return 2
    else:
        return 0

def high_card(hand):
    high = 0
    r = int(len(hand)/3)
    for i in range(0,r):
        index = 3*i
        value = hand[index]
        if is_face_card(value):
            value = get_face_card_value(value)
        value = int(value)
        high = max(high,value)
        
    return high

def compare_high_card(p1_hand, p2_hand):
    if(high_card(p1_hand) > high_card(p2_hand)):
        return 1
    elif(high_card(p1_hand) < high_card(p2_hand)):
        return 2
    else:
        return 0


def get_excluded_hand(hand, exclusion):
    new_hand = ''
    r = int(len(hand)/3)
    for i in range(r):
        index = i*3
        val = hand[index]
        if(val != exclusion):
            val = hand[index:index+3]
            new_hand += val
    return new_hand
        

def simulate(p1_hand, p2_hand):
    winner = compare_royal_flush(p1_hand, p2_hand)
    
    if(winner == 0):
        winner = compare_straight_flush(p1_hand, p2_hand)

    if(winner == 0):
        winner = compare_x_of_a_kind(p1_hand, p2_hand,4)

    if(winner == 0):
        winner = compare_full_house(p1_hand, p2_hand)

    if(winner == 0):
        winner = compare_flush(p1_hand, p2_hand)

    if(winner == 0):
        winner = compare_straight(p1_hand, p2_hand)

    if(winner == 0):
        winner = compare_x_of_a_kind(p1_hand, p2_hand,3)

    if(winner == 0):
        winner = compare_two_pairs(p1_hand, p2_hand)

    if(winner == 0):
        winner = compare_x_of_a_kind(p1_hand, p2_hand,2)

    if(winner == 0):
        winner = compare_high_card(p1_hand, p2_hand)

    return winner   

'''
p1 = '4D 6S 9H QH QC '
p2 = '3D 6D 7H QD QS '

print(simulate(p1,p2))
'''
'''
print(compare_high_card(p1,p2))
print(compare_x_of_a_kind(p1,p2,4))
print(compare_x_of_a_kind(p1,p2,3))
print(compare_x_of_a_kind(p1,p2,2))
print(compare_straight(p1,p2))
print(compare_flush(p1,p2))
print(compare_straight_flush(p1,p2))
print(compare_royal_flush(p1,p2))
print(compare_full_house(p1,p2))
print(compare_two_pairs(p1,p2))
'''


with open('Euler Problem 54 Input.txt') as f:
    hands = f.readlines()

player_1_hands = []
player_2_hands = []
wins = 0
desired_winner = 1

for hand in hands:
    player_1_hands.append(hand[0:15])
    player_2_hands.append(hand[15:len(hand)])

for i in range(len(player_1_hands)):
    p1_hand = player_1_hands[i]
    p2_hand = player_2_hands[i]

    if simulate(p1_hand,p2_hand) == desired_winner:
        wins += 1

print(wins)
