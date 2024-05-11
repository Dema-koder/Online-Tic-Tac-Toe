from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game as gm
from django.http import HttpResponseRedirect

@login_required
def create_game(request):
    if request.method == 'POST':
        game = gm.objects.create(cross_id=request.user, whose_move=request.user)
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
    game = gm.objects.get(id=game_id)
    if game.nought_id == None and game.cross_id != request.user:
        game.nought_id = request.user
    if game.cross_id != request.user and game.nought_id != request.user:
        return redirect('connect')
    game.save()
    return render(request, 'game/connect_to_game.html', {'game': game})

@login_required
def make_move(request, game_id):
    game = gm.objects.get(id=game_id)
    if game.whose_move != request.user:
        return redirect('connect_to_game', game_id=game_id)
    if request.method == 'POST':
        move = request.POST.get('move')
        if move.isdigit() and 1 <= int(move) <= 9:
            kol = 0
            for cell in game.moves:
                if cell != 'x' and cell != 'o':
                    kol += 1
            res = ''
            if kol % 2 == 1:
                res = 'x'
            else:
                res = 'o'
            game.make_move(move, res)
            return HttpResponseRedirect(request.path_info) 
    return redirect('connect_to_game', game_id=game_id)