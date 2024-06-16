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
    
    def play_new_game(difficulty):
        game_board = Board(difficulty)
        Board.show_board(game_board)

# end of class Main

def main():
    User.load_stats()
    Main.main_menu()

if __name__ == '__main__':
    main()