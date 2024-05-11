from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    cross_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games_as_cross', null=True, blank=True)
    nought_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games_as_nought', null=True, blank=True)
    whose_move = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_move', null=True, blank=True)
    moves = models.CharField(max_length=9, default='123456789')
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner', null=True, blank=True)

    def make_move(self, position, symbol):
        winner_pos = [[0, 1, 2], [3, 4, 5], [6,7, 8], 
        [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]

        moves_list = list(self.moves)
        if moves_list[int(position) - 1] != 'x' and moves_list[int(position) - 1] != 'o':
            moves_list[int(position) - 1] = symbol
        self.moves = ''.join(moves_list)
        
        for pos in winner_pos:
            kol_x, kol_o = 0, 0
            for x in pos:
                if moves_list[x] == 'x':
                    kol_x += 1
                if moves_list[x] == 'o':
                    kol_o += 1
            if kol_x == 3:
                self.winner = self.cross_id
            if kol_o == 3:
                self.winner = self.nought_id 
        
        if self.whose_move == self.cross_id:
            self.whose_move = self.nought_id
        else:
            self.whose_move = self.cross_id

        self.save()

    def get_board(self):
        return [
            [self.moves[0], self.moves[1], self.moves[2]],
            [self.moves[3], self.moves[4], self.moves[5]],
            [self.moves[6], self.moves[7], self.moves[8]],
        ]