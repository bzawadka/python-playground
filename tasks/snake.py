
class Game:
    default_board_width = 21
    default_board_height = 15
    default_snake_length = 3

    def __init__(self, board_width: int = default_board_width, board_height: int = default_board_height):
        self.game_over = False
        self.board = [[' ' for _ in range(board_width)] for _ in range(board_height)]
        self.draw_initial_snake(board_width)


    def draw_initial_snake(self, board_width):
        default_snake_position_w = board_width // 2
        default_snake_position_h = 1
        self.snake_direction = 'd'

        # draw initial snake
        self.snake = []
        for i in range(self.default_snake_length):
            x = default_snake_position_w
            y = i + default_snake_position_h
            self.board[y][x] = 'x'
            self.snake.append((x, y))
            self.snake_head = (x, y)
    
    
    def tick(self):
        # assume no moves/instructions for now
        # knowing snake direction, move the head - down, left, right or up
        
        # clear the tail
        tail_x, tail_y = self.snake.pop(0)
        self.board[tail_y][tail_x] = ' '
        
        # move the head
        head_x, head_y = self.snake[-1]
        match self.snake_direction:
            case 'd':
                x = head_x
                y = head_y + 1
            case _:
                raise RuntimeError('unknown direction')

        head = (x, y)
        try:
            self.board[y][x] = 'x'
            self.snake.append(head)
            self.snake_head = head
        except IndexError:
            self.game_over = True

            
    def place_item(self):
        pass