from game import Game
from playerRandom import PlayerRandom

if __name__ == '__main__':
    game = Game([PlayerRandom('Andre'), PlayerRandom('Clemens')])
    game.PlayGame()