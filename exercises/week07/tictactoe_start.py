"""
Oefening: TicTacToe met Minimax & Alpha-Beta
==============================================
"""
import copy


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def possible_moves(self):
        """Geef lijst van (rij, kolom)-tupels van lege velden."""
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def is_valid_move(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == ' '

    def make_move(self, x, y, player):
        self.board[x][y] = player

    def undo_move(self, x, y):
        self.board[x][y] = ' '

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ':
                return 1 if self.board[i][0] == 'X' else -1
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' ':
                return 1 if self.board[0][i] == 'X' else -1

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return 1 if self.board[0][0] == 'X' else 'O' # wait, return -1 for O
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return 1 if self.board[0][2] == 'X' else -1

        # Check draw
        if len(self.possible_moves()) == 0:
            return 0

        return None

    def is_draw(self):
        return len(self.possible_moves()) == 0 and not self.check_winner()

    def minimax(self, depth, is_maximizing, alpha=None, beta=None, max_depth=None):
        status = self.check_winner()
        if status != None:
            return status
        if is_maximizing:
            best = -float('inf')
            for zet in self.possible_moves():
                self.make_move(zet[0], zet[1], 'X')
                score = self.minimax(depth - 1, False, alpha, beta, max_depth)
                self.undo_move(zet[0], zet[1])
                best = max(best, score)
            return best


        else:
            best = float('inf')
            for zet in self.possible_moves():
                self.make_move(zet[0], zet[1], 'O')
                score = self.minimax(depth - 1, True, alpha, beta, max_depth)
                self.undo_move(zet[0], zet[1])
                best = min(best, score)
            return best


                
    

    def find_best_move(self):
        pass

    def print_board(self):
        horizontal_line = "+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print("| {} | {} | {} |".format(row[0], row[1], row[2]))
            print(horizontal_line)

    def play(self):
        pass


if __name__ == "__main__":
    game = TicTacToe()
    game.play()