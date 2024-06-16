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
        print('Minesweeper: Terminal Detonation by Nick Chadha')
        while True:
            print('\nPlease enter the number indicating the action you would like to take:')
            for option in Main.main_menu_options:
                print(option)
            choice = input('Enter number choice: ').strip()
            choice = Main.check_choice(choice, len(Main.main_menu_options))
            if choice == 1: # Read the rules of the game
                # TODO: implement rules description
                pass
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
                # TODO: implement rules description
                pass
            elif choice == 2: # View my stats
                User.view_stats(current_user)
            elif choice == 3: # Play a new game
                print('\nPlease enter a number to choose your difficulty:')
                for option in Main.difficulty_menu_options:
                    print(option)
                difficulty = input('Enter number choice: ').strip()
                difficulty = Main.check_choice(difficulty, len(Main.difficulty_menu_options))
                Main.play_new_game(difficulty)
            elif choice == 4: # Save and quit
                User.write_stats()
                print('\nThanks for playing!')
                return
            
    def check_choice(choice, menu_length):
        choice = int(choice) # TODO: handle possible error
        if choice > 0 and choice <= menu_length:
            return choice
        else:
            choice = input('Invalid Input. Please enter a valid number: ').strip()
            choice = Main.check_choice(choice, menu_length)
        return choice
    
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
        
    
    def play_new_game(difficulty):
        game_board = Board(difficulty)
        Board.show_board(game_board)
        tile_info = input('\nPlease select a tile to uncover. Enter the row letter, then column number, and add an asterisk if you wish to flag the tile as a bomb: ')
        first_tile_info = Main.parse_game_input(tile_info, game_board)
        Board.add_mines(game_board, first_tile_info)
        while True:
            tile_info = input('\nPlease select a tile to uncover. Enter the row letter, then column number, and add an asterisk if you wish to flag the tile as a bomb: ')
            tile_info = Main.parse_game_input(tile_info, game_board)
            Board.uncover_tile(game_board, tile_info)
            # TODO: handle case where player loses --> exit while loop, adjust stats

# end of class Main

def main():
    User.load_stats()
    Main.main_menu()

if __name__ == '__main__':
    main()