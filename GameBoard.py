from colorama import init, Fore, Back, Style
import random

FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]

class Board:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    init()

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
        display = ['  ']
        for col in range(self.num_cols):
            if col == 0 or col >= 10:
                display[0] += '   ' + str(col)
            elif col < 10:
                display[0] += '    ' + str(col)
        for row in range(self.num_rows):
            display.append('\t ' + Board.alphabet[row])
            index = row + 1
            for col in range(self.num_cols):
                display[index] += '  [^]'
        
        board_backs = [BACKS[2], BACKS[6]]
        board_backs_index = 0
        row_count = 0
        row_index = 0
        for line_num in range(len(display)):
            if line_num == 0:
                print('\n\t', end='')
                Board.print_with_color(display[line_num] + ' ', color=BACKS[0], brightness=BRIGHTNESS[2])
            else:
                col_index = 0
                line_split = display[line_num].split('^')
                Board.print_with_color(line_split[0], color=board_backs[board_backs_index], brightness=BRIGHTNESS[2], end='')
                for line_split_index in range(len(line_split[1:])):
                    # check coding style standards for really long lines
                    Board.print_with_color(self.actual_board[row_index][col_index], color=board_backs[board_backs_index]+Tile.val_to_color[self.actual_board[row_index][col_index].value], brightness=BRIGHTNESS[2], end='')
                    Board.print_with_color(line_split[line_split_index + 1], color=board_backs[board_backs_index], brightness=BRIGHTNESS[2], end='')
                    col_index += 1
                print()
                row_index += 1
                row_count += 1
                if row_count == 3:
                    row_count = 0
                    board_backs_index += 1
                    if board_backs_index == len(board_backs):
                        board_backs_index = 0

    def add_mines(self, first_tile_info):
        # there's likely a better way to handle this with exceptions
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
       
        for row in range(len(self.actual_board)):
            for col in range(len(self.actual_board[row])):
                if self.actual_board[row][col].value == 'X':
                    affected_rows = [row - 1, row, row + 1]
                    affected_cols = [col - 1, col, col + 1]
                    if row == 0:
                        affected_rows = [row, row + 1]
                    elif row == self.num_rows - 1:
                        affected_rows = [row - 1, row]
                    if col == 0:
                        affected_cols = [col, col + 1]
                    elif col == self.num_cols - 1:
                        affected_cols = [col - 1, col]
                    for affected_row in affected_rows:
                        for affected_col in affected_cols:
                            if not self.actual_board[affected_row][affected_col].value == 'X':
                                self.actual_board[affected_row][affected_col].value += 1
        self.uncover_tile(first_tile_info)
        self.show_board()

    def uncover_tile(self, tile_info):
        pass

    @staticmethod
    def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
        print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)
    

class Tile:
    val_to_color = {
        0: FORES[0], # black
        1: FORES[5],# magenta
        2: FORES[3], # yellow
        3: FORES[7], # white
        4: FORES[4], # blue
        5: FORES[5], # magenta
        6: FORES[3], # yellow
        7: FORES[7], # white
        8: FORES[4], # blue
        'X': FORES[1], # red
        '*': FORES[1] # red
    }
    
    def __init__(self):
        self.visible = True
        self.value = 0
        self.flagged = False
    
    def __repr__(self):
        if self.flagged:
            return '*'
        elif self.visible:
            return '{VALUE}'.format(VALUE=self.value)
        else:
            return ' '