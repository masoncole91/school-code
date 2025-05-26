"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Dec. 4, 2022
Description: Plays a game of Mancala with two players in the terminal
"""

class Mancala:
    """Stores game logic for moves and the game's two special rules"""
    def __init__(self):
        self._board = [4 for _ in range(6)] + [0] + [4 for _ in range(6)] + [0]
        self._game = True
        self._players = []

    def create_player(self, name):
        """Stores player names as Player class objects"""
        if isinstance(name, str):
            name = Player(name)
            self._players.append(name)
            return name
        return None

    def get_board(self):
        """Returns board"""
        return self._board

    def get_game(self):
        """Returns game status"""
        return self._game

    def get_players(self):
        """Returns list of Player objects"""
        return self._players

    def play_game(self, player, pit):
        """Prevents invalid moves;
        Runs helper function for moving seeds, evaluating rules;
        Returns updated board"""
        board = self._board

        if self._game is False:
            return "Game is ended"

        if pit > 6 or pit <= 0:
            return "Invalid number for pit index"

        self._move_seeds(player, pit)

        return board

    def print_board(self):
        """Prints current player status and board positions"""
        self.return_winner()

        player1_pits = self._board[0:6]
        player1_store = self._board[6]
        player2_pits = self._board[7:13]
        player2_store = self._board[13]

        print("player1:")
        print("store:", player1_store)
        print(player1_pits)
        print("player2:")
        print("store:", player2_store)
        print(player2_pits)

    def return_winner(self):
        """Determines winner or tie"""
        board = self._board

        players = self._players
        player1_obj = players[0]
        player1_name = player1_obj.get_name()
        player2_obj = players[1]
        player2_name = player2_obj.get_name()

        player1_pits = board[0:6]
        player2_pits = board[7:13]

        store1, store2 = board[6], board[13]

        if sum(player2_pits) == 0 and sum(player1_pits) > 0:
            self._game = False
            board[6] += sum(player1_pits)
            board[0:6] = [0, 0, 0, 0, 0, 0]

            if board[6] == board[13]:
                return "It's a tie"

            return "Winner is player 1: " + player1_name

        if sum(player1_pits) == 0 and sum(player2_pits) > 0:
            self._game = False
            board[13] += sum(player2_pits)
            board[7:13] = [0, 0, 0, 0, 0, 0]

            if board[6] == board[13]:
                return "It's a tie"

            return "Winner is player 2: " + player2_name

        return "Game has not ended"

    def _move_seeds(self, player, pit):
        """Runs the game's primary logic;
        Adds player's seeds to iterating pits;
        Runs helper function for special rules 1 and 2"""
        board = self._board
        store = None
        pit -= 1
        last = None

        if player == 1:
            store = 13
        if player == 2:
            pit += 7
            store = 6

        current = pit + 1

        for _ in range(board[pit]):
            last = current % len(board)
            if last != store:
                board[last] += 1
            else:
                last = (current + 1) % len(board)
                board[last] += 1
            current += 1

        board[pit] = 0

        self._special_rule_1(player, last)
        self._special_rule_2(player, last)

        return board

    def _special_rule_1(self, player, last):
        """If player last lands in own store;
        Player gets additional turn"""
        if player == 1:
            store = 6
            if last == store:
                print("player 1 take another turn")
        else:
            store = 13
            if last == store:
                print("player 2 take another turn")

    def _special_rule_2(self, player, last):
        """If player lands in last own empty pit;
        Player gets opponent's seeds from vertically across board"""
        board = self._board
        player1_pits = board[0:6]
        player1_store = 6
        player2_pits = board[7:13]
        player2_store = 13

        if board[last] == 1:
            if player == 1 and (0 <= last < 6):
                opposite = last
                player2_pits = player2_pits[::-1]
                if player2_pits[opposite] > 0:
                    board[player1_store] += player2_pits[opposite]
                    board[player1_store] += board[last]
                    player2_pits[opposite], board[last] = 0, 0
                    player2_pits = player2_pits[::-1]
                    board[7:13] = player2_pits

            if player == 2 and (7 <= last < 13):
                opposite = last - 7
                player1_pits = player1_pits[::-1]
                if player1_pits[opposite] > 0:
                    board[player2_store] += player1_pits[opposite]
                    board[player2_store] += board[last]
                    player1_pits[opposite], board[last] = 0, 0
                player1_pits = player1_pits[::-1]
                board[0:6] = player1_pits

        return board

class Player:
    """Houses objects for game players"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        """Returns string name of player"""
        return self._name
