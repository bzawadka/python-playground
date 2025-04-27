from tic_tac_toe import *


def test_game_init():
    game = TicTacToe()
    assert game.current_player == 'X'
    assert game.winner is None
    assert game.is_draw() is False
    assert game.board == [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]


def test_make_move():
    game = TicTacToe()
    if game.current_player == 'X':
        made_move = game.make_move('X', 0, 1)
    
    assert made_move is True
    assert game.board[0][1] == 'X'
    assert game.current_player == 'O'


def test_make_move_invalid():
    game = TicTacToe()
    assert game.current_player == 'X'
    move_made = game.make_move('O', 0, 1)  # Invalid move

    assert move_made is False
    assert game.board[0][1] == ' '
    assert game.current_player == 'X'


def test_make_move_out_of_bounds():
    game = TicTacToe()
    move_made = game.make_move('X', 4, 4)  # Out of bounds

    assert move_made is False
    assert game.board[0][1] == ' '
    assert game.current_player == 'X'


def test_move_cannot_overwrite():
    game = TicTacToe()
    move_made = game.make_move('X', 1, 1)
    assert move_made is True
    assert game.board[1][1] == 'X'

    move_made = game.make_move('O', 1, 1)  # Overwriting move
    assert move_made is False
    assert game.board[1][1] == 'X'
    assert game.current_player == 'O'


def test_is_draw():
    game = TicTacToe()
    game.board = [['X', 'O', 'X'],
                  ['O', 'X', 'O'],
                  ['O', 'X', 'O']]
    game.winner = None
    assert game.is_draw() is True
    assert game.is_board_full() is True


def test_is_winner():
    game = TicTacToe()
    game.board = [['X', 'X', 'X'],
                  ['O', 'O', 'O'],
                  ['O', 'X', 'O']]
    assert game.is_board_full() is True
    assert game.is_draw() is False
    assert game.winner == 'X'


def __main__():
    game = TicTacToe()
    game.print_board()

if __name__ == "__main__":
    __main__()
