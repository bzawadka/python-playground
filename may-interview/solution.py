import random

class Solution:
    board_size = 4
    default_no_of_items = 8

    def __init__(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]


    def remove_empty_cells(self, my_board: list[list]) -> list[list]:
        temp_board = [] 
        for y, row in enumerate(my_board):
            temp_board.append([])
            for cell in row:
                if cell != ' ':
                    temp_board[y].append(cell)
        return temp_board


    def make_move(self, inst: str) -> None:
        match inst:
            case 'r':
                # move right
                pass
            case 'u':
                # move up
                pass
            case 'd':
                # move down
                pass
            case 'l':
                temp_board = self.remove_empty_cells(self.board)

                for row in temp_board:
                    if len(row) >= 2:
                        first_value = int(row[0])
                        second_value = int(row[1])
                        if second_value == first_value:
                            row[0] = str(first_value + second_value)
                            row[1] = ' '

                    if len(row) >= 3:
                        second_value = int(row[1]) if row[1] != ' ' else -1
                        third_value = int(row[2]) if row[2] != ' ' else -1

                        if second_value == third_value:
                            if len(row) >= 3:
                                row[1] = str(second_value + third_value)
                                row[2] = ' '

                    if len(row) >= 4:
                        third_value = int(row[2]) if row[2] != ' ' else -1
                        fourth_value = int(row[3]) if row[3] != ' ' else -1

                        if third_value == fourth_value:
                            if len(row) >= 4:
                                row[2] = str(third_value + fourth_value)
                                row[3] = ' '

                temp_board = self.remove_empty_cells(temp_board)

                # use temp_board
                # keep appeding empty elements until I have 4 in a row
                for row in temp_board:
                    while len(row) < self.board_size:
                        row.append(' ')

                self.board = temp_board

            case _:
                raise RuntimeError('unknown instruction')

        # return temp_board


    def init_board(self, items: list[tuple[int,int]]) -> None:
        if not items:
            empty_cells = [(x, y) for y, row in enumerate(self.board)
                                  for x, cell in enumerate(row)
                                  if cell == ' ']
            
            for i in range(self.default_no_of_items):
                item = random.choice(empty_cells)
                y, x = item
                self.board[y][x] = '2'


        for x, y in items:
            self.board[y][x] = '2'

    
