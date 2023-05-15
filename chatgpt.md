create a class  GameLogic: that has a function  roll_dice() 
+ import random

class GameLogic:
    def roll_dice(self):
        return random.randint(1, 6)


create a function  roll_dice()
+ import random

def roll_dice():
    return random.randint(1, 6)

create function calculate_score that will return score according to the ten thousand game rules
+ def calculate_score(dice):
    score = 0

    # Check for a straight (1, 2, 3, 4, 5, 6)
    if set(dice) == set([1, 2, 3, 4, 5, 6]):
        score += 1500
        return score

    # Check for three pairs
    if len(set(dice)) == 3 and all(dice.count(x) == 2 for x in set(dice)):
        score += 1500
        return score

    # Check for individual 1s and 5s
    for die in dice:
        if die == 1:
            score += 100
        elif die == 5:
            score += 50

    # Check for triples (3 of a kind)
    triplets = set([x for x in dice if dice.count(x) >= 3])
    for triplet in triplets:
        if triplet == 1:
            score += 1000
        else:
            score += triplet * 100

    # Check for single 1 or 5
    singles = set([x for x in dice if dice.count(x) < 3])
    for single in singles:
        if single == 1:
            score += 100
        elif single == 5:
            score += 50

    return score
modify the code so that it stores the possible dice rolls in in a tuple and their results 
+ def calculate_score(dice):
    scores = (
        ((1, 1, 1), 1000),  # Three 1s
        ((6, 6, 6), 600),  # Three 6s
        ((5, 5, 5), 500),  # Three 5s
        ((4, 4, 4), 400),  # Three 4s
        ((3, 3, 3), 300),  # Three 3s
        ((2, 2, 2), 200),  # Three 2s
        ((1, ), 100),      # Single 1
        ((5, ), 50)        # Single 5
    )

    score = 0

    for roll, points in scores:
        count = dice.count(roll[0])
        while count >= len(roll):
            score += points
            count -= len(roll)

    return score


we tried to solve the strech goal so we gave chat gpt many commands but non of them worked
like :
can you include every possibility in the tuple ?
+ def calculate_score(dice):
    scores = (
        ((1, 1, 1), 1000),  # Three 1s
        ((2, 2, 2), 200),   # Three 2s
        ((3, 3, 3), 300),   # Three 3s
        ((4, 4, 4), 400),   # Three 4s
        ((5, 5, 5), 500),   # Three 5s
        ((6, 6, 6), 600),   # Three 6s
        ((1, ), 100),       # Single 1
        ((5, ), 50),        # Single 5
        ((1, 2, 3, 4, 5, 6), 1500)  # Straight
    )

    score = 0

    for roll, points in scores:
        count = dice.count(roll[0])
        while count >= len(roll):
            score += points
            count -= len(roll)

    return score

can you make it pass the six ones, three pairs, six of a kind, and 5 of a kind
+ def calculate_score(dice):
    scores = (
        ((1, 1, 1, 1, 1, 1), 4000),  # Six 1s
        ((2, 2, 2, 2, 2, 2), 3200),  # Six 2s
        ((3, 3, 3, 3, 3, 3), 2400),  # Six 3s
        ((4, 4, 4, 4, 4, 4), 1600),  # Six 4s
        ((5, 5, 5, 5, 5, 5), 2000),  # Six 5s
        ((6, 6, 6, 6, 6, 6), 2400),  # Six 6s
        ((1, 1, 1, 2, 2, 2), 1500),  # Three pairs
        ((1, 1, 1), 1000),           # Three 1s
        ((2, 2, 2), 200),            # Three 2s
        ((3, 3, 3), 300),            # Three 3s
        ((4, 4, 4), 400),            # Three 4s
        ((5, 5, 5), 500),            # Three 5s
        ((6, 6, 6), 600),            # Three 6s
        ((1, ), 100),                # Single 1
        ((5, ), 50)                  # Single 5
    )

    score = 0

    for roll, points in scores:
        count = dice.count(roll[0])
        while count >= len(roll):
            score += points
            count -= len(roll)

    return score

    
We made edits on the code so that it covers all the tests in the test file