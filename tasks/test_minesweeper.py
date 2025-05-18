from minesweeper import *


def test_init_minesweeper():
    m = Minesweeper()
    assert m.board == [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    m.plant_bombs([(1, 1), (3, 4)])
    m.plant_bombs([(2, 5), (4, 2), (3, 6)])
    assert m.board == [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'b', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'b', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'b', ' ', ' ', ' '],
        [' ', ' ', 'b', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'b', ' ', ' ', ' ']]
    assert m.bombs == [(1, 1), (3, 4), (2, 5), (4, 2), (3, 6)]

    m.prepare_board()
    assert m.board == [
        ['1', '1', '1', ' ', ' ', ' ', ' '],
        ['1', 'b', '1', '1', '1', '1', ' '],
        ['1', '1', '1', '1', 'b', '1', ' '],
        [' ', ' ', '1', '2', '2', '1', ' '],
        [' ', '1', '2', 'b', '1', ' ', ' '],
        [' ', '1', 'b', '3', '2', ' ', ' '],
        [' ', '1', '2', 'b', '1', ' ', ' ']]


def test_click_game_interactions():
    pass


def test_click_on_bomb_game_over():
    m = Minesweeper()
    m.plant_bombs([(1, 1), (3, 4), (2, 5), (4, 2), (3, 6)])
    m.prepare_board()
    m.game_over is False
    m.make_move(4, 2)
    m.game_over is True


if __name__ == "__main__":
    test_init_minesweeper()
    print("All tests passed.")
