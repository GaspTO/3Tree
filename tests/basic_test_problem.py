import unittest
from algorithms.breadth_first_search import BreadthFirstSearch
from problems.mock_problem import MockProblem

class BasicTestProblem(unittest.TestCase):
    
    def setUp(self):
        """Set up mock problems with various configurations."""
        # Simple problem with a single path to the goal
        self.simple_problem = MockProblem(
            transitions={
                1: [(2, 1), (3, 1), (4, 1)],
                2: [(5, 1), (6, 1)],
                3: [(7, 1), (8, 1)],
                4: [(9, 1), (10, 1)],
                5: [(11, 1), (12, 1)],
                6: [(13, 1), (14, 1)]
            },
            initial_state_id=1,
            goal_state_id=8
        )

        # Problem with no path to the goal
        self.unreachable_goal_problem = MockProblem(
            transitions={
                1: [(2, 1), (3, 1), (4, 1)],
                2: [(5, 1), (6, 1)],
                3: [(7, 1), (8, 1)],
                4: [(9, 1), (10, 1)],
                5: [(11, 1), (12, 1)],
                6: [(13, 1), (14, 1)]
            },
            initial_state_id=1,
            goal_state_id=15
        )

        # Problem with multiple paths to the goal
        self.multi_path_problem = MockProblem(
            transitions={
                1: [(2, 1), (3, 1), (4, 1)],
                2: [(5, 1), (6, 1)],
                3: [(7, 1), (8, 1)],
                4: [(9, 1), (8, 1)],
                5: [(11, 1), (12, 1)],
                6: [(13, 1), (14, 1)]
            },
            initial_state_id=1,
            goal_state_id=8
        )

        # Problem where the initial state is the goal
        self.initial_is_goal_problem = MockProblem(
            transitions={
                1: [(2, 1), (3, 1), (4, 1)],
                2: [(5, 1), (6, 1)],
                3: [(7, 1), (8, 1)],
                4: [(9, 1), (10, 1)],
                5: [(11, 1), (12, 1)],
                6: [(13, 1), (14, 1)]
            },
            initial_state_id=1,
            goal_state_id=1
        )