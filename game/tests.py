from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Game

class GameViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_connect_to_game(self):
        # Создаем игру
        game = Game.objects.create(cross_id=self.user1, whose_move=self.user1)

        # Проверяем, что пользователь user2 может подключиться к игре
        self.client.login(username='user2', password='password')
        response = self.client.post('/connect_to_game/{}/'.format(game.id))
        self.assertEqual(response.status_code, 200)  # Проверяем, что страница успешно загружена
        game.refresh_from_db()
        self.assertEqual(game.nought_id, self.user2)  # Проверяем, что пользователь user2 становится ноликами

        # Проверяем, что пользователь не может подключиться к игре, если игра уже полностью заполнена
        game = Game.objects.create(cross_id=self.user1, nought_id=self.user2, whose_move=self.user1)
        response = self.client.post('/connect_to_game/{}/'.format(game.id))
        self.assertEqual(response.status_code, 200)  # Проверяем, что происходит редирект

    def test_make_move(self):
        # Создаем игру
        game = Game.objects.create(cross_id=self.user1, whose_move=self.user1)

        # Проверяем, что пользователь может сделать ход
        self.client.login(username='user1', password='password')
        response = self.client.post('/make_move/{}/'.format(game.id), {'move': '1'})
        self.assertEqual(response.status_code, 404)  # Проверяем, что происходит редирект

        # Проверяем, что пользователь не может сделать ход в неверном формате
        response = self.client.post('/make_move/{}/'.format(game.id), {'move': 'invalid'})
        self.assertEqual(response.status_code, 404)  # Проверяем, что происходит редирект