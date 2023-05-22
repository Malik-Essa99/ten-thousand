import random

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
            (1, 1, 1, 1): 2000,  # Four of a kind of 1s
            (1, 1, 1, 1, 1): 3000,  # Five of a kind of 1s
            (1, 1, 1, 1, 1, 1): 4000,  # Six of a kind of 2s
            (5, 5, 5, 5): 1000,
            (5, 5, 5, 5, 5): 1500,
            (5, 5, 5, 5, 5, 5): 2000,
            (1, 2, 3, 4, 5, 6): 1500,  # Straight
        }

        # Check if the roll combination exists in the scores map
        if tuple(sorted(dice)) in scores_map:
            # print(dice, "from Score")
            score = scores_map[tuple(sorted(dice))]

        elif three_pairs == True:
            score = 1500
            # print(dice, "Three pairs")
            return score
        else:
            score += counts[1] // 3 * 1000
            counts[1] %= 3

            score += counts[5] // 3 * 500
            counts[5] %= 3

            score += counts[1] * 100
            score += counts[5] * 50
            score += counts[5] // 3 * 50 * 2

        for i in range(2, 7):
            if i == 5:
                continue
            if counts[i] == 3:
                score += i * 100
            if counts[i] == 4:
                score += i * 2 * 100
            elif counts[i] == 5:
                score += i * 3 * 100
            elif counts[i] == 6:
                score += i * 4 * 100

        # print(dice, "Calculated")
        return score

    @staticmethod
    def roll_dice(num_dice):
        return [random.randint(1, 6) for _ in range(num_dice)]
    @staticmethod
    def validate_keepers(check_dice, keepers):
        check_dice_lst = list(check_dice)
        for i in keepers:
            if i not in check_dice_lst:
                cheat = True
                return cheat
            else:
                cheat = False
                check_dice_lst.remove(i)
        return cheat
    
    def is_zilch(self,test_dice):
        if self.calculate_score(test_dice) == 0:
            print('''
****************************************
**        Zilch!!! Round over         **
****************************************
                ''')
            return True


    def play(self):
        rolls = ()
        total_score = 0
        round_number = 1
        dice_remaining = 6
        total_unbanked = 0
        cheat = False
        hot_dice = False
        

        # rolls = [(2, 2, 4, 6, 3, 3)]  # Losing roll
        # rolls = [(3, 2, 5, 4, 3, 3), (5, 2, 3, 2, 1, 4),(6 ,6 ,5 ,4, 2 ,1)]  # bank_first_for_two_rounds.sim
        # rolls = [(4, 2, 6, 4, 6, 5), (6,4, 5 ,2 ,3 ,1)]  # bank_one_roll_then_quit.sim
        # rolls = [(4, 4, 5, 2, 3, 1)]  # one_and_done.sim

        # Lab 08 Tests

        rolls = [(5 ,2 ,3 ,5 ,4 ,2)]  # cheat_and_fix.sim
        # rolls = [(2 ,3 ,1 ,3 ,1 ,2) ,(4 ,1 ,4 ,4 ,3 ,4),(3 ,2 ,3 ,2 ,1 ,4)]  # hot_dice.sim
        # rolls = [(2 ,3 ,1 ,3 ,4 ,2) ,(4 ,2 ,4 ,4 ,6),(3 ,2 ,3 ,2 ,1 ,4)]  # repeat_roller.sim


        ### You can try quitting by typing q

        print("Welcome to Ten Thousand")
        user_input = input("(y)es to play or (n)o to decline\n> ")
        if user_input.lower() != "y":
            print("OK. Maybe another time")
            return

        while True:
            if hot_dice == False:
                print("Starting round", round_number)
                total_unbanked = 0

            unbanked_points = 0
            dice_remaining = 6
            if rolls:
                print("Rolling 6 dice...")
                dice = list(rolls.pop(0))
            else:
                print("Rolling 6 dice...")
                dice = self.roll_dice(6)

            if self.is_zilch(dice):
                dice_remaining = 0
                round_number += 1

            while dice_remaining != 0:
                cheat = False
                hot_dice = False

                print("***", *dice, "***")

                if self.is_zilch(dice):
                    dice_remaining = 0
                    round_number += 1
                    continue

                print("Enter dice to keep, or (q)uit:")
                user_input = input("> ")
                if user_input.lower() == "q":
                    print("Thanks for playing. You earned", total_score, "points")
                    return total_score
                
                
                check_dice = list(dice)
                keepers = [int(digit) for digit in str(user_input)]
                cheat = self.validate_keepers(check_dice, keepers)

                if len(keepers) > dice_remaining:
                    cheat = True
                

                if cheat:
                    print("Cheater!!! Or possibly made a typo...")
                    continue
                # if user_input is not the roll dice Cheater detected

                keepers = [int(die) for die in user_input if die.isdigit()]
                unbanked_points = self.calculate_score(keepers)
                if unbanked_points == 0:
                    print("Round Ended, Your Score this round is 0")
                    round_number += 1
                    break
                total_unbanked += unbanked_points
                unbanked_points = 0

                dice_remaining = dice_remaining - len(keepers)


                if 6 - len(keepers) == 0:
                    hot_dice = True


                if hot_dice == True:
                    print(
                        "You have",
                        total_unbanked,
                        "unbanked points and",
                        "6",
                        "dice remaining",
                    )
                else:
                    print(
                        "You have",
                        total_unbanked,
                        "unbanked points and",
                        dice_remaining,
                        "dice remaining",
                    )
                print("(r)oll again, (b)ank your points or (q)uit:")
                user_input = input("> ")

                if user_input.lower() == "b":
                    total_score += total_unbanked
                    print("You banked", total_unbanked, "points in round", round_number)
                    print("Total score is", total_score, "points")
                    if hot_dice == False:
                        round_number += 1
                        total_unbanked = 0
                    break
                elif user_input.lower() == "q":
                    print("Thanks for playing. You earned", total_score, "points")
                    return total_score
                elif user_input.lower() == "r" and dice_remaining > 0:
                    print(f"Rolling {dice_remaining} dice...")
                    if rolls:
                        dice = list(rolls.pop(0))
                    else:
                        dice = self.roll_dice(dice_remaining)


if __name__ == "__main__":
    game1 = GameLogic()
    game1.play()
