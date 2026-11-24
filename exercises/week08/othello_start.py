"""
Oefening: Mini Othello met Evaluatiefunctie & Minimax
=======================================================
"""
import random


class Othello:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        self.initialize_board()
        self.player = 'X'

    def print_board(self):
        horizontal_line = "+---+---+---+---+---+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print("| {} | {} | {} | {} | {} | {} | {} | {} |".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            print(horizontal_line)

    def initialize_board(self):
        self.board[3][3] = self.board[4][4] = "O"
        self.board[3][4] = self.board[4][3] = "X"

    def is_valid_move(self, row, col, player):
        if self.board[row][col] != " ":
            return False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row, col
            r += dr
            c += dc
            if not (0 <= r < 8) or not (0 <= c < 8):
                continue
            if self.board[r][c] == self.opponent():
                r += dr
                c += dc
                while (0 <= r < 8) and (0 <= c < 8):
                    if self.board[r][c] == " ":
                        break
                    if self.board[r][c] == player:
                        return True
                    r += dr
                    c += dc
        return False

    def opponent(self):
        return "O" if self.player == "X" else "X"

    def change_player(self):
        self.player = self.opponent()

    def make_move(self, row, col, player):
        if self.is_valid_move(row, col, player):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            self.board[row][col] = player
            for dr, dc in directions:
                r, c = row, col
                r += dr
                c += dc
                while (0 <= r < 8) and (0 <= c < 8):
                    if self.board[r][c] == " ":
                        break
                    if self.board[r][c] == player:
                        while (r != row) or (c != col):
                            r -= dr
                            c -= dc
                            self.board[r][c] = player
                        break
                    r += dr
                    c += dc

    def count_pieces(self):
        x_count = sum(row.count("X") for row in self.board)
        o_count = sum(row.count("O") for row in self.board)
        return x_count, o_count

    def valid_moves(self, player):
        return [(r, c) for r in range(8) for c in range(8)
                if self.is_valid_move(r, c, player)]

    def random_move(self):
        # TODO: kies een geldige zet
        moves = self.valid_moves(self.player)
        if not moves:
            return None
        random.shuffle(moves)
        return moves[0]

    def evaluate(self, player):
        # TODO: evaluatiefunctie (bijv. stukken + mobiliteit)
        x_count, o_count = self.count_pieces()
        if player == 'X':
            stone_diff = x_count - o_count
        else:
            stone_diff = o_count - x_count
        return stone_diff

    def minimax(self, depth, is_maximizing, player):
        # TODO: implementeer minimax (simuleer zetten op een kopie)
        valid_moves = self.valid_moves(player)
        if depth == 0 or not valid_moves:
            return self.evaluate(player), None
        if is_maximizing:
            max_eval = float('-inf')
            best_action = None
            for move in valid_moves:
                new_game = self.copy()
                new_game.make_move(move[0], move[1], self.player)
                new_game.change_player()
                eval, _ = new_game.minimax(depth-1,False, player)
                if eval > max_eval:
                    max_eval = eval
                    best_action = move
            return max_eval, best_action
        else:
            min_eval = float('inf')
            best_action = None
            for move in valid_moves:
                new_game = self.copy()
                new_game.make_move(move[0], move[1], self.player)
                new_game.change_player()

                eval, _ = new_game.minimax(depth-1, True, player)
                if eval < min_eval:
                    min_eval = eval
                    best_action = move
            return min_eval, best_action
            


    def best_move(self, depth=3):
        # TODO: kies de beste zet via minimax
        _, move = self.minimax(depth, True, self.player)
        return move 

    def copy(self):
            """Maakt een diepe kopie van de huidige spelstaat."""
            new_game = Othello()
            new_game.board = [row[:] for row in self.board]  # Kopieer de 2D-lijst
            new_game.player = self.player                    # Neem de huidige speler over
            return new_game

def play():
    game = Othello()

    while True:
        game.print_board()
        x_count, o_count = game.count_pieces()
        print(f"X: {x_count}, O: {o_count}")

        if not game.valid_moves(game.player):
            print("Geen geldige zetten meer.")
            game.change_player()
            if not game.valid_moves(game.player):
                print("Game over.")
                break

        if game.player == 'X':
            # TODO: laat de computer spelen met best_move()
            print("Computer ('X') denkt na...")
            move = game.best_move(depth=3)
            if move:
                print(f"Computer kiest zet: {move}")
                game.make_move(move[0], move[1], game.player)
        else:
            # TODO: menselijke input
            print("Jij bent aan de beurt ('O').")
            valid = game.valid_moves(game.player)
            print(f"Geldige zetten (rij, kolom): {valid}")
            while True:
                try:
                    r = int(input("Geef rij (0-7): "))
                    c = int(input("Geef kolom (0-7): "))
                    if (r, c) in valid:
                        game.make_move(r, c, game.player)
                        break
                    else:
                        print("Ongeldige zet. Kies een geldige zet uit de lijst.")
                except ValueError:
                    print("Voer een geldig geheel getal in tussen 0 en 7.")

        game.change_player()


if __name__ == "__main__":
    play()