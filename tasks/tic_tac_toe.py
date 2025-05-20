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
        if self.check_winner('X'):
            self.winner = 'X'
        elif self.check_winner('O'):
            self.winner = 'O'

        return self.is_board_full() and self.winner is None
    
    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)
    
    def make_move(self, player: str, row: int, col: int) -> bool:
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False

        if self.board[row][col] == ' ' and player == self.current_player:
            self.board[row][col] = player
            self.current_player = 'O' if player == 'X' else 'X'
            if self.check_winner(player):
                self.winner = player
            return True

        return False
    
    def check_winner(self, player: str) -> bool:
        size = self.board_size

        # Check rows and columns
        for i in range(size):
            if all(self.board[i][j] == player for j in range(size)) or \
               all(self.board[j][i] == player for j in range(size)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(size)) or \
           all(self.board[i][size - i - 1] == player for i in range(size)):
            return True

        return False
    
    def create_problem(self):
        raise RuntimeError("problem")