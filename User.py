import csv

class User:
    filename = 'user_info.csv'

    def __init__(self, username):
        self.username = username
        self.games_won = 0
        self.games_lost = 0

    def check_username(name):
        while True:
            if ',' in name:
                print('Sorry, you can\'t use commas in your username. Please enter a valid username!')
                name = input()
            else: # username is valid
                break

        current_user = None
        name = name.title()
        if False: # TODO: check if username exists
            print('\nWelcome back {NAME}, let\'s play some Minesweeper: Terminal Detonation!'.format(NAME=name))
            current_user = None
            # TODO: get user from list
        else: # new username
            print('\nLooks like you\'re a new user. Welcome {NAME}, let\'s play some Minesweeper: Terminal Detonation!'.format(NAME=name))
            current_user = User(name)
            # TODO: add to user list
        return current_user

    def view_stats(self):
        pass   

    @staticmethod 
    def load_stats():
        pass

    @staticmethod
    def write_stats():
        pass