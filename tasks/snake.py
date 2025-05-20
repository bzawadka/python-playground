from enum import Enum
import random

class Direction(Enum):
    RIGHT = 'r'
    LEFT = 'l'
    UP = 'u'
    DOWN = 'd'

class Game:
    default_board_width = 21
    default_board_height = 15
    default_snake_length = 3
    eatable_item = 'o'
    snake_body = 'x'

    def __init__(self, 
                 board_width: int = default_board_width, 
                 board_height: int = default_board_height, 
                 snake_length: int = default_snake_length):
        self.game_over = False
        self.board = [[' ' for _ in range(board_width)] for _ in range(board_height)]
        self.instructions = []
        self.snake_has_eaten = False
        self.draw_initial_snake(board_width, snake_length)


    def draw_initial_snake(self, board_width, snake_length) -> None:
        default_snake_position_w = board_width // 2
        default_snake_position_h = 1
        self.snake_direction = Direction.DOWN

        self.snake = []
        for i in range(snake_length):
            x = default_snake_position_w
            y = i + default_snake_position_h
            self.board[y][x] = self.snake_body
            self.snake.append((x, y))
            self.snake_head = (x, y)


    def instruct(self, instr: Direction) -> bool:
        # if instr not in {d.value for d in Direction}: return False
        self.instructions.append(instr)
        return True


    def tick(self) -> None:
        # what are the instructions?
        if len(self.instructions) > 0:
            instr = self.instructions.pop(0)
            self.snake_direction = instr
        
        # clear the tail... unless snake has just eaten in the previous move!
        if self.snake_has_eaten:
            self.snake_has_eaten = False 
        else:
            tail_x, tail_y = self.snake.pop(0)
            self.board[tail_y][tail_x] = ' '
        
        # knowing snake direction, move the head - down, left, right or up
        # move the head
        head_x, head_y = self.snake[-1]
        match self.snake_direction:
            case Direction.DOWN:
                x = head_x
                y = head_y + 1
            case Direction.RIGHT:
                x = head_x + 1
                y = head_y
            case Direction.UP:
                x = head_x
                y = head_y - 1
            case Direction.LEFT:
                x = head_x - 1
                y = head_y
            case _:
                raise RuntimeError('unknown direction')

        head = (x, y)
        try:
            what_is_ahead = self.board[y][x]
            if what_is_ahead == self.eatable_item:
                self.snake_has_eaten = True

            if what_is_ahead == self.snake_body:
                self.game_over = True
                
            if not self.game_over:
                self.board[y][x] = self.snake_body
                self.snake.append(head)
                self.snake_head = head
        except IndexError:
            self.game_over = True

            
    def place_item(self, x: int = -1, y: int = -1):
        # choose randomly one of empty cells
        if x == -1 or y == -1:
            empty_cells = [(c, r) for r, row in enumerate(self.board)
                                  for c, cell in enumerate(row) if cell == ' ']
            if not empty_cells:
                return    
            x, y = random.choice(empty_cells)
        
        if self.board[y][x] == self.snake_body:
            raise RuntimeError('item cannot be placed on non-empty cell')
        
        self.board[y][x] = self.eatable_item