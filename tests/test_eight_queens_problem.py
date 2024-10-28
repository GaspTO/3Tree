import unittest
from problems.eight_queens_problem import EightQueensProblem

class TestEightQueensProblem(unittest.TestCase):
    SOLUTION = [3,6,2,7,1,4,0,5]

    def test_initial_state(self):
        """Test the initial state creation of the EightQueensProblem."""
        problem = EightQueensProblem(board_dimension=8)
        initial_state = problem.get_initial_state()
        
        self.assertEqual(len(initial_state.queens_positions), 0)
        self.assertEqual(initial_state.board_dimension, 8)
        self.assertEqual(initial_state.board.shape, (8, 8), "Board dimensions should match the specified board dimension")
        self.assertFalse(any(initial_state.board.flatten()), "Board should be empty initially")


    def test_is_goal(self):
        """Test is_goal to ensure it only returns True for the complete solution state."""
        problem = EightQueensProblem(board_dimension=8)

        # Iterate over progressively larger partial solutions
        for i in range(len(self.SOLUTION)+1):
            partial_solution = self.SOLUTION[:i]
            state = problem.State(board_dimension=8, queens_positions=partial_solution, strict=True)
            if i < len(self.SOLUTION):
                # Expect False for incomplete solutions
                self.assertFalse(problem.is_goal(state), f"is_goal should return False for partial solution {partial_solution}")
            else:
                # Expect True for the complete solution
                self.assertTrue(problem.is_goal(state), "is_goal should return True for the complete solution")


    def test_invalid_state_initialization(self):
        """Test state initialization with conflicting queens in strict mode, checking row, column, and diagonal conflicts."""

        # Column conflict
        queens_positions_column = [0,0]  # Same column
        with self.assertRaises(ValueError, msg="Invalid state: Conflict detected in a column configuration."):
            EightQueensProblem.State(board_dimension=8, queens_positions=queens_positions_column, strict=True)

        # Main diagonal conflict
        queens_positions_main_diag = [0,1]  # Same main diagonal
        with self.assertRaises(ValueError, msg="Invalid state: Conflict detected in a main diagonal."):
            EightQueensProblem.State(board_dimension=8, queens_positions=queens_positions_main_diag, strict=True)

        # Anti-diagonal conflict
        queens_positions_anti_diag = [1,0]  # Same anti-diagonal
        with self.assertRaises(ValueError, msg="Invalid state: Conflict detected in an anti-diagonal."):
            EightQueensProblem.State(board_dimension=8, queens_positions=queens_positions_anti_diag, strict=True)


    def test_get_actions(self):
        """Test get_actions to return valid columns for the next queen placement."""
        problem = EightQueensProblem(board_dimension=8)
        
        # Arrange: A partially completed state with queens in non-conflicting positions
        queens_positions = [3,6,2]
        state = problem.State(board_dimension=8, queens_positions=queens_positions)
        
        # Act: Get actions for the next queen placement
        actions = problem.get_actions(state)

        # Assert: Verify that the returned actions are valid
        correct_actions = [5,7]
        self.assertTrue(set(actions) == set(correct_actions))


    def test_get_result(self):
        """Test get_result to ensure it produces a new state with an additional queen."""
        problem = EightQueensProblem(board_dimension=8)
        initial_state = problem.get_initial_state()
        
        # Act: Place the first queen in column 0 of row 0
        next_state, cost = problem.get_result(initial_state, action=0)
        
        # Assert: Verify that the new state has the queen in the correct position
        self.assertEqual(cost, 1.0)
        self.assertEqual(len(next_state.queens_positions), 1)
        self.assertEqual(next_state.queens_positions[0], 0)
        self.assertEqual(next_state.board[0, 0], 1)

    def test_strict_flag(self):
        """Test state initialization with strict=False (should not raise errors for conflicts)."""
        queens_positions = [0,1]  # Conflict in the same row
        try:
            state = EightQueensProblem.State(board_dimension=8, queens_positions=queens_positions, strict=False)
            self.assertTrue(True, "State initialized without error in non-strict mode")
        except ValueError:
            self.fail("State should not raise ValueError in non-strict mode")


if __name__ == '__main__':
    unittest.main()
