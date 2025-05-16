from tic_tac import *


def board_is_empty(board: list[list[str]]) -> bool:
    return board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def test_game_init():
    game = TicTacToe()
    assert game.board_size == 3
    assert game.winner is None
    assert game.next_player == 'X'
    assert board_is_empty(game.board)


def test_game_moves():
    game = TicTacToe()
    res = game.make_move('X', 0, 0)
    assert res is True
    assert game.board == [['X', ' ', ' '], 
                          [' ', ' ', ' '], 
                          [' ', ' ', ' ']]
    assert game.next_player == 'O'
    res2 = game.make_move('O', 1, 1)
    assert res2 is True
    assert game.next_player == 'X'
    assert game.board == [['X', ' ', ' '], 
                          [' ', 'O', ' '], 
                          [' ', ' ', ' ']]
    assert game.winner is None


def test_prevent_invalid_move():
    game = TicTacToe()
    res = game.make_move('Z', 0, 0)
    assert res is False
    assert board_is_empty(game.board)


def test_prevent_move_override():
    game = TicTacToe()
    res1 = game.make_move('X', 1, 1)
    assert res1 is True
    res2 = game.make_move('O', 1, 1)
    assert res2 is False


def test_game_is_winner():
    game = TicTacToe()
    game.board = [['X', ' ', 'O'],
                  ['O', 'O', ' '],
                  ['X', 'X', 'X']]
    game.check_for_winners()
    assert game.winner == 'X'

    game.board = [['X', ' ', 'O'],
                  [' ', 'X', 'O'],
                  ['X', ' ', 'O']]
    game.check_for_winners()
    assert game.winner == 'O'


def test_game_winner_diagonal():
    game = TicTacToe()
    game.board = [['X', ' ', 'O'],
                  ['O', 'X', ' '],
                  ['X', 'O', 'X']]
    game.check_for_winners()
    assert game.winner == 'X'

    game.board = [[' ', 'X', 'O'],
                  [' ', 'O', ' '],
                  ['O', 'X', ' ']]
    game.check_for_winners()
    assert game.winner == 'O'


if __name__ == "__main__":
    test_game_is_winner()
    print("All tests passed.")