class TicTacToe:
    board_size = 3

    def __init__(self):
        self.winner = None
        self.next_player = 'X'
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
    

    def make_move(self, player: str, x: int, y: int) -> bool:
        if player not in set(['X', 'O']): return False

        if self.board[x][y] in set(['X', 'O']): return False

        self.board[x][y] = player

        self.next_player = 'O' if player == 'X' else 'X'
        
        self.check_for_winner('X')
        self.check_for_winner('O')
        return True
    
    
    def check_for_winners(self):
        self.check_for_winner('X')
        self.check_for_winner('O')


    def check_for_winner(self, player: str):
        size = self.board_size

        # check rows and columns
        for x in range(size):
            if all(self.board[x][y] == player for y in range(size)) or \
               all(self.board[y][x] == player for y in range(size)):
                self.winner = player
        
        # check diagonal
        if all(self.board[i][i] == player for i in range(size)):
            self.winner = player
            
        if all(self.board[i][size - i - 1] == player for i in range(size)):
            self.winner = player
                