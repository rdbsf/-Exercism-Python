# Score categories
# Change the values as you see fit
YACHT = 'YACHT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):

    matches = [0,0,0,0,0,0]
    for x in dice:
        index = x - 1
        matches[index] += 1 
            
    if category == YACHT and 5 in matches:
        return 50
    elif category == CHOICE or (category == FULL_HOUSE and 2 in matches and 3 in matches):
        return sum(dice)   
    elif category == FOUR_OF_A_KIND and 4 in matches:
        return (matches.index(4) + 1) * 4
    elif category == FOUR_OF_A_KIND and 5 in matches:
        return (matches.index(5) + 1) * 4
    elif category == LITTLE_STRAIGHT and matches[0]==1 and matches[1]==1 and matches[2]==1 and matches[3]==1 and matches[4]==1:
        return 30
    elif category == BIG_STRAIGHT and matches[1]==1 and matches[2]==1 and matches[3]==1 and matches[4]==1 and matches[5]==1:
        return 30
    elif category in [1,2,3,4,5,6]:
        return matches[category-1] * category  
    else:
        return 0
