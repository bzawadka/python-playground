import random
from enum import Enum

class Direction(Enum):
    UP = 'u'
    DOWN = 'd'
    LEFT = 'l'
    RIGHT = 'r'

class GameState(Enum):
    PLAYING = 'playing'
    WON = 'won'
    LOST = 'lost'

class Solution:
    board_size = 4
    default_no_of_items = 8
    default_item_value = 2

    def __init__(self):
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]


    def make_move(self, instr: Direction, generate_new_item: bool = False) -> GameState:
        rotated = False
        if instr in (Direction.UP, Direction.DOWN):
            self.board = self.transpose(self.board)
            rotated = True

        if instr in (Direction.LEFT, Direction.UP):
            self.board = [self.merge_row(row) for row in self.board]
        else:
            self.board = [self.merge_row(row[::-1])[::-1] for row in self.board]

        if rotated:
            self.board = self.transpose(self.board)

        if generate_new_item:
            self.generate_new_random_item_on_the_board()

        return self.game_state()


    def merge_row(self, src_row):
        row = self.non_empty_items(src_row)
        merged = []
        skip = False
        for i in range(len(row)):
            if skip:
                skip = False
                continue
            if i + 1 < len(row) and row[i] == row[i + 1]:
                merged.append(row[i] * 2)
                skip = True
            else:
                merged.append(row[i])
        merged += [0] * (self.board_size - len(merged))
        return merged


    def non_empty_items(self, row):
        return [n for n in row if n != 0]


    def game_state(self) -> GameState:
        if any(2048 in row for row in self.board):
            return GameState.WON
        if any(0 in row for row in self.board):
            return GameState.PLAYING
        return GameState.LOST


    def generate_new_random_item_on_the_board(self):
        empty_cells = [(x, y) for y in range(self.board_size)
                              for x in range(self.board_size)
                              if self.board[y][x] == 0]
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.board[y][x] = self.default_item_value


    def transpose(self, board):
        return [list(row) for row in zip(*board)]


    def init_board(self, items: list[tuple[int, int]]) -> None:
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        for x, y in items:
            self.board[y][x] = self.default_item_value
