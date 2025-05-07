from tic_tac_toe import *


def test_game_init():
    game = TicTacToe()
    assert game.current_player == 'X'
    assert game.winner is None
    assert game.is_draw() is False
    assert game.board == [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]
    # another way    
    for row in game.board:
        assert all(cell == ' ' for cell in row) is True


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
    # horizontal
    game = TicTacToe()
    game.board = [['O', 'O', 'O'],
                  ['X', 'X', 'O'],
                  [' ', 'X', 'X']]
    assert game.is_board_full() is False
    assert game.is_draw() is False
    assert game.winner == 'O'

    # manual
    game2 = TicTacToe()
    game2.make_move('X', 1, 1)
    game2.make_move('O', 0, 0)
    game2.make_move('X', 1, 0)
    game2.make_move('O', 2, 1)
    assert game2.winner is None
    game2.make_move('X', 1, 2)
    game2.make_move('O', 0, 1)
    game2.make_move('X', 2, 2)
    game2.make_move('O', 0, 2)
    assert game2.winner is 'O'

    # vertical
    game3 = TicTacToe()
    game3.board = [['O', ' ', 'X'],
                  ['O', 'X', ' '],
                  ['O', ' ', ' ']]
    assert game3.is_draw() is False
    assert game3.winner == 'O'

    # diagonal
    game4 = TicTacToe()
    game4.board = [['O', ' ', 'X'],
                  [' ', 'O', 'X'],
                  [' ', ' ', 'O']]
    assert game4.is_draw() is False
    assert game4.winner == 'O'

    # diagonal
    game5 = TicTacToe()
    game5.board = [['X', ' ', 'O'],
                  ['X', 'O', ' '],
                  ['O', ' ', ' ']]
    assert game5.is_draw() is False
    assert game5.winner == 'O'


def test_some_exception():
    game = TicTacToe()
    try:
        game.create_problem()
    except Exception as e:
        msg = e.args[0]

    assert msg is "problem"


def __main__():
    game = TicTacToe()
    game.print_board()

if __name__ == "__main__":
    __main__()
