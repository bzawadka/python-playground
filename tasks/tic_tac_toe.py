class TicTacToe:
    board_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.winner = None
        self.current_player = 'X'

    def print_board(self):
        print('Current board:')
        print('-' * 5)
        for row in self.board:
            print('|'.join(row))
        print('-' * 5)

    def is_draw(self) -> bool:
        return self.is_board_full() and self.winner is None
    
    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)
    
    def make_move(self, player: str, row: int, col: int) -> bool:
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False

        if self.board[row][col] == ' ' and player == self.current_player:
            self.board[row][col] = player
            self.current_player = 'O' if player == 'X' else 'X'
            return True
        return False