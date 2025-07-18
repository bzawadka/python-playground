from solution import *


def test_init_solution():
    s = Solution()
    assert s.board == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

    s.init_board([(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (3, 1), (3, 3)])
    assert s.board == [
        [2, 0, 2, 0],
        [0, 2, 0, 2],
        [2, 0, 2, 0],
        [0, 2, 0, 2]]



def test_move_left_adds_numbers():
    s = Solution()
    s.init_board([(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (3, 1), (3, 3)])
    s.make_move(Direction.LEFT)
    assert s.board == [
        [4, 0, 0, 0],
        [4, 0, 0, 0],
        [4, 0, 0, 0],
        [4, 0, 0, 0]]


def test_move_right_adds_numbers():
    s = Solution()
    s.init_board([(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (3, 1), (3, 3)])
    s.make_move(Direction.RIGHT)
    assert s.board == [
        [0, 0, 0, 4],
        [0, 0, 0, 4],
        [0, 0, 0, 4],
        [0, 0, 0, 4]]


def test_move_left_on_empty_board():
    s = Solution()
    assert s.board == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

    s.make_move(Direction.LEFT)
    assert s.board == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

    s.make_move(Direction.RIGHT)
    assert s.board == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


def test_move_left_all_filled():
    s = Solution()
    s.board = [
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2]]

    s.make_move(Direction.LEFT)
    assert s.board == [
        [4, 4, 0, 0],
        [4, 4, 0, 0],
        [4, 4, 0, 0],
        [4, 4, 0, 0]]


def test_move_right_all_filled():
    s = Solution()
    s.board = [
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2]]

    s.make_move(Direction.RIGHT)
    assert s.board == [
        [0, 0, 4, 4],
        [0, 0, 4, 4],
        [0, 0, 4, 4],
        [0, 0, 4, 4]]


def test_move_left_not_all_added():
    s = Solution()
    s.board = [
        [4, 2, 2, 0],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2]]

    s.make_move(Direction.LEFT)
    assert s.board == [
        [4, 4, 0, 0],
        [4, 4, 0, 0],
        [4, 4, 0, 0],
        [4, 4, 0, 0]]


def test_requirement_2_merge_left():
    s = Solution()
    s.board = [
        [0, 8, 2, 2],
        [4, 2, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 2]]

    s.make_move(Direction.LEFT)
    assert s.board == [
        [8, 4, 0, 0],
        [4, 4, 0, 0],
        [0, 0, 0, 0],
        [2, 0, 0, 0]]


def test_requirement_3_merge_right():
    s = Solution()
    s.board = [
        [0, 8, 2, 2],
        [4, 2, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 2]]

    s.make_move(Direction.RIGHT)
    assert s.board == [
        [0, 0, 8, 4],
        [0, 0, 4, 4],
        [0, 0, 0, 0],
        [0, 0, 0, 2]]


def test_requirement_4_merge_up():
    s = Solution()
    s.board = [
        [0, 8, 2, 2],
        [4, 2, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 2]]

    s.make_move(Direction.UP)
    assert s.board == [
        [4, 8, 2, 4],
        [0, 2, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


def test_requirement_4_merge_down():
    s = Solution()
    s.board = [
        [0, 8, 2, 2],
        [4, 2, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 2]]

    s.make_move(Direction.DOWN)
    assert s.board == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 8, 0, 2],
        [4, 2, 2, 4]]


def test_requirement_5_generate_new_item():
    s = Solution()
    s.board = [
        [0, 8, 2, 2],
        [4, 2, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 2]]

    s.make_move(Direction.UP, generate_new_item=True)

    # after the move, first row is always populated
    assert s.board[0] == [4, 8, 2, 4]

    # remaining rows should contain two original cells with number 2, and one new - generated
    remainder = s.board[1:]
    cells_with_2 = [(x, y) for y, row in enumerate(remainder)
                           for x, cell in enumerate(row)
                           if cell == 2]

    assert len(cells_with_2) == 3


def test_requirement_6_game_state_playing():
    s = Solution()
    s.init_board([(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (3, 1), (3, 3)])
    state = s.make_move(Direction.LEFT)
    assert state == GameState.PLAYING


def test_requirement_6_game_state_won():
    s = Solution()
    s.board = [
        [4, 0, 0, 2],
        [1024, 0, 0, 1024],
        [4, 2, 0, 0],
        [4, 0, 0, 0]]

    state = s.make_move(Direction.LEFT)
    assert state == GameState.WON


def test_requirement_6_game_state_lost():
    s = Solution()
    s.board = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]]

    state = s.make_move(Direction.LEFT)
    assert state == GameState.LOST

    

if __name__ == "__main__":
    test_init_solution()
    print("All tests passed.")
