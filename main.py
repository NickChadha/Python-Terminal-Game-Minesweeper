from User import *
from GameBoard import *

class Main:
    main_menu_options = [
        '1) Read the rules of the game',
        '2) Sign in',
        '3) Quit'
    ]
    user_menu_options = [
        '1) Read the rules of the game',
        '2) View my stats',
        '3) Play a new game',
        '4) Save and quit'
    ]
    difficulty_menu_options = [
        '1) Beginner',
        '2) Intermediate',
        '3) Expert'
    ]

    def main_menu():
        choice = 0
        print('\nMinesweeper: Terminal Detonation by Nick Chadha')
        while True:
            print('\nPlease enter the number indicating the action you would like to take:')
            for option in Main.main_menu_options:
                print(option)
            choice = input('Enter number choice: ').strip()
            choice = Main.check_choice(choice, len(Main.main_menu_options))
            if choice == 1: # Read the rules of the game
                Main.display_rules()
            elif choice == 2: # Sign in
                print('\nPlease enter your username. If you don\'t have one yet, choose any name for your account!')
                name = input()
                current_user = User.check_username(name)
                Main.user_menu(current_user)
                quit()
            elif choice == 3: # Quit
                print('\nThanks for playing!')
                break

    def user_menu(current_user):
        while True:
            print('\nPlease enter the number indicating the action you would like to take:')
            for option in Main.user_menu_options:
                print(option)
            choice = input('Enter number choice: ').strip()
            choice = Main.check_choice(choice, len(Main.user_menu_options))
            if choice == 1: # Read the rules of the game
                Main.display_rules()
                pass
            elif choice == 2: # View my stats
                User.view_stats(current_user)
            elif choice == 3: # Play a new game
                print('\nPlease enter a number to choose your difficulty:')
                for option in Main.difficulty_menu_options:
                    print(option)
                difficulty = input('Enter number choice: ').strip()
                difficulty = Main.check_choice(difficulty, len(Main.difficulty_menu_options))
                Main.play_new_game(difficulty, current_user)
            elif choice == 4: # Save and quit
                User.write_stats()
                print('\nThanks for playing!')
                return
            
    def check_choice(choice, menu_length): # TODO: change function name to check_menu_choice()
        choice = int(choice) # TODO: handle possible error
        if choice > 0 and choice <= menu_length:
            return choice
        else:
            choice = input('Invalid Input. Please enter a valid number: ').strip()
            choice = Main.check_choice(choice, menu_length)
        return choice 
    
    def display_rules():
        print('\nWelcome to Minesweeper: Terminal Detonation! You can navigate between menus by entering the number of option you\'d like to select.')
        print('You can sign in to save your stats and view them after playing a round of Minesweeper. The following are the rules to the game:')
        print('There are 3 difficulty levels: Beginner (9x9 tiles), Intermediate (16x16 tiles), and Expert (16x30 tiles). Here\'s an example of a Beginner board:')
        example_game_board = Board(1)
        Board.show_board(example_game_board)
        print('\nEach turn, you can either uncover a tile or put a flag (*) on a tile to mark it as a mine. You select a tile by entering the row letter and column number,' +
              ' and add an asterisk (*) if you want to flag that tile.')
        print('For example, if I want to uncover the tile at row D and column 3, I would type: D3. If I instead wanting to put a flag on that tile, I\'d type: D3*')
        print('NOTE: You will never dig up a mine on your very first turn.')
        example_first_tile_info = Main.parse_game_input('D3', example_game_board)
        Board.add_mines(example_game_board, example_first_tile_info)
        print('\nThis is what the board could look like after uncovering tile D3 on the first turn.' +
              ' The number on each tile represents the number of mines in the vicinity (8 bordering tiles)')
        print('Use this information to uncover tiles that can\'t have mines and put flags on the tiles that must have mines.' +
              ' Successfully uncover every safe tile in order to win, but be careful not to dig up a mine, as that\'s an instant game over. Good luck!')
    
    def play_new_game(difficulty, current_user):
        game_board = Board(difficulty)
        Board.show_board(game_board)
        tile_info = input('\nPlease select a tile to uncover. Enter the row letter, then column number, and add an asterisk if you wish to flag the tile as a bomb: ')
        first_tile_info = Main.parse_game_input(tile_info, game_board)
        Board.add_mines(game_board, first_tile_info)
        while True:
            tile_info = input('\nPlease select a tile to uncover. Enter the row letter, then column number, and add an asterisk if you wish to flag the tile as a bomb: ')
            tile_info = Main.parse_game_input(tile_info, game_board)
            if tile_info[2]:
                Board.flag_tile(game_board, tile_info[0], tile_info[1])
            else:
                success = Board.uncover_tile(game_board, tile_info[0], tile_info[1])
                Board.show_board(game_board)
                if not success:
                    print('\nGame over! You dug up a mine. Better luck next time!')
                    current_user.losses += 1
                    User.write_stats()
                    return
                elif game_board.check_win():
                    print('\nCongrats, you didn\'t dig up a single mine! You won the game on {DIFFICULTY} difficulty!'.format(DIFFICULTY=difficulty))
                    current_user.wins += 1

    def parse_game_input(tile_info, game_board):
        row = -1
        col = -1
        flag = False
        while True:
            if type(tile_info) == type([0, 0, 0]):
                return tile_info
            row = Board.alphabet.index(tile_info[0].upper())
            if '*' in tile_info:
                flag = True
                col = int(tile_info[1:tile_info.index('*')])
            else:
                col = int(tile_info[1:])
            if row >= game_board.num_rows or col >= game_board.num_cols:
                tile_info = input('Invalid Input. Please enter a valid response: ')
                tile_info = Main.parse_game_input(tile_info, game_board)
            else:
                break
        return [row, col, flag]
# end of class Main

def main():
    User.load_stats()
    Main.main_menu()

if __name__ == '__main__':
    main()