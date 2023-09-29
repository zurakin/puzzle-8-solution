import random

from solver import AStar


def in_bounds(i, j):
    return 0 <= i <= 2 and 0 <= j <= 2


class Model:
    def __init__(self):
        self.grid = [[1, 2, 3], [4, 5, 6], [7, None, 8]]
        self.counter = 0
        self.solver = AStar()

    def move(self, tile_x, tile_y):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for d in directions:
            x, y = tile_x + d[0], tile_y + d[1]
            if in_bounds(x, y) and self.grid[y][x] is None:
                self.grid[y][x] = self.grid[tile_y][tile_x]
                self.grid[tile_y][tile_x] = None
                self.counter += 1
                break
        if self.is_complete():
            self.grid[2][2] = 9

    def __move_direction(self, direction):
        none_y, none_x = None, None
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] is None:
                    none_y, none_x = i, j
                    break
        if none_y is None: return False
        dy, dx = direction
        tile_y, tile_x = none_y + dy, none_x + dx
        if not in_bounds(tile_y, tile_x): return False

        self.grid[none_y][none_x] = self.grid[tile_y][tile_x]
        self.grid[tile_y][tile_x] = None
        if self.is_complete():
            self.grid[2][2] = 9

    def move_up(self):
        self.__move_direction((1, 0))

    def move_down(self):
        self.__move_direction((-1, 0))

    def move_right(self):
        self.__move_direction((0, -1))

    def move_left(self):
        self.__move_direction((0, 1))

    def is_complete(self):
        for i in range(3):
            for j in range(3):
                val = 3 * i + j + 1
                if val != 9 and self.grid[i][j] != val:
                    return False
        return True

    def random_move(self):
        empty_tile_x, empty_tile_y = None, None
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] is None or self.grid[i][j] == 9:
                    empty_tile_y, empty_tile_x = i, j
                    break
        directions = [(empty_tile_y + d[0], empty_tile_x + d[1]) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        possible_directions = [d for d in directions if in_bounds(*d)]
        rand_dir = random.choice(possible_directions)
        self.grid[empty_tile_y][empty_tile_x] = self.grid[rand_dir[0]][rand_dir[1]]
        self.grid[rand_dir[0]][rand_dir[1]] = None

    def shuffle(self, iters=100):
        for _ in range(iters):
            self.random_move()

    def get_grid(self):
        return self.grid

    def get_counter(self):
        return self.counter

    def help(self):
        return self.solver.solve(self.grid)
