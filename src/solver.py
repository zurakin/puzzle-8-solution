from abc import ABC, abstractmethod
from priority_queue import PriorityQueue


class Solver(ABC):
    @abstractmethod
    def solve(self, initial_grid):
        pass


def init_tiles_final_positions():
    positions = {}
    for i in range(3):
        for j in range(3):
            positions[i * 3 + j + 1] = (i, j)
    return positions


class AStar(Solver):
    tiles_final_positions = init_tiles_final_positions()

    def solve(self, initial_grid):
        initial_grid = self.to_tuple(initial_grid)
        pq = PriorityQueue()
        costs_matrix = {initial_grid: 0}
        antecedents_matrix = {initial_grid: None}
        pq.push(initial_grid, self.heuristic_evaluation(initial_grid))
        final_grid = None
        while not pq.is_empty():
            current_grid = pq.pop()
            current_cost = costs_matrix[current_grid]
            if self.is_solution(current_grid):
                final_grid = current_grid
                break
            neighbors = self.get_neighbors(current_grid)
            for n in neighbors:
                neighbor_previous_cost = costs_matrix.get(n, float('inf'))
                if (current_cost + 1) < neighbor_previous_cost:
                    costs_matrix[n] = current_cost + 1
                    antecedents_matrix[n] = current_grid
                    pq.push(n, current_cost + 1 + self.heuristic_evaluation(n))

        # backtrack from final_grid to find the path
        path = []
        node = final_grid
        while node is not None:
            path.append(node)
            node = antecedents_matrix[node]

        actions_list = [self.none_position(g) for g in path[::-1][1:]]
        return actions_list

    @staticmethod
    def is_solution(grid):
        for i in range(3):
            for j in range(3):
                val = 3 * i + j + 1
                if val != 9 and grid[i][j] != val:
                    return False
        return True

    @staticmethod
    def get_neighbors(grid):
        none_y, none_x = AStar.none_position(grid)
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        neighbors = []
        for d in directions:
            y, x = none_y + d[0], none_x + d[1]
            if 0 <= x <= 2 and 0 <= y <= 2:
                neighbor = AStar.to_list(grid)
                neighbor[none_y][none_x] = neighbor[y][x]
                neighbor[y][x] = None
                neighbors.append(AStar.to_tuple(neighbor))
        return neighbors

    @staticmethod
    def to_list(grid):
        return [list(g) for g in grid]

    @staticmethod
    def to_tuple(grid):
        return tuple(tuple(g) for g in grid)

    @staticmethod
    def none_position(grid):
        for i in range(3):
            for j in range(3):
                if grid[i][j] is None:
                    return i, j
        return None

    def heuristic_evaluation(self, grid):
        h = 0
        for y in range(3):
            for x in range(3):
                value = grid[y][x]
                if value is None:
                    continue
                final_y, final_x = self.tiles_final_positions[value]
                h += abs(y - final_y) + abs(x - final_x)
        return h
