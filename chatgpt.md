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

     Check for a straight (1, 2, 3, 4, 5, 6)
    if set(dice) == set([1, 2, 3, 4, 5, 6]):
        score += 1500
        return score

     Check for three pairs
    if len(set(dice)) == 3 and all(dice.count(x) == 2 for x in set(dice)):
        score += 1500
        return score

     Check for individual 1s and 5s
    for die in dice:
        if die == 1:
            score += 100
        elif die == 5:
            score += 50

     Check for triples (3 of a kind)
    triplets = set([x for x in dice if dice.count(x) >= 3])
    for triplet in triplets:
        if triplet == 1:
            score += 1000
        else:
            score += triplet * 100

     Check for single 1 or 5
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

################################################################################

## Version_2


## command:
+ create a function that will return tthis output when given these inputs using this code  but the function has to be outside the class


Welcome to Ten Thousand
(y)es to play or (n)o to decline
> y
Starting round 1
Rolling 6 dice...
*** 3 2 5 4 3 3 ***
Enter dice to keep, or (q)uit:
> 3335
You have 350 unbanked points and 2 dice remaining
(r)oll again, (b)ank your points or (q)uit:
> b
You banked 350 points in round 1
Total score is 350 points
Starting round 2
Rolling 6 dice...
*** 5 2 3 2 1 4 ***
Enter dice to keep, or (q)uit:
> 15
You have 150 unbanked points and 4 dice remaining
(r)oll again, (b)ank your points or (q)uit:
> b
You banked 150 points in round 2
Total score is 500 points
Starting round 3
Rolling 6 dice...
*** 6 6 5 4 2 1 ***
Enter dice to keep, or (q)uit:
> q
Thanks for playing. You earned 500 points
create a function that will return tthis output when given these inputs using this code import random

class GameLogic:

    @staticmethod
    def calculate_score(dice):
        num_count = 0
        three_pairs = False
        score = 0
        counts = [0] * 7  # Initialize counts for each dice value

        for value in dice:
            counts[value] += 1
            
        for element in counts:
            if element == 2:
                num_count += 1
                if num_count == 3:
                    three_pairs = True

        scores_map = {
            (1, 1, 1, 1): 2000, # Four of a kind of 1s
            (2, 2, 2, 2): 400,  # Four of a kind of 2s
            (3, 3, 3, 3): 600,  # Four of a kind of 3s
            (4, 4, 4, 4): 800,  # Four of a kind of 4s
            (5, 5, 5, 5): 1000, # Four of a kind of 5s
            (6, 6, 6, 6): 1200, # Four of a kind of 6s
            (1, 1, 1, 1, 1): 3000,  # Five of a kind of 1s
            (2, 2, 2, 2, 2): 600,   # Five of a kind of 2s
            (3, 3, 3, 3, 3): 900,   # Five of a kind of 3s
            (4, 4, 4, 4, 4): 1200,  # Five of a kind of 4s
            (5, 5, 5, 5, 5): 1500,  # Five of a kind of 5s
            (6, 6, 6, 6, 6): 1800,  # Five of a kind of 6s
            (1, 1, 1, 1, 1, 1): 4000,  # Six of a kind of 2s
            (2, 2, 2, 2, 2, 2): 800,   # Six of a kind of 2s
            (3, 3, 3, 3, 3, 3): 1200,  # Six of a kind of 3s
            (4, 4, 4, 4, 4, 4): 1600,  # Six of a kind of 4s
            (5, 5, 5, 5, 5, 5): 2000,  # Six of a kind of 5s
            (6, 6, 6, 6, 6, 6): 2400,  # Six of a kind of 6s
            (1, 2, 3, 4, 5, 6): 1500,  # Straight
        }

        # Check if the roll combination exists in the scores map
        if tuple(sorted(dice)) in scores_map:
            print (dice, "from Score")
            score = scores_map[tuple(sorted(dice))]
        elif three_pairs == True:
            score = 1500
            print (dice, "Three pairs")
            return score
        else:
            score += counts[1] // 3 * 1000
            counts[1] %= 3

            score += counts[5] // 3 * 500
            counts[5] %= 3

            score += counts[1] * 100
            score += counts[5] * 50
            score += counts[5] // 3 * 50 * 2

            for value in range(2, 7):
                if counts[value] >= 3:
                    score += value * 100
                    counts[value] -= 3
        print (dice, "Calculated")
        return score
    
    @staticmethod
    def roll_dice(num_dice):
        return [random.randint(1, 6) for _ in range(num_dice)]
## Output

+ def play_ten_thousand():
    game_logic = GameLogic()
    total_score = 0
    round_number = 1

    while True:
        print("Starting round", round_number)
        print("Rolling 6 dice...")
        dice = game_logic.roll_dice(6)
        print("*", *dice, "**")

        print("Enter dice to keep, or (q)uit:")
        user_input = input("> ")
        if user_input.lower() == 'q':
            print("Thanks for playing. You earned", total_score, "points")
            return total_score

        dice_to_keep = [int(die) for die in user_input if die.isdigit()]
        unbanked_points = game_logic.calculate_score(dice_to_keep)
        dice_remaining = 6 - len(dice_to_keep)

        print("You have", unbanked_points, "unbanked points and", dice_remaining, "dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_input = input("> ")

        if user_input.lower() == 'b':
            total_score += unbanked_points
            print("You banked", unbanked_points, "points in round", round_number)
            print("Total score is", total_score, "points")
            round_number += 1
        elif user_input.lower() == 'q':
            print("Thanks for playing. You earned", total_score, "points")
            return total_score


 Test the function
play_ten_thousand()

## We made changes to the overall code and how it functions