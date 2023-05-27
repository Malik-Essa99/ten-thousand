import random

class GameLogic:
    def __init__(self) -> None:
        self.rolls = ()
        self.total_score = 0
        self.round_number = 1
        self.dice_remaining = 0
        self.cheat = False
        self.hot_dice = False
        self.total_unbanked =0
        self.unbanked_points =0
        self.dice= ()
        self.keepers = ()
        self.check_dice =[]

    @staticmethod
    def get_scorers(dice):
        # dice= tuple(dice)
        all_dice_score = GameLogic.calculate_score(dice)
        if all_dice_score == 0:
            return tuple()
        scorers = []
        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i+1:]
            sub_score = GameLogic.calculate_score(sub_roll)
            if sub_score != all_dice_score:
                scorers.append(val)
        return tuple(scorers)
    
    def welcome_msg(self):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        self.user_input = input("> ")
        if self.user_input.lower() != "y":
            print("OK. Maybe another time")
            return "n"
    
    def play_game(self):
        self.rolls = ()
        self.total_score = 0
        self.round_number = 1
        self.dice_remaining = 6
        self.total_unbanked = 0
        self.cheat = False
        self.hot_dice = False
        # rolls = [(2, 2, 4, 6, 3, 3)]  # Losing roll
        # self.rolls = [(2, 2, 4, 4, 3, 3)]  # Losing roll
        # rolls = [(3, 2, 5, 4, 3, 3), (5, 2, 3, 2, 1, 4),(6 ,6 ,5 ,4, 2 ,1)]  # bank_first_for_two_rounds.sim
        # rolls = [(4, 2, 6, 4, 6, 5), (6,4, 5 ,2 ,3 ,1)]  # bank_one_roll_then_quit.sim
        # rolls = [(4, 4, 5, 2, 3, 1)]  # one_and_done.sim

        # Lab 08 Tests

        # rolls = [(5 ,2 ,3 ,5 ,4 ,2)]  # cheat_and_fix.sim
        # rolls = [(2 ,3 ,1 ,3 ,1 ,2) ,(4 ,1 ,4 ,4 ,3 ,4),(3 ,2 ,3 ,2 ,1 ,4)]  # hot_dice.sim
        # rolls = [(2 ,3 ,1 ,3 ,4 ,2) ,(4 ,2 ,4 ,4 ,6),(3 ,2 ,3 ,2 ,1 ,4)]  # repeat_roller.sim

        if self.welcome_msg() == "n":
            return

        while True:
            if self.hot_dice == False:
                print(f"Starting round {self.round_number}")
                self.total_unbanked = 0

            self.unbanked_points = 0
            self.dice_remaining = 6
            
            if self.rolls:
                print("Rolling 6 dice...")
                self.dice = list(self.rolls.pop(0))
            else:
                print("Rolling 6 dice...")
                self.dice = self.roll_dice(6)

            if self.is_zilch(self.dice):
                self.dice_remaining = 0
                self.round_number += 1

            while self.dice_remaining != 0:
                self.cheat = False
                self.hot_dice = False

                
                roll_str = " ".join(str(num) for num in self.dice)
                                    
                print(f"*** {roll_str} ***")

                if self.is_zilch(self.dice):
                    self.dice_remaining = 0
                    self.round_number += 1
                    continue

                print("Enter dice to keep, or (q)uit:")
                self.user_input = input("> ")

                if self.user_input.lower() == "q" or self.round_number > 19:
                    print(f"Thanks for playing. You earned {self.total_score} points")
                    return self.total_score
                
                
                self.check_dice = list(self.dice)
                self.keepers = [int(digit) for digit in str(self.user_input)]
                self.cheat = self.validate_keepers(self.check_dice, self.keepers)

                if len(self.keepers) > self.dice_remaining:
                    self.cheat = True
                

                if self.cheat:
                    print("Cheater!!! Or possibly made a typo...")
                    continue
                # if user_input is not the roll dice Cheater detected

                self.keepers = [int(die) for die in self.user_input if die.isdigit()]
                self.unbanked_points = self.calculate_score(self.keepers)
                if self.unbanked_points == 0:
                    print("Round Ended, Your Score this round is 0")
                    self.round_number += 1
                    break
                self.total_unbanked += self.unbanked_points
                self.unbanked_points = 0

                self.dice_remaining = self.dice_remaining - len(self.keepers)

                if self.dice_remaining == 0 and len(self.keepers) ==  len(GameLogic.get_scorers(self.keepers)):
                    self.hot_dice = True
                    self.check_dice = 6
                    self.dice_remaining = 6

                if self.hot_dice == True:
                    print(f"You have {self.total_unbanked} unbanked points and 6 dice remaining")
                else:
                    print(f"You have {self.total_unbanked} unbanked points and {self.dice_remaining} dice remaining")

                print("(r)oll again, (b)ank your points or (q)uit:")
                self.user_input = input("> ")

                if self.user_input.lower() == "b":
                    self.total_score += self.total_unbanked
                    print(f"You banked {self.total_unbanked} points in round {self.round_number}")
                    print(f"Total score is {self.total_score} points")
                    self.round_number += 1
                    self.total_unbanked = 0
                    break
                elif self.user_input.lower() == "q":
                    print(f"Thanks for playing. You earned {self.total_score} points")
                    return self.total_score
                elif self.user_input.lower() == "r" and self.dice_remaining > 0:
                    print(f"Rolling {self.dice_remaining} dice...")
                    # if self.rolls:
                    #     self.dice = list(self.rolls.pop(0))
                    # else:
                    self.dice = self.roll_dice(self.dice_remaining)
                elif self.user_input.lower() == "r" and self.dice_remaining == 0:
                    print("You have 0 dices remaining, banking and moving to the next round")
                    self.total_score += self.total_unbanked
                    print(f"You banked {self.total_unbanked} points in round {self.round_number}")
                    print(f"Total score is {self.total_score} points")
                    self.round_number += 1
                    self.total_unbanked = 0
                else:
                    print("You can only enter, (r) (b) or (q)")
                    continue
                    


    @staticmethod
    def calculate_score(dice):
        num_count = 0
        three_pairs = False
        score = 0
        counts = [0] * 7

        for value in dice:
            counts[value] += 1

        for element in counts:
            if element == 2:
                num_count += 1
                if num_count == 3:
                    three_pairs = True

        scores_map = {
            (1, 1, 1, 1): 2000,
            (1, 1, 1, 1, 1): 3000,
            (1, 1, 1, 1, 1, 1): 4000,
            (5, 5, 5, 5): 1000,
            (5, 5, 5, 5, 5): 1500,
            (5, 5, 5, 5, 5, 5): 2000,
            (1, 2, 3, 4, 5, 6): 1500,
        }

        if tuple(sorted(dice)) in scores_map:
            score = scores_map[tuple(sorted(dice))]

        elif three_pairs == True:
            score = 1500
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
        return score

    @staticmethod
    def roll_dice(num_dice):
        return [random.randint(1, 6) for _ in range(num_dice)]
    
    
    def validate_keepers(self,check_dice, keepers):
        check_dice_lst = list(check_dice)
        for i in keepers:
            if i not in check_dice_lst:
                self.cheat = True
                return self.cheat
            else:
                self.cheat = False
                check_dice_lst.remove(i)
        return self.cheat

    def is_zilch(self,test_dice):
        if self.calculate_score(test_dice) == 0:
            print('''
****************************************
**        Zilch!!! Round over         **
****************************************
                ''')
            return True

if __name__ == "__main__":
    game1 = GameLogic()
    game1.play_game()
