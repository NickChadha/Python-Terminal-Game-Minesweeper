class Board:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
        self.game_board = [[Tile() for i in range(self.num_cols)] for j in range(self.num_rows)]
    
    def show_board(self):
        display = '\t\t '
        for col in range(self.num_cols):
            if col == 0:
                display += '  ' + str(col)
            elif col < 10:
                display += '    ' + str(col)
            else:
                display += '   ' + str(col)
            
        
        for row in range(self.num_rows):
            display += '\n\t' + Board.alphabet[row] + '\t'
            for col in range(self.num_cols):
                display += '  ' + str(self.game_board[row][col])
        print(display)
        

    def create_board(self, first_tile):
        pass    
    

class Tile:
    def __init__(self):
        self.visible = False
        self.value = 0
    
    def __repr__(self):
        if self.visible:
            return '[{VALUE}]'.format(VALUE=self.value)
        else:
            return '[ ]'