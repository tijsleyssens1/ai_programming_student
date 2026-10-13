"""
Oefening 2: Sliding Puzzle (8-puzzle)
======================================
Implementeer de sliding puzzle en los hem op met BFS/DFS.
"""
import numpy as np
from collections import deque


class SlidingPuzzle:
    GRIDSIZE = 3
    EMPTY = 0

    GOAL = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    def __init__(self, game):
        self.Game = np.array(game)

    def possible_new_configurations(self):
        # TODO: geef alle nieuwe configuraties door het lege vakje te verschuiven
        possible_configurations = []
        row, col = self.locate_empty()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dir_row, dir_col in moves:
            new_row, new_col = row + dir_row, col + dir_col
            if 0 <= new_row < self.GRIDSIZE and 0 <= new_col < self.GRIDSIZE:
                new_configuration = self.duplicate()
                new_configuration.Game[row, col] = new_configuration.Game[new_row, new_col]
                new_configuration.Game[new_row, new_col] = self.EMPTY

                possible_configurations.append(new_configuration)
        
        return possible_configurations

    def locate_empty(self):
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return (row, col)
        raise Exception("Geen leeg vakje!")

    def manhattan_distance(self):
        # TODO: bereken de Manhattan-afstand tot de goal-configuratie
        cost = 0
        for i in range(9):
            goal_array = np.array(self.GOAL)
            row, col = np.where(self.Game == i)
            goal_row, goal_col = np.where(goal_array == i)
            cost += abs(goal_row[0] - row[0]) + abs(goal_col[0] - col[0])
        return cost

    def is_goal(self):
        return np.array_equal(self.Game, self.GOAL)

    def duplicate(self):
        return SlidingPuzzle([[self.Game[r][c] for c in range(self.GRIDSIZE)] for r in range(self.GRIDSIZE)])

    def log(self):
        print("---")
        for row in self.Game:
            print(", ".join(str(int(x)) for x in row))
        print("---")


def solve_puzzle(start_puzzle):
    # TODO: los de puzzel op met BFS
    if start_puzzle.is_goal():
        return[start_puzzle]

    queu = deque([(start_puzzle, [start_puzzle])])
    visited = {start_puzzle}

    while queu:
        current_puzzle, path = queu.popleft()

        if current_puzzle.is_goal():
            return path

        for next_puzzle in current_puzzle.possible_new_configurations():
            if next_puzzle not in visited:
                visited.add(next_puzzle)
                queu.append((next_puzzle, path + [next_puzzle]))

    return None
    
    


if __name__ == "__main__":
    game = [
        [0, 6, 3],
        [4, 5, 1],
        [7, 8, 2]
    ]
    puzzle = SlidingPuzzle(game)
    print("Startconfiguratie:")
    puzzle.log()

    oplossing = solve_puzzle(puzzle)
    # print("Oplossing:", oplossing)    
    if oplossing:
        print(f"Oplossing gevonden in {len(oplossing)} stappen!\n")
        for i, stap in enumerate(oplossing):
            print(f"Stap {i}:")
            stap.log()
    else:
        print("Geen oplossing gevonden.")