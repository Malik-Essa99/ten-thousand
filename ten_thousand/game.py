from ten_thousand.game_logic import GameLogic

class Game(GameLogic):
    def play(self):
        GameLogic().play_game()

if __name__ == "__main__":
    Game.play()