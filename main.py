from User import *

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
                pass
            elif choice == 4: # Save and quit
                # TODO: save
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

def main():
    User.load_stats()
    Main.main_menu()

if __name__ == '__main__':
    main()