WINNING_COMBOS = [
    [(0,0),(0,1),(0,2)],
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],
    [(0,0),(1,1),(2,2)],
    [(0,2),(1,1),(2,0)],
    [(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)],
]

class TicTacToe:

    def __init__(self):
        self.board = ([[' ',' ',' '],
                       [' ',' ',' '],
                       [' ',' ',' ']])
        self.players = ['X', 'O']
        self.turn = 0
        self.row_dict = {'top': 0, 'middle': 1, 'bottom': 2}
        self.col_dict = {'left': 0, 'middle': 1, 'right': 2}
        self.used_rows = []
        self.game_on = True
        self.print_board()

    def move(self):
        row = None
        col = None
        while row == None:
            row = self.get_row()
        while col == None:
            col = self.get_col()
        if (row, col) in self.used_rows:
            print("Position has already been played, please pick another.")
            self.move()
        else:
            if self.turn % 2 == 0:
                self.board[row][col] = self.players[0]
            else:
                self.board[row][col] = self.players[1]
            self.turn += 1
            self.used_rows.append((row, col))
            self.print_board()
            self.is_game_over()

    def get_row(self):
        input_row = input("Please pick a row: top, middle, or bottom \n").lower()
        try:
            row = self.row_dict[input_row]
        except KeyError:
            print("Please enter a valid row")
            return None
        return row

    def get_col(self):
        input_col = input("Please pick a column: left, middle, or right \n").lower()
        try:
            col = self.col_dict[input_col]
        except KeyError:
            print("Please enter a valid column")
            return None
        return col
        
    def print_board(self):
        print(f'{self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}\n ------------\n{self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}\n ------------\n{self.board[2][0]}  |  {self.board[2][1]}  |  {self.board[2][2]}\n')

    def is_game_over(self):
        if self.turn == 9:
            print('Tie!')
            self.game_on = False
        elif self.turn < 5:
            return
        else:
            for combo in WINNING_COMBOS:
                if self.board[combo[0][0]][combo[0][1]] == self.board[combo[1][0]][combo[1][1]] == self.board[combo[2][0]][combo[2][1]]:
                    if self.board[combo[0][0]][combo[0][1]] != ' ':
                        print(f'{self.board[combo[0][0]][combo[0][1]]} wins')
                        self.game_on = False
                    else:
                        continue


game = TicTacToe()
while game.game_on == True:
    game.move()
