from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game

@login_required
def create_game(request):
    if request.method == 'POST':
        game = Game.objects.create(cross_id=request.user, whose_move=request.user)
        return redirect('connect_to_game', game_id=game.id)
    return render(request, 'game/create_game.html')

@login_required
def connect(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        if game_id.isdigit():
            return redirect('connect_to_game', game_id=int(game_id))
    return render(request, 'game/connect.html')

@login_required
def connect_to_game(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'game/connect_to_game.html', {'game': game})