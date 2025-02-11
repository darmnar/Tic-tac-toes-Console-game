import random
import sys
import os


ascii_art = """

                                              )        (     
  *   )              )              *   )  ( /(        )\ )  
` )  /( (         ( /(    )       ` )  /(  )\())  (   (()/(  
 ( )(_)))\   (    )\())( /(   (    ( )(_))((_)\   )\   /(_)) 
(_(_())((_)  )\  (_))/ )(_))  )\  (_(_())   ((_) ((_) (_))   
|_   _| (_) ((_) | |_ ((_)_  ((_) |_   _|  / _ \ | __|/ __|  
  | |   | |/ _|  |  _|/ _` |/ _|    | |   | (_) || _| \__ \  
  |_|   |_|\__|   \__|\__,_|\__|    |_|    \___/ |___||___/  
                                                             


"""


def main():

    class Board:
        def __init__(self):
            # Initiate board

            self.board = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "],
            ]

        def update(self, row, column):
            if self.board[row][column] == " ":
                self.board[row][column] = "X"

        def update_cpu(self, row, column):
            if self.board[row][column] == " ":
                self.board[row][column] = "O"

        def draw_board(self):
            for line in self.board:
                for row in line:
                    print("|_" + str(row), end="_|")
                print("\n")

        def check_game(self):

            for row in self.board:
                if row[0] == row[1] == row[2]:
                    if row[0] == "X":
                        self.draw_board()
                        print("You won!")
                        sys.exit()
                    elif row[0] == "O":
                        self.draw_board()
                        print("You lost!")
                        sys.exit()

            for col in range(3):
                if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                    if self.board[0][col] == "X":
                        self.draw_board()
                        sys.exit("You won!")
                    elif self.board[0][col] == "O":
                        self.draw_board()
                        sys.exit("You lost!")

            collapsed_board = []

            for row in self.board:
                for item in row:
                    collapsed_board.append(item)
            if " " not in collapsed_board:
                sys.exit("IT IS A DRAW!")

            if self.board[0][0] == self.board[1][1] == self.board[2][2] == "X":
                self.draw_board()
                return sys.exit("You Won!")
            
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == "O":
                self.draw_board()
                return sys.exit("You lost!")

            if self.board[0][2] == self.board[1][1] == self.board[2][0] == "X":
                self.draw_board()
                return sys.exit("You Won!")
            
            if self.board[0][2] == self.board[1][1] == self.board[2][0] == "O":
                self.draw_board()
                return sys.exit("You lost!")

            else:
                pass

    class CPU:
        def __init__(self, board):
            pass

        def pick_a_spot(self):
            self.new_line = random.randint(0, 2)
            self.new_row = random.randint(0, 2)

        def check_spot(self):
            if (
                board.board[self.new_row][self.new_line] == "X"
                or board.board[self.new_row][self.new_line] == "O"
            ):
                self.pick_a_spot()
                self.check_spot()
            else:
                board.update_cpu(self.new_row, self.new_line)

    game_on = True
    board = Board()
    cpu = CPU(board)
    print(ascii_art)

    while game_on:
        board.draw_board()

        row = input("Please choose a row: ")
        try:
            row = int(row)
        except ValueError:
            os.system("cls")
            print("Valid number, please\n")
            continue
        if 0 <= row <= 2:
            pass
        if row > 2:
            os.system("cls")
            print("Please choose between 0 and 2\n")
            continue

        column = input("Please, choose a column: ")
        try:
            column = int(column)
        except ValueError:
            os.system("cls")
            print("Valid number, please\n")
            continue
        if 0 <= column <= 2:
            pass
        if column > 2:
            os.system("cls")
            print("Please choose between 0 and 2\n")
            continue
        if board.board[row][column] != " ":
            os.system("cls")
            print("\nSpot taken! Choose another field.\n")
            continue

        print("\n")

        board.update(row, column)
        cpu.pick_a_spot()
        cpu.check_spot()
        board.check_game()
        #    board.draw_board()
        print("\n")
        os.system("cls")


if __name__ == "__main__":
    main()
