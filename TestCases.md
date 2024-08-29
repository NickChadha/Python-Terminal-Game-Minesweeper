# Test Cases

For each of the following test cases, first run Main.py to begin. Then, follow the steps listed for each test case to verify the output is correct.

## Main Menu

### 1

* Type "1" and press enter. You should see an explanation of the game rules pop up.
* Type any integer other than 1, 2, or 3, then press enter. You should see an error message telling you that your input is invalid.
* Type "3" and press enter. You should see a thank you message and the program should stop running.

## User Menu

### 2

* Type "2" and press enter. You should be prompted to enter a username. 
* Since you don't have one yet, type any name you'd like (ignores capitalization), then press enter. You should see a message referring to you by your username that says you're a new user.
* Type "2" and press enter. You should see your stats pop up. With no games won or lost, and your win rate will be at 0%.
* Type "4" and press enter. You should see a thank you message and the program should stop running.
* If you check the [user_info.csv](user_info.csv) file, you should see your username in the second line, with zeros for your wins and losses (if you haven't completed any games yet).

## Minesweeper Game

### 3

* Type "2" and press enter. You should be prompted to enter your username.
* Type your username that you selected and press enter. You should see a message welcoming you back.
* Type "3" and press enter. You should see a prompt to choose your game difficulty.
* Type "1" and press enter. You should see a board with 8 columns and rows going from A to I.
* Select a tile to uncover, and type its row letter, then column number, then press enter.
* Repeat this step until you purposefully uncover a mine. You should see a game over message and a board revealing the locations of the remaining mines.
* Type "2" and press enter. You should see 0 games won and 1 game lost (if this is the first game you've completed).
* Type "4" and press enter. You should see a thank you message and the program should stop running.
* If you check the [user_info.csv](user_info.csv) file, you should see 0 wins and 1 loss for your username (if this is the first game you've completed).

### 4

* Type "2" and press enter. You should be prompted to enter your username.
* Type your username that you selected and press enter. You should see a message welcoming you back.
* Type "3" and press enter. You should see a prompt to choose your game difficulty.
* Type "2" and press enter. You should see a board with 15 columns and rows going from A to P.
* Select a tile to uncover, and type its row letter, then column number, then press enter.
* Select a tile to flag, and type its row letter, then column number, then an asterisk (*), then press enter.
* Repeat the above two steps until you have uncovered every safe tile. You should see a message congratulating you for completing Intermediate difficulty.
* Type "2" and press enter. You should see 1 game won and 1 game lost (if you've followed the previous test cases).
* Type "4" and press enter. You should see a thank you message and the program should stop running.
* If you check the [user_info.csv](user_info.csv) file, you should see 1 win and 1 loss for your username (if you've followed the previous test cases).