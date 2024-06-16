class Board:
    def __init__(self, difficulty):
        self.num_rows
        self.num_cols
        self.num_mines
        self.difficulty
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