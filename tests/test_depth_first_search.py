import unittest
from algorithms import DepthFirstSearch
from problems.mock_problem import MockProblem
from basic_test_problem import BasicTestProblem
    
class TestDepthFirstSearch(BasicTestProblem):
    
    def setUp(self):
        super().setUp()
        self.search = DepthFirstSearch()

    def test_single_path_to_goal(self):
        """Test BFS on a problem with a single path to the goal."""
        success = self.search.search(self.simple_problem)
        result = self.search.retrieve_result()
        self.assertTrue(success)
        self.assertTrue(self.simple_problem.is_goal(result))
        self.assertEqual(self.search.get_nodes_retrieved(), 9)
        self.assertEqual(self.simple_problem.discovered_transitions,
                         [(1,2), (1,3), (1,4), (2,5), (2,6), (5,11), 
                          (5,12), (6,13), (6,14), (3,7), (3,8)])

    def test_no_path_to_goal(self):
        """Test BFS when there is no path to the goal."""
        success = self.search.search(self.unreachable_goal_problem)
        result = self.search.retrieve_result()
        self.assertFalse(success)
        self.assertIsNone(result)
        self.assertEqual(self.search.get_nodes_retrieved(), 14)
        self.assertEqual(self.unreachable_goal_problem.discovered_transitions,
                         [(1,2), (1,3), (1,4), (2,5), (2,6), (5,11), (5,12),
                          (6,13), (6,14), (3,7), (3,8), (4,9), (4,10)])

    def test_multiple_paths_to_goal(self):
        """Test BFS on a problem with multiple paths, ensuring shortest path is chosen."""
        success = self.search.search(self.multi_path_problem)
        result = self.search.retrieve_result()
        self.assertTrue(success)
        self.assertTrue(self.multi_path_problem.is_goal(result))
        self.assertEqual(self.search.get_nodes_retrieved(), 9)
        self.assertEqual(self.multi_path_problem.discovered_transitions,
                         [(1,2), (1,3), (1,4), (2,5), (2,6), (5,11), 
                          (5,12), (6,13), (6,14), (3,7), (3,8)])

    def test_initial_state_is_goal(self):
        """Test BFS when the initial state is the goal."""
        success = self.search.search(self.initial_is_goal_problem)
        result = self.search.retrieve_result()
        self.assertTrue(success)
        self.assertTrue(self.initial_is_goal_problem.is_goal(result))
        self.assertEqual(result, self.initial_is_goal_problem.get_initial_state())  # Ensure it returns the initial state as the goal
        self.assertEqual(self.search.get_nodes_retrieved(), 0)
        self.assertEqual(self.initial_is_goal_problem.discovered_transitions,[])

if __name__ == "__main__":
    unittest.main()
