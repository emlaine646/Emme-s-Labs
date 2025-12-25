#----------------------------------SOURCE CODE----------------------------------
"""
Emme's LAB Assignment 7B - Tic-Tac-Toe: In this lab we created a player class
to make a board with each space containing either a symbol or an empty string.
Then, we created a nested list to make our board with each space being an
initial Player object.  I then created two players, one and two and assigned
them symbols and if they move they change that index to their symbol (from
its default to a default symbol).

"""

class Player:
    MIN_SYMBOL = "A"
    MAX_SYMBOL = "Z"
    MAX_WINS = 5
    DEFAULT_SYMBOL = " "

    # constructor
    def __init__(self, symbol=DEFAULT_SYMBOL, wins=0):
        self.symbol = symbol
        self.wins = wins

    # setters
    def set_symbol(self, symbol):
        if Player.MIN_SYMBOL <= symbol <= Player.MAX_SYMBOL:
            self.symbol = symbol
            return True
        return False

    def set_wins(self, wins):
        self.wins = wins

    def get_symbol(self):
        return self.symbol

    def get_wins(self):
        return self.wins

    def to_string(self):
        return self.symbol

    def add_win(self):
        if self.wins < Player.MAX_WINS:
            self.wins += 1
            return True
        return False

    def resetWins(self):
        self.wins = 0


MIN_VALUE = 0
MAX_VALUE = 2


def symbolFromUser():
    while True:
        try:
            player_symbol = input("What is the symbol for a player?: ").upper()
            if (player_symbol < Player.MIN_SYMBOL or player_symbol >
                    Player.MAX_SYMBOL or len(player_symbol) > 1):
                print("Sorry that is no good.  Invalid symbol try again:")
            else:
                return player_symbol
        except ValueError:
            print("Input a valid character")



def resetBoard():
    board = [[Player(), Player(), Player()], [Player(), Player(), Player()],
             [Player(), Player(), Player()]]
    return board


def makeAMove(board: list[list[Player]], player: Player):
    while True:
        try:
            row = int(input(
                "Enter a row (0, 1, or 2) for player " + player.get_symbol() +
                ": "))
            coll = int(input(
                "Enter a coll (0, 1, or 2) for player " + player.get_symbol()
                + ": "
                  ""))
            if 0 <= row <= 2 and 0 <= coll <= 2 and board[row][
                coll].get_symbol() == ' ':
                board[row][coll].set_symbol(player.get_symbol())
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Use numbers 0, 1, or 2.")


# get collum from the user
# if play row collumer != ' ' then ask agian return nothing
# if its valid you have to replace object with players object set player() to

def displayBoard(board):
    print("-------------")
    for row in range(3):
        p1 = board[row][0].to_string()
        p2 = board[row][1].to_string()
        p3 = board[row][2].to_string()
        print("| {} | {} | {} |".format(p1, p2, p3))
        print('-------------')

def is_draw(board: list[list[Player]], player: Player):
        for row in range(3):
            for coll in range(3):
                if board[row][coll].get_symbol() != ' ':
                    print("Draw game")
                    return True
                else:
                    return True




def isWin(board: list[list[Player]], player: Player) -> bool:
    row_1_win = board[0][0].get_symbol() == player.get_symbol() and board[0][
        1].get_symbol() == player.get_symbol() and board[0][
                    2].get_symbol() == player.get_symbol()
    row_2_win = board[1][0].get_symbol() == player.get_symbol() and board[1][
        1].get_symbol() == player.get_symbol() and board[1][
                    2].get_symbol() == player.get_symbol()
    row_3_win = board[2][0].get_symbol() == player.get_symbol() and board[2][
        1].get_symbol() == player.get_symbol() and board[2][
                    2].get_symbol() == player.get_symbol()

    coll_1_win = board[0][0].get_symbol() == player.get_symbol() and board[1][
        0].get_symbol() == player.get_symbol() and board[2][
                     0].get_symbol() == player.get_symbol()
    coll_2_win = board[0][1].get_symbol() == player.get_symbol() and board[1][
        1].get_symbol() == player.get_symbol() and board[2][
                     1].get_symbol() == player.get_symbol()
    coll_3_win = board[0][2].get_symbol() == player.get_symbol() and board[1][
        2].get_symbol() == player.get_symbol() and board[2][
                     2].get_symbol() == player.get_symbol()

    dia_1_win = board[0][0].get_symbol() == player.get_symbol() and board[1][
        1].get_symbol() == player.get_symbol() and board[2][
                    2].get_symbol() == player.get_symbol()
    dia_2_win = board[0][2].get_symbol() == player.get_symbol() and board[1][
        1].get_symbol() == player.get_symbol() and board[2][
                    0].get_symbol() == player.get_symbol()
    return any(
        [row_1_win, row_2_win, row_3_win, coll_1_win, coll_2_win, coll_3_win,
         dia_1_win, dia_2_win])


def is_draw(board: list[list[Player]], player: Player):
    for row in range(3):
        for coll in range(3):
            if board[row][coll].get_symbol() == ' ':
                return False
    print("Draw game")
    return True


def main():
    game_count = 0
    sym_user_1 = symbolFromUser()
    sym_user_2 = symbolFromUser()
    player_1 = Player(sym_user_1)
    player_2 = Player(sym_user_2)
    while game_count < Player.MAX_WINS:
        game_count += 1
        board = resetBoard()
        print("Game ", game_count, " is starting")
        print("Player ", player_1.get_symbol(), "has ", player_1.get_wins(), " wins")
        print("Player ", player_2.get_symbol(), "has ", player_2.get_wins(), " wins")
        displayBoard(board)
        while True:
            makeAMove(board, player_1)
            p1_win = isWin(board, player_1)
            displayBoard(board)
            if p1_win:
                print("Player " + player_1.get_symbol() + " wins!")
                player_1.add_win()
                break
            if is_draw(board, player_1):
                break
            makeAMove(board, player_2)
            p2_win = isWin(board, player_2)
            if p2_win:
                print("Player " + player_2.get_symbol() + " wins!")
                player_2.add_win()
                break
            if is_draw(board, player_2):
                break
            displayBoard(board)
    print("\n")
    print("Player ", player_1.get_symbol(), "has ", player_1.get_wins(),
          " wins")
    print("Player ", player_2.get_symbol(), "has ", player_2.get_wins(),
          " wins")


main()

#--------------------------------------RUN--------------------------------------
"""
C:\Users\lunal\PycharmProjects\PythonProject\.venv\Scripts\python.exe "C:\Users\lunal\PycharmProjects\PythonProject\LAB Assignment 7B - Tic-Tac-Toe.py" 
What is the symbol for a player?: X
What is the symbol for a player?: O
Game  1  is starting
Player  X has  0  wins
Player  O has  0  wins
-------------
|   |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 0
Enter a coll (0, 1, or 2) for player X: 0
-------------
| X |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 1
Enter a coll (0, 1, or 2) for player O: 1
-------------
| X |   |   |
-------------
|   | O |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 0
Enter a coll (0, 1, or 2) for player X: 1
-------------
| X | X |   |
-------------
|   | O |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 0
Enter a coll (0, 1, or 2) for player O: 2
-------------
| X | X | O |
-------------
|   | O |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 1
Enter a coll (0, 1, or 2) for player X: 0
-------------
| X | X | O |
-------------
| X | O |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 2
Enter a coll (0, 1, or 2) for player O: 0
Player O wins!
Game  2  is starting
Player  X has  0  wins
Player  O has  1  wins
-------------
|   |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 0
Enter a coll (0, 1, or 2) for player X: 0
-------------
| X |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 2
Enter a coll (0, 1, or 2) for player O: 2
-------------
| X |   |   |
-------------
|   |   |   |
-------------
|   |   | O |
-------------
Enter a row (0, 1, or 2) for player X: 1
Enter a coll (0, 1, or 2) for player X: 0
-------------
| X |   |   |
-------------
| X |   |   |
-------------
|   |   | O |
-------------
Enter a row (0, 1, or 2) for player O: 2
Enter a coll (0, 1, or 2) for player O: 0
-------------
| X |   |   |
-------------
| X |   |   |
-------------
| O |   | O |
-------------
Enter a row (0, 1, or 2) for player X: 2
Enter a coll (0, 1, or 2) for player X: 1
-------------
| X |   |   |
-------------
| X |   |   |
-------------
| O | X | O |
-------------
Enter a row (0, 1, or 2) for player O: 1
Enter a coll (0, 1, or 2) for player O: 1
-------------
| X |   |   |
-------------
| X | O |   |
-------------
| O | X | O |
-------------
Enter a row (0, 1, or 2) for player X: 0
Enter a coll (0, 1, or 2) for player X: 2
-------------
| X |   | X |
-------------
| X | O |   |
-------------
| O | X | O |
-------------
Enter a row (0, 1, or 2) for player O: 0
Enter a coll (0, 1, or 2) for player O: 1
-------------
| X | O | X |
-------------
| X | O |   |
-------------
| O | X | O |
-------------
Enter a row (0, 1, or 2) for player X: 1
Enter a coll (0, 1, or 2) for player X: 2
-------------
| X | O | X |
-------------
| X | O | X |
-------------
| O | X | O |
-------------
Draw game
Game  3  is starting
Player  X has  0  wins
Player  O has  1  wins
-------------
|   |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 0
Enter a coll (0, 1, or 2) for player X: 0
-------------
| X |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 2
Enter a coll (0, 1, or 2) for player O: 2
-------------
| X |   |   |
-------------
|   |   |   |
-------------
|   |   | O |
-------------
Enter a row (0, 1, or 2) for player X: 0
Enter a coll (0, 1, or 2) for player X: 2
-------------
| X |   | X |
-------------
|   |   |   |
-------------
|   |   | O |
-------------
Enter a row (0, 1, or 2) for player O: 1
Enter a coll (0, 1, or 2) for player O: 1
-------------
| X |   | X |
-------------
|   | O |   |
-------------
|   |   | O |
-------------
Enter a row (0, 1, or 2) for player X: 0
Enter a coll (0, 1, or 2) for player X: 1
-------------
| X | X | X |
-------------
|   | O |   |
-------------
|   |   | O |
-------------
Player X wins!
Game  4  is starting
Player  X has  1  wins
Player  O has  1  wins
-------------
|   |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 1
Enter a coll (0, 1, or 2) for player X: 1
-------------
|   |   |   |
-------------
|   | X |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 1
Enter a coll (0, 1, or 2) for player O: 0
-------------
|   |   |   |
-------------
| O | X |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 2
Enter a coll (0, 1, or 2) for player X: 0
-------------
|   |   |   |
-------------
| O | X |   |
-------------
| X |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 0
Enter a coll (0, 1, or 2) for player O: 2
-------------
|   |   | O |
-------------
| O | X |   |
-------------
| X |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 1
Enter a coll (0, 1, or 2) for player X: 2
-------------
|   |   | O |
-------------
| O | X | X |
-------------
| X |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 0
Enter a coll (0, 1, or 2) for player O: 1
-------------
|   | O | O |
-------------
| O | X | X |
-------------
| X |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 2
Enter a coll (0, 1, or 2) for player X: 2
-------------
|   | O | O |
-------------
| O | X | X |
-------------
| X |   | X |
-------------
Enter a row (0, 1, or 2) for player O: 0
Enter a coll (0, 1, or 2) for player O: 0
Player O wins!
Game  5  is starting
Player  X has  1  wins
Player  O has  2  wins
-------------
|   |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 1
Enter a coll (0, 1, or 2) for player X: 2
-------------
|   |   |   |
-------------
|   |   | X |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 1
Enter a coll (0, 1, or 2) for player O: 0
-------------
|   |   |   |
-------------
| O |   | X |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 0
Enter a coll (0, 1, or 2) for player X: 2
-------------
|   |   | X |
-------------
| O |   | X |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player O: 0
Enter a coll (0, 1, or 2) for player O: 0
-------------
| O |   | X |
-------------
| O |   | X |
-------------
|   |   |   |
-------------
Enter a row (0, 1, or 2) for player X: 2
Enter a coll (0, 1, or 2) for player X: 2
-------------
| O |   | X |
-------------
| O |   | X |
-------------
|   |   | X |
-------------
Player X wins!


Player  X has  2  wins
Player  O has  2  wins

Process finished with exit code 0

"""