import csv

class User:
    filename = 'user_info.csv'
    user_list = []

    def __init__(self, username, wins=0, losses=0):
        self.username = username
        self.wins = wins
        self.losses = losses
        User.user_list.append(self)

    def check_username(name):
        while True:
            if ',' in name:
                print('Sorry, you can\'t use commas in your username. Please enter a valid username!')
                name = input()
            else: # username is valid
                break

        current_user = None
        name = name.title()
        username_found = False
        user_index = -1
        for user in User.user_list:
            if user.username == name:
                username_found = True
                current_user = user

        if username_found:
            print('\nWelcome back {NAME}, let\'s play some Minesweeper: Terminal Detonation!'.format(NAME=name))
        else: # new username
            print('\nLooks like you\'re a new user. Welcome {NAME}, let\'s play some Minesweeper: Terminal Detonation!'.format(NAME=name))
            current_user = User(name)
        return current_user

    def view_stats(self):
        win_rate = 0
        if not (self.wins == 0 and self.losses == 0):
            win_rate = 100 * self.wins / float(self.wins + self.losses)

        print('\nLet\'s take a look at your stats, {NAME}!'.format(NAME=self.username))
        print('\tGames won:\t{WINS}\n\tGames lost:\t{LOSSES}\n\tWin rate:\t{:.2f}%'.format(win_rate, WINS=self.wins, LOSSES=self.losses))   

    @staticmethod 
    def load_stats():
        with open(User.filename) as user_info:
            info_reader = csv.DictReader(user_info)
            for row in info_reader:
                User(row['Username'], wins=int(row['Wins']), losses=int(row['Losses']))
    
    @staticmethod
    def write_stats():
        with open(User.filename, 'w') as user_info:
            user_info.write('Username,Wins,Losses')
            for user in User.user_list:
                user_info.write('\n{USERNAME},{WINS},{LOSSES}'.format(USERNAME=user.username, WINS=user.wins, LOSSES=user.losses))