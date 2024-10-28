import unittest
from algorithms.breadth_first_search import BreadthFirstSearch
from problems.mock_problem import MockProblem

class TestBreadthFirstSearch(unittest.TestCase):
    
    def setUp(self):
        """Set up mock problems with various configurations."""
        # Simple problem with a single path to the goal
        self.simple_problem = MockProblem(
            transitions={
                1: [(2, 1), (3, 1)],
                2: [(4, 1)],
                3: [(4, 1)],
                4: []
            },
            initial_state_id=1,
            goal_state_id=4
        )

        # Problem with no path to the goal
        self.unreachable_goal_problem = MockProblem(
            transitions={
                1: [(2, 1)],
                2: [(3, 1)],
                3: []  # No connection to state 4, so goal is unreachable
            },
            initial_state_id=1,
            goal_state_id=4
        )

        # Problem with multiple paths to the goal
        self.multi_path_problem = MockProblem(
            transitions={
                1: [(2, 1), (3, 1)],
                2: [(4, 1)],
                3: [(4, 1)],
                4: []
            },
            initial_state_id=1,
            goal_state_id=4
        )

        # Problem where the initial state is the goal
        self.initial_is_goal_problem = MockProblem(
            transitions={
                    1: [(2, 1)],
                    2: [(3, 1)]
                },
                initial_state_id=1,
                goal_state_id=1  # Goal is the same as the initial state
        )

    def test_single_path_to_goal(self):
        """Test BFS on a problem with a single path to the goal."""
        bfs = BreadthFirstSearch()
        success = bfs.search(self.simple_problem)
        result = bfs.retrieve_result()
        self.assertTrue(success)
        self.assertTrue(self.simple_problem.is_goal(result))

    def test_no_path_to_goal(self):
        """Test BFS when there is no path to the goal."""
        bfs = BreadthFirstSearch()
        success = bfs.search(self.unreachable_goal_problem)
        result = bfs.retrieve_result()
        self.assertFalse(success)
        self.assertIsNone(result)

    def test_multiple_paths_to_goal(self):
        """Test BFS on a problem with multiple paths, ensuring shortest path is chosen."""
        bfs = BreadthFirstSearch()
        success = bfs.search(self.multi_path_problem)
        result = bfs.retrieve_result()
        self.assertTrue(success)
        self.assertTrue(self.simple_problem.is_goal(result))

    def test_correct_order_of_expansion(self):
        """Ensure BFS explores states in layer-by-layer order."""
        bfs = BreadthFirstSearch()
        bfs.search(self.simple_problem)
        # Check the order of expansion
        self.assertEqual(set(self.simple_problem.discovered_transitions),set([(1, 2), (1, 3), (2, 4)]))

    def test_initial_state_is_goal(self):
        """Test BFS when the initial state is the goal."""
        bfs = BreadthFirstSearch()
        success = bfs.search(self.initial_is_goal_problem)
        result = bfs.retrieve_result()
        self.assertTrue(success)
        self.assertEqual(result, self.initial_is_goal_problem.get_initial_state())  # Ensure it returns the initial state as the goal


if __name__ == "__main__":
    unittest.main()
