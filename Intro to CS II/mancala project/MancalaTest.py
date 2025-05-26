"""Unit tests"""

import unittest
from io import StringIO
from unittest.mock import patch
from Mancala import Mancala, Player

class TestMancala(unittest.TestCase):
    """Unit tests for Mancala"""
    def setUp(self):
        self.game = Mancala()

        self.player1 = self.game.create_player("Joe")
        self.player2 = self.game.create_player("Mark")

        self.board = self.game.get_board()

    def test_player_obj(self):
        # player names stored as objects;
        # read as "Joe", "Mark"

        player1 = self.player1.get_name()
        player2 = self.player2.get_name()

        self.assertIsInstance(self.player1, object)
        self.assertIsInstance(self.player2, object)
        self.assertEqual(player1, "Joe")
        self.assertEqual(player2, "Mark")

    def test_player_list(self):
        # private Mancala array stores Player objects
        # in correct order ["Joe", "Mark"]

        players = self.game.get_players()
        joe = players[0].get_name()
        mark = players[1].get_name()

        self.assertIsInstance(players[0], object)
        self.assertIsInstance(players[1], object)
        self.assertEqual(joe, "Joe")
        self.assertEqual(mark, "Mark")

    def test_wrongplayer(self):
        # non-string player name returns None

        player3 = self.game.create_player(2)

        self.assertIs(player3, None)

    def test_player1_wins(self):
        # player 2 runs out of seeds, game stops,
        # player 1 counts own seeds, updates store, wins

        self.game.play_game(2, 1)
        self.game.play_game(2, 2)
        self.game.play_game(2, 3)
        self.game.play_game(2, 4)
        self.game.play_game(2, 5)
        self.game.play_game(2, 6)

        result = self.game.return_winner()
        msg = "Winner is player 1: Joe"
        store_result = 36
        store_actual = self.board[6]

        self.assertEqual(result, msg)
        self.assertEqual(store_result, store_actual)

    def test_player2_wins(self):
        # player 1 runs out of seeds, game stops,
        # player 2 counts own seeds, updates store, wins
        self.game.play_game(1, 1)
        self.game.play_game(1, 2)
        self.game.play_game(1, 3)
        self.game.play_game(1, 4)
        self.game.play_game(1, 5)
        self.game.play_game(1, 6)

        result = self.game.return_winner()
        msg = "Winner is player 2: Mark"

        self.assertEqual(result, msg)

    def test_game_continues(self):
        # game continues after winner declared
        # play_game() checks status
        self.game.play_game(1, 1)
        self.game.play_game(1, 2)
        self.game.play_game(1, 3)
        self.game.play_game(1, 4)
        self.game.play_game(1, 5)
        self.game.play_game(1, 6)

        result = self.game.return_winner()
        msg = "Winner is player 2: Mark"

        self.assertEqual(result, msg)

        status = self.game.play_game(1, 1)
        msg = "Game is ended"
        game = self.game.get_game()

        self.assertEqual(status, msg)
        self.assertEqual(game, False)

    # test tie

    # game continues after tie

    def game_not_ended(self):
        # function return_winner()
        # reads game state,
        # returns "Game has not ended"
        self.game.play_game(1, 2)
        self.game.play_game(2, 1)

        result = self.game.return_winner()
        msg = "Game has not ended"
        self.assertEqual(result, msg)

    def test_player1_move(self):
        # player 1 moves
        # not into either store or player 2 pits

        result = [0, 5, 5, 5, 5, 4]

        self.game.play_game(1, 1)
        player1_pits = self.board[0:6]

        self.assertEqual(player1_pits, result)

    def test_player1_jaunt(self):
        # player 1 moves into player 2 pits
        result = [5, 5, 5, 4, 4, 4]

        self.game.play_game(1, 6)

        player2_pits = self.board[7:13]

        self.assertEqual(player2_pits, result)

    def test_player1_store(self):
        # player 1 moves into own store

        self.game.play_game(1, 3)

        store1_result = 1
        player1_store = self.board[6]

        self.assertEqual(player1_store, store1_result)

    def test_player1_skip(self):
        # player 1 doesn't move into player 2 store

        self.game.play_game(1, 1)
        self.game.play_game(1, 2)
        self.game.play_game(1, 3)
        self.game.play_game(1, 4)
        self.game.play_game(1, 5)
        self.game.play_game(2, 5)
        self.game.play_game(1, 6)

        store2_result = 1
        player2_store = self.board[13]

        self.assertEqual(player2_store, store2_result)

    def test_player2_move(self):
        # player 2 moves
        # not into either store or player 1 pits

        result = [0, 5, 5, 5, 5, 4]

        self.game.play_game(2, 1)
        player2_pits = self.board[7:13]

        self.assertEqual(player2_pits, result)

    def test_player2_jaunt(self):
        # player 2 moves into player 1 pits
        result = [5, 5, 5, 4, 4, 4]

        self.game.play_game(2, 6)

        player1_pits = self.board[0:6]

        self.assertEqual(player1_pits, result)

    def test_player2_store(self):
        # player 2 moves into own store
        self.game.play_game(2, 3)

        store2_result = 1
        player2_store = self.board[13]

        self.assertEqual(player2_store, store2_result)

    def test_player2_skip(self):
        # player 2 skips player 1 store

        self.game.play_game(2, 1)
        self.game.play_game(2, 2)
        self.game.play_game(2, 3)
        self.game.play_game(2, 4)
        self.game.play_game(2, 5)
        self.game.play_game(1, 5)
        self.game.play_game(2, 6)

        store1_result = 1
        player1_store = self.board[6]

        self.assertEqual(player1_store, store1_result)

    def test_player1_rule2(self):
        # player 1's last seed in own, empty pit
        # gets player 2's opposing seeds

        self.game.play_game(1, 1)
        self.game.play_game(1, 2)
        self.game.play_game(1, 3)
        self.game.play_game(1, 4)
        self.game.play_game(1, 5)
        self.game.play_game(1, 6)

        store = self.board[6]

        self.assertEqual(store, 12)

    def test_player2_rule2_(self):
        # player 2's last seed in own, empty pit
        # gets player 1's opposing seeds

        self.game.play_game(1, 1)
        self.game.play_game(1, 2)
        self.game.play_game(1, 3)
        self.game.play_game(1, 4)
        self.game.play_game(1, 5)
        self.game.play_game(2, 1)
        self.game.play_game(2, 2)
        self.game.play_game(2, 3)
        self.game.play_game(2, 4)

        self.game.play_game(2, 5)

        store1 = self.board[6]
        store1_result = 4
        store2 = self.board[13]
        store2_result = 16

        self.assertEqual(store1, store1_result)
        self.assertEqual(store2, store2_result)

    def test_wrong_pit(self):
        # player tries wrong pit
        error1 = self.game.play_game(1, 0)
        error2 = self.game.play_game(1, 7)

        self.assertEqual(error1, "Invalid number for pit index")
        self.assertEqual(error2, "Invalid number for pit index")

    def test_player1_rule1(self):
        # player 1's last seed in own store
        # special rule 1 message prints:
        # "player 1 take another turn

        result = "player 1 take another turn\n"
        with patch("sys.stdout", new = StringIO()) as output:
            self.game.play_game(1, 3)
            self.assertEqual(output.getvalue(), result)

    def test_player2_rule1(self):
        # player 2's last seed in own store
        # special rule 1 message prints:
        # "player 2 take another turn"

        result = "player 2 take another turn\n"
        with patch("sys.stdout", new = StringIO()) as output:
            self.game.play_game(2, 3)
            self.assertEqual(output.getvalue(), result)

    def test_board_return(self):
        # function play_game() returns board

        result = self.game.play_game(1, 2)
        expected = [4, 0, 5, 5, 5, 5, 0,
                    4, 4, 4, 4, 4, 4, 0]

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
