from django.test import TestCase
from django.contrib.auth.models import User
from game.models import Game

class GameTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')

    def test_make_move(self):
        game = Game.objects.create(cross_id=self.user1, whose_move=self.user1)

        self.assertEqual(game.cross_id, self.user1)
        self.assertEqual(game.whose_move, self.user1)
        self.assertEqual(game.moves, '123456789')
        self.assertIsNone(game.winner)

        game.make_move(1, 'x')

        self.assertEqual(game.moves, 'x23456789')
        self.assertIsNone(game.winner) 

        game.make_move(2, 'o')

        self.assertEqual(game.moves, 'xo3456789')
        self.assertIsNone(game.winner)  

        game.make_move(3, 'x')

        self.assertEqual(game.moves, 'xox456789')
        self.assertNotEqual(game.winner, self.user1) 

    def test_get_board(self):
        game = Game.objects.create(moves='xoxooxoxo')

        board = game.get_board()

        self.assertEqual(board, [
            ['x', 'o', 'x'],
            ['o', 'o', 'x'],
            ['o', 'x', 'o'],
        ])
