import unittest

from priority_queue import PriorityQueue
from solver import AStar


class Tests(unittest.TestCase):
    def test_priority_queue(self):
        pq = PriorityQueue()
        pq.push("Node 1", 1)
        pq.push("Node 2", 10)
        pq.push("Node 3", 3)

        self.assertEqual(pq.pop(), "Node 1")
        self.assertEqual(pq.pop(), "Node 3")
        self.assertEqual(pq.pop(), "Node 2")

        self.assertTrue(pq.is_empty())

    def test_priority_queue_heterogeneous_types(self):
        pq = PriorityQueue()
        pq.push(None, 1)
        pq.push(3, 1)
        pq.push("Node 3", 3)

        self.assertIn(pq.pop(), [None, 3])
        self.assertIn(pq.pop(), [None, 3])
        self.assertEqual(pq.pop(), "Node 3")
        self.assertTrue(pq.is_empty())

    def test_heuristic(self):
        solver = AStar()
        self.assertEqual(solver.heuristic_evaluation(((1, 2, None),
                                                      (4, 5, 3),
                                                      (7, 8, 6))), 2)
        self.assertEqual(solver.heuristic_evaluation(((1, None, 2),
                                                      (4, 5, 3),
                                                      (7, 8, 6))), 3)
        self.assertEqual(solver.heuristic_evaluation(((1, 2, 3),
                                                      (4, 5, None),
                                                      (7, 8, 6))), 1)
        self.assertEqual(solver.heuristic_evaluation(((1, 2, 3),
                                                      (4, 5, 6),
                                                      (7, 8, None))), 0)

    def test_none_positio(self):
        self.assertEqual(AStar.none_position(((1, 2, None),
                                              (4, 5, 3),
                                              (7, 8, 6))), (0, 2))
        self.assertEqual(AStar.none_position(((1, 2, 3),
                                              (4, 5, 6),
                                              (7, 8, 9))), None)
        self.assertEqual(AStar.none_position(((1, 2, 3),
                                              (4, 5, 6),
                                              (7, 8, None))), (2, 2))

    def test_is_solution(self):
        self.assertTrue(AStar.is_solution(((1, 2, 3),
                                           (4, 5, 6),
                                           (7, 8, 9))))
        self.assertTrue(AStar.is_solution(((1, 2, 3),
                                           (4, 5, 6),
                                           (7, 8, None))))
        self.assertFalse(AStar.is_solution(((1, 2, 3),
                                            (4, None, 6),
                                            (7, 8, 9))))

    def test_get_neighbors(self):
        self.assertEqual(AStar.get_neighbors(((1, 2, 3),
                                              (4, 5, 6),
                                              (7, 8, None))),
                         [((1, 2, 3), (4, 5, None), (7, 8, 6)), ((1, 2, 3), (4, 5, 6), (7, None, 8))])

    def test_astar_solver(self):
        grid = ((1, 2, None),
                (4, 5, 3),
                (7, 8, 6))
        solver = AStar()
        print(solver.solve(grid))
