import random

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        score = 0
        counts = [0] * 7  # Initialize counts for each dice value

        for value in dice:
            counts[value] += 1

        scores_map = {
            (1,2,3,4,5,6) : 1500, # Straight
            (1, 1, 1, 1, 1, 1): 4000,  # Six ones
            (1,1,1,1): 2000,
            (2, 2, 2, 2): 400,  # Four of a kind of 2s
            (3, 3, 3, 3): 600,  # Four of a kind of 3s
            (4, 4, 4, 4): 800,  # Four of a kind of 4s
            (5, 5, 5, 5): 1000,  # Four of a kind of 5s
            (6, 6, 6, 6): 1200,  # Four of a kind of 6s
            (2, 2, 2, 2, 2): 600,  # Five of a kind of 2s
            (3, 3, 3, 3, 3): 900,  # Five of a kind of 3s
            (4, 4, 4, 4, 4): 1200,  # Five of a kind of 4s
            (5, 5, 5, 5, 5): 1500,  # Five of a kind of 5s
            (6, 6, 6, 6, 6): 1800,  # Five of a kind of 6s
            (2, 2, 2, 2, 2, 2): 800,  # Six of a kind of 2s
            (3, 3, 3, 3, 3, 3): 1200,  # Six of a kind of 3s
            (4, 4, 4, 4, 4, 4): 1600,  # Six of a kind of 4s
            (5, 5, 5, 5, 5, 5): 2000,  # Six of a kind of 5s
            (6, 6, 6, 6, 6, 6): 2400,  # Six of a kind of 6s
        }

        # Check if the roll combination exists in the scores map
        if tuple(sorted(dice)) in scores_map:
            score = scores_map[tuple(sorted(dice))]
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
        return score
    
    @staticmethod
    def roll_dice(num_dice):
        return [random.randint(1, 6) for _ in range(num_dice)]
    

if __name__ == "__main__":
    game_logic = GameLogic()
    print(game_logic.calculate_score(game_logic.roll_dice(6)))