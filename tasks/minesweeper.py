
class Minesweeper:
    default_board_size = 7
    
    def __init__(self, board_size: int = default_board_size):
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.bombs = list()
        self.board_size = board_size
        self.game_over = False


    def plant_bombs(self, bombs: list) -> None:
        self.bombs.extend(bombs)
        for bomb in bombs:
            x, y = bomb
            self.board[y][x] = 'b'


    def make_move(self, x: int, y: int) -> None:
        if self.board[y][x] == 'b':
            self.game_over = True
        # TODO make actual move which does not hit the bomb


    def prepare_board(self) -> None:
        # for each bomb
        #   get coordinates of every neighbour
        #       for each neighbour
        #           if it's count is not yet set
        #               get coordinates of every neighbour
        #               count how many of them are bombs
        #               enter the count in current cell
        
        for bomb in self.bombs:
            print('processing' + str(bomb))
            neighbours = self.get_neighbours(bomb)
            
            for n in neighbours:
                x, y = n
                if self.board[y][x] != ' ':
                    continue
                
                coordinates = self.get_neighbours(n)
                bomb_count = self.count_bombs_at(coordinates)
                if bomb_count > 0:
                    self.board[y][x] = str(bomb_count)
        


    def get_neighbours(self, point_coordinates: tuple[int, int]) -> list[tuple[int, int]]:
        x_src, y_src = point_coordinates
        neighbours = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                new_x = x_src + x
                new_y = y_src + y
                
                if (0 <= new_x < self.board_size) and (0 <= new_y < self.board_size):
                    neighbours.append((new_x, new_y))
        
        return neighbours


    def count_bombs_at(self, coordinates: list) -> int:
        bomb_count = 0
        for c in coordinates:
            x, y = c
            if self.board[y][x] == 'b':
                bomb_count += 1
        return bomb_count


if __name__ == "__main__":
    game = Minesweeper()