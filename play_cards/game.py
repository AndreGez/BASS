import numpy as np

from card import Card
from playerRandom import PlayerRandom
from table import Table

class Game:
    table: Table
    players: list
    cardsPerPlayer: int

    def __init__(self, players, cardsPerPlayer = 6, seed = None):
        if seed is not None:
            np.random.seed(seed)

        self.players = players
        self.cardsPerPlayer = cardsPerPlayer
        self.table = Table()
        
        for p in self.players:
            p.SetTrump(self.table.trump)
            p.SetTable(self.table)

    def Deal(self):
        for player in self.players:
            player.AcceptCards(self.table.DrawNextCards(self.cardsPerPlayer))

    def FillCards(self):
        for player in self.players:
            player.AcceptCards(self.table.DrawNextCards(max(0, self.cardsPerPlayer - len(player.hand))))

    def PrintHandCards(self):
        for p in self.players:
            print(p.name)
            print(p.hand)

    def PrintTable(self):
        print('Table: ')
        print(self.table.attacking)

    def GameOver(self):
        for p in self.players:
            if len(p.hand) == 0:
                print(f"{p.name} has won the game!")
                return True
        return False

    def PlayGame(self):
        self.Deal()
        
        print('TRUMP: ' + self.table.trump.name)

        player_idx = 0
        i = 0
        game_over = False
        while not game_over:
            self.FillCards()
            print(f"\nNew round {i + 1}\n")
            self.PrintHandCards()

            attacking_player = self.players[player_idx]
            defending_player = self.players[(player_idx + 1) % len(self.players)]
            print(f"{attacking_player.name} is attacking, {defending_player.name} is defending")
            
            while True:
                tbl_state = self.table.attacking.copy()
                attacking_player.Attack()
                if self.GameOver():
                    game_over = True
                    break
                defending_player.Defend()
                self.PrintTable()
                if self.GameOver():
                    game_over = True
                    break
                if len(self.table.attacking) == 0:
                    print(f"Table is empty, {defending_player.name} hat geschluckt")
                    break
                if self.table.attacking == tbl_state:
                    player_idx = (player_idx + 1) % len(self.players)
                    print("No one attacked, next player is attacking")
                    break
                
            
            self.table.DiscardCards()
            i += 1
            if i == -1:
                break
            

