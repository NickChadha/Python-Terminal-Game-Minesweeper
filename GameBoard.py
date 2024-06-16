from colorama import init, Fore, Back, Style
import random

class Board:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    init()
    FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
    BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]

    def __init__(self, difficulty):
        self.num_rows = 0
        self.num_cols = 0
        self.num_mines = 0
        self.difficulty = ''
        if difficulty == 1:
            self.difficulty = 'Beginner'
            self.num_rows = 9
            self.num_cols = 9
            self.num_mines = 16
        elif difficulty == 2:
            self.difficulty = 'Intermediate'
            self.num_rows = 16
            self.num_cols = 16
            self.num_mines = 40
        else:
            self.difficulty = 'Expert'
            self.num_rows = 16
            self.num_cols = 30
            self.num_mines = 99
        self.actual_board = [[Tile() for i in range(self.num_cols)] for j in range(self.num_rows)]
    
    def show_board(self):
        display = ['\n\t\t ']
        for col in range(self.num_cols):
            if col == 0:
                display[0] += '  ' + str(col)
            elif col < 10:
                display[0] += '    ' + str(col)
            else:
                display[0] += '   ' + str(col)
        for row in range(self.num_rows):
            display.append('\t' + Board.alphabet[row] + '\t')
            index = row + 1
            for col in range(self.num_cols):
                display[index] += '  ' + str(self.actual_board[row][col])
        
        fore_index = 0
        brightness_index = 0
        for line in display:
            Board.print_with_color(line, color=Board.FORES[fore_index], brightness=Board.BRIGHTNESS[brightness_index])
            brightness_index += 1
            if brightness_index == len(Board.BRIGHTNESS):
                brightness_index = 0
                fore_index += 1

    def add_mines(self, first_tile_info):
        row = first_tile_info[0]
        col = first_tile_info[1]
        mines_left = self.num_mines
        safe_tiles = [[row, col]]
        safe_rows = [row - 1, row, row + 1]
        safe_cols = [col - 1, col, col + 1]
        if row == 0:
            safe_rows = [row, row + 1]
        elif row == self.num_rows - 1:
            safe_rows = [row - 1, row]
        if col == 0:
            safe_cols = [col, col + 1]
        elif col == self.num_cols - 1:
            safe_cols = [col - 1, col]
        for safe_row in safe_rows:
            for safe_col in safe_cols:
                safe_tiles.append([safe_row, safe_col])
        
        while mines_left > 0:
            mine_location = [random.randint(0, self.num_rows - 1), random.randint(0, self.num_cols - 1)]
            if not mine_location in safe_tiles:
                self.actual_board[mine_location[0]][mine_location[1]].value = 'X'
                mines_left -= 1
        # TODO: finish implementing here
        self.show_board()

    def uncover_tile(self, tile_info):
        pass

    @staticmethod
    def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
        print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)
    

class Tile:
    def __init__(self):
        self.visible = True
        self.value = 0
    
    def __repr__(self):
        if self.visible:
            return '[{VALUE}]'.format(VALUE=self.value)
        else:
            return '[ ]'