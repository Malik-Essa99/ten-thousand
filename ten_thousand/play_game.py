from game_logic import GameLogic

if __name__ == "__main__":    
    def play_ten_thousand():
        game_logic = GameLogic()
        total_score = 0
        round_number = 1
        dice_remaining = 6
        total_unbanked = 0

        rolls = [(3, 2, 5, 4, 3, 3), (5, 2, 3, 2, 1, 4),(6 ,6 ,5 ,4, 2 ,1)]  # bank_first_for_two_rounds.sim
        # rolls = [(4, 2, 6, 4, 6, 5), (6,4, 5 ,2 ,3 ,1)]  # bank_one_roll_then_quit.sim
        # rolls = [(4, 4, 5, 2, 3, 1)]  # one_and_done.sim
        # rolls = [(2, 2, 4, 6, 3, 3)]  # Losing roll
        ### You can try quitting by typing q

        print("Welcome to Ten Thousand")
        user_input = input("(y)es to play or (n)o to decline\n> ")
        if user_input.lower() != 'y':
            print("OK. Maybe another time")
            return

        while True:
            print("Starting round", round_number)
            total_unbanked = 0
            unbanked_points = 0
            dice_remaining = 6
            if rolls:
                dice = list(rolls.pop(0))
            else:
                print("Rolling 6 dice...")
                dice = game_logic.roll_dice(6)

            while dice_remaining:
                print("***", *dice, "***")
                print("Enter dice to keep, or (q)uit:")
                user_input = input("> ")
                # if user_input is not the roll dice Cheater detected
                if user_input.lower() == 'q':
                    print("Thanks for playing. You earned", total_score, "points")
                    return total_score

                dice_to_keep = [int(die) for die in user_input if die.isdigit()]
                unbanked_points = game_logic.calculate_score(dice_to_keep)
                if unbanked_points == 0:
                    print("Round Ended, Your Score this round is 0")
                    round_number += 1
                    break
                total_unbanked += unbanked_points
                unbanked_points =0
                dice_remaining = dice_remaining - len(dice_to_keep)
                print("You have", total_unbanked, "unbanked points and", dice_remaining, "dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                user_input = input("> ")
                
                if user_input.lower() == 'b':
                    total_score +=  total_unbanked
                    print("You banked", total_unbanked, "points in round", round_number)
                    print("Total score is", total_score, "points")
                    round_number += 1
                    total_unbanked = 0
                    break
                elif user_input.lower() == 'q':
                    print("Thanks for playing. You earned", total_score, "points")
                    return total_score
                elif user_input.lower() == 'r' and dice_remaining > 0:
                    print(f"Rolling {dice_remaining} dice...")
                    dice = game_logic.roll_dice(dice_remaining)

    # Test the function
    play_ten_thousand()