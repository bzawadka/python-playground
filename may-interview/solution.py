import random

class Solution:
    board_size = 4
    default_no_of_items = 8

    def __init__(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]


    def remove_empty_cells(self, my_board: list[list]) -> list[list]:
        temp_board = [] 
        for row in my_board:
            temp_board.append([c for c in row if c != ' '])
        return temp_board


    def make_move(self, inst: str) -> None:
        temp_board = self.remove_empty_cells(self.board)
        match inst:
            # move right
            case 'r':
                for row in temp_board:
                    i = len(row) - 1
                    while i >= 0:
                        # if adjacent numbers are equal - add value in the right
                        if row[i] == row[i - 1]:
                            row[i] = str(int(row[i]) + int(row[i - 1]))
                            row[i - 1] = ' '
                            i -= 1 # skip merged cell    
                        i -= 1

                temp_board = self.remove_empty_cells(temp_board)
                for row in temp_board:
                    while len(row) < self.board_size:
                        row.insert(0, ' ')

            # move up
            case 'u':
                pass
            # move down
            case 'd':
                pass
            # move left
            case 'l':
                for row in temp_board:
                    i = 0
                    while i < len(row) - 1:
                        # if adjacent numbers are equal - add value in the left
                        if row[i] == row[i + 1]:
                            row[i] = str(int(row[i]) + int(row[i + 1]))
                            row[i + 1] = ' '
                            i += 1 # skip merged cell    
                        i += 1

                temp_board = self.remove_empty_cells(temp_board)
                for row in temp_board:
                    while len(row) < self.board_size:
                        row.append(' ')

            case _:
                raise RuntimeError('unknown instruction')


        self.board = temp_board

        # return temp_board


    def init_board(self, items: list[tuple[int,int]]) -> None:
        # random assignment
        if not items:
            empty_cells = [(x, y) for y, row in enumerate(self.board)
                                  for x, cell in enumerate(row)
                                  if cell == ' ']

            for _ in range(self.default_no_of_items):
                item = random.choice(empty_cells)
                x, y = item
                self.board[y][x] = '2'
                empty_cells.remove(item)

        # explicit assignment
        for x, y in items:
            self.board[y][x] = '2'

    
