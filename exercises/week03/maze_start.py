"""
Oefening 3: Maze met DFS
=========================
Implementeer DFS om een weg door het maze te vinden.
"""
import numpy as np


class Maze:
    def __init__(self, size, start, end, walls):
        self.size = size
        self.start = start
        self.end = end
        self.maze = np.zeros(size, dtype=str)
        self.maze[:, :] = '.'
        self.maze[start] = 'S'
        self.maze[end] = 'E'
        for wall in walls:
            self.maze[wall] = '#'

    def valid_moves(self, current):
        # TODO: geef lijst van (rij,kolom)-coördinaten die geldig zijn
        possible_moves = []
        row, col = current

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dir_row, dir_col in moves:
            new_row, new_col = row + dir_row, col + dir_col
            if 0 <= new_row < self.size[0] and 0 <= new_col < self.size[1]:
                if self.maze[new_row, new_col] != "#":
                    possible_moves.append((new_row, new_col))

        return possible_moves
        
    def extract_path(self, stack):
        # TODO: haal het pad uit de stack van start tot end
        pad = []

        for positie in stack:
            pad.append(positie)
            if positie == self.end:
                break

        return pad

    def print_maze(self):
        for row in self.maze:
            print(' '.join(row))


def find_path(maze):
    # TODO: implementeer DFS met een stack
    stack = [maze.start]
    parent = {maze.start: None}
    visited = {maze.start}

    while stack:
        current = stack.pop()
        if current == maze.end:
            pad = []
            stap = current
            while stap is not None:
                pad.append(stap)
                stap = parent[stap]
            pad.reverse()
            return (pad, len(pad) - 1)

        for buur in maze.valid_moves(current):
            if buur not in visited:
                visited.add(buur)
                parent[buur] = current
                stack.append(buur)

    return (None, 0)


if __name__ == "__main__":
    maze_size = (10, 10)
    start_point = (0, 0)
    end_point = (9, 9)
    walls = [(2, 1), (2, 2), (2, 3), (4, 6), (6, 6), (7, 6), (8, 6),
             (4, 7), (4, 8), (2, 2), (5, 2), (6, 2), (4, 2), (3, 2),
             (8, 0), (9, 6), (1, 8), (2, 8), (6, 9), (7, 9),
             (3, 6), (3, 7), (4, 1), (5, 1)]

    my_maze = Maze(maze_size, start_point, end_point, walls)
    pad, stappen = find_path(my_maze)

    my_maze.print_maze()
    print("Pad:", pad)
    print("Stappen:", stappen)