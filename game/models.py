from django.db import models
from django.contrib.auth.models import User

# Deploy data base
class Game(models.Model):
    cross_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games_as_cross', null=True, blank=True)
    nought_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games_as_nought', null=True, blank=True)
    whose_move = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_move', null=True, blank=True)
    moves = models.CharField(max_length=100, default='')
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner', null=True, blank=True)