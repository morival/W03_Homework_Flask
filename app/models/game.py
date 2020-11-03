from app.models.player import *

class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def player_move(self, result):
        if result == "rock":
            return 0
        elif result == "paper":
            return 1
        elif result == "scissors":
            return 2
            
    def print_winner(self, winning_player):
        return f"{winning_player.name} wins by playing {winning_player.choice}!"

    def tie(self):
        return "Tie Game!"


    def clip_path(self, player):
        clip_table = ["7% 67% 27% 0%", "24% 33.55% 10% 34%", "7% 2% 27% 65%" ]
        cp = clip_table[self.player_move(player.choice)]
        return cp

    def margin_left(self, player):
        ml_table = ["-4px", "-248px", "-500px"]
        ml = ml_table[self.player_move(player.choice)]
        return ml

    def margin_top(self, player):
        mt_table = ["-13px", "-70px", "-13px"]
        mt = mt_table[self.player_move(player.choice)]
        return mt
        
        
    def play_new_game(self, player1, player2):
        
        # game_map = {0:"rock", 1:"paper", 2:"scissors"}
        rps_table = [[None, 1, 0], [1, None, 2],[0, 2, None]]
        winner = rps_table[self.player_move(player1.choice)][self.player_move(player2.choice)]

        if winner == self.player_move(player1.choice):
            return self.print_winner(player1)
        elif winner == self.player_move(player2.choice):
            return self.print_winner(player2)
        else:
            return self.tie()

    def select_icon(self, player):
        player.choice
        return "header > h1 {color: hotpink;}"

    
