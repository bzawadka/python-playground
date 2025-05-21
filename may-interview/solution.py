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
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]


    def make_move(self, instr: Direction, generate_new_item: bool = False) -> GameState:
        match instr:
            case Direction.RIGHT | Direction.DOWN:
                match instr:
                    case Direction.RIGHT:
                        temp_board = self.remove_empty_cells(self.board)
                    case Direction.DOWN:
                        # transpose the board to work with columns as rows; then repat the logic for moving right
                        transposed = self.transpose(self.board)
                        temp_board = self.remove_empty_cells(transposed)

                for row in temp_board:
                    i = len(row) - 1    # starting from the right
                    while i > 0:
                        # compare pairs; if adjacent numbers are equal - add values in the right cell
                        if row[i] == row[i - 1]:
                            row[i] = row[i] + row[i - 1]
                            row[i - 1] = ' '
                            i -= 1 # skip merged cell    
                        i -= 1

                temp_board = self.remove_empty_cells(temp_board)
                temp_board = self.prepend_empty_cells(temp_board)
                self.board = temp_board if instr == Direction.RIGHT else self.transpose(temp_board)

            case Direction.LEFT | Direction.UP:
                match instr:
                    case Direction.LEFT:
                        temp_board = self.remove_empty_cells(self.board)
                    case Direction.UP:
                        # transpose the board to work with columns as rows; then repat the logic for moving left
                        transposed = self.transpose(self.board)
                        temp_board = self.remove_empty_cells(transposed)

                for row in temp_board:
                    i = 0   # starting from the left
                    while i < len(row) - 1:
                        # compare pairs; if adjacent numbers are equal - add values in the left cell
                        if row[i] == row[i + 1]:
                            row[i] = row[i] + row[i + 1]
                            row[i + 1] = ' '
                            i += 1  # skip merged cell
                        i += 1

                temp_board = self.remove_empty_cells(temp_board)
                temp_board = self.append_empty_cells(temp_board)
                self.board = temp_board if instr == Direction.LEFT else self.transpose(temp_board)

            case _:
                raise RuntimeError('unknown instruction')

        if generate_new_item:
            self.generate_new_random_item_on_the_board()

        return self.game_state()


    def game_state(self) -> GameState:
        if any(2048 in row for row in self.board):
            return GameState.WON
        elif not any(' ' in row for row in self.board):
            return GameState.LOST
        else:
            return GameState.PLAYING


    def generate_new_random_item_on_the_board(self):
        empty_cells = [(x, y) for y, row in enumerate(self.board)
                              for x, cell in enumerate(row)
                              if cell == ' ']
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.board[y][x] = self.default_item_value


    def remove_empty_cells(self, board: list[list]) -> list[list]:
        return [[c for c in row if c != ' '] for row in board]


    def append_empty_cells(self, board: list[list]) -> list[list]:
        for row in board:
            while len(row) < self.board_size:
                row.append(' ')
        return board


    def prepend_empty_cells(self, board: list[list]) -> list[list]:
        for row in board:
            while len(row) < self.board_size:
                row.insert(0, ' ')
        return board


    def transpose(self, board: list[list]) -> list[list]:
        return [[board[y][x] for y in range(self.board_size)] for x in range(self.board_size)]


    def init_board(self, items: list[tuple[int,int]]) -> None:
        # random assignment
        if not items:
            empty_cells = [(x, y) for y, row in enumerate(self.board)
                                  for x, cell in enumerate(row)
                                  if cell == ' ']

            for _ in range(self.default_no_of_items):
                item = random.choice(empty_cells)
                x, y = item
                self.board[y][x] = 2
                empty_cells.remove(item)

        # explicit assignment
        for x, y in items:
            self.board[y][x] = self.default_item_value
