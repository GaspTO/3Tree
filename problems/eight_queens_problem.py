import numpy as np
from .problem import Problem
from typing import Any, List, Tuple


class EightQueensProblem(Problem):
    """Defines the 8-queens problem, where the goal is to place 8 queens on a chessboard 
    so that no two queens threaten each other.

    This implementation assumes that queens are placed one per row, starting from the 
    topmost row and moving downwards sequentially. Each action places a queen in the 
    next available row, reducing the search space by automatically satisfying the 
    unique row constraint.
    """

    class State:
        """Represents a board configuration in the 8-queens problem, ensuring queens are 
        placed sequentially, one per row, without conflicts.

        This class maintains a chessboard of a given dimension, where queens are represented
        as marked positions on the board. It enforces the following rules (when strict mode is enabled):
        
        - Queens must be placed in consecutive rows without any skipped rows.
        - No two queens can be in the same row, column, or diagonal.
        """

        def __init__(self, board_dimension: int = 8, queens_positions: List[int] = None, strict=True):
            """Initialize the board as a numpy array with given queen positions marked by 1s,
            ensuring that all placements are valid and conflict-free.
            """
            self.board_dimension = board_dimension
            self.board = np.zeros((board_dimension, board_dimension), dtype=int)  # 0s represent empty squares
            self.queens_positions = queens_positions if queens_positions is not None else []

            # Validation: Ensure no more queens than the board dimension
            if strict:
                if len(self.queens_positions) > board_dimension:
                    raise ValueError("Invalid state: More queens placed than the board dimension allows.")
                
            # Place queens on the board without initial validation
            for row, col in enumerate(self.queens_positions):
                self.board[row, col] = 1

            # Perform separate checks for rows, columns, and diagonals, with specific error messages
            if strict:
                if self.check_columns(self.board):
                    raise ValueError("Invalid state: Conflict detected in a column configuration.")
                if self.check_main_diagonals(self.board):
                    raise ValueError("Invalid state: Conflict detected in a main diagonal.")
                if self.check_anti_diagonals(self.board):
                    raise ValueError("Invalid state: Conflict detected in an anti-diagonal.")

        @staticmethod
        def check_columns(board: np.ndarray) -> bool:
            col_sums = np.sum(board, axis=0)
            return np.any(col_sums > 1)

        @staticmethod
        def check_main_diagonals(board: np.ndarray) -> bool:
            for offset in range(-board.shape[0] + 1, board.shape[1]):
                if np.sum(np.diagonal(board, offset=offset)) > 1:
                    return True
            return False

        @staticmethod
        def check_anti_diagonals(board: np.ndarray) -> bool:
            flipped_board = np.fliplr(board)
            for offset in range(-flipped_board.shape[0] + 1, flipped_board.shape[1]):
                if np.sum(np.diagonal(flipped_board, offset=offset)) > 1:
                    return True
            return False
        
        def __repr__(self):
            return f"State(board=\n{self.board})"

    
    def __init__(self, board_dimension: int = 8):
        """Initialize the 8-queens problem with a specified board dimension and an empty initial state."""
        self.board_dimension = board_dimension
        self.initial_state = self.State(board_dimension=board_dimension)


    def is_goal(self, state: State) -> bool:
        """Check if the state has the correct number of queens.
        There is no need to verify the validity of the state, as it is ensured by the State class."""
        return len(state.queens_positions) == self.board_dimension 
        

    def get_actions(self, state: State) -> List[int]: 
        """Return a list of valid column positions for the next queen in the next row.

        Assumes that queens are placed row by row. The next queen will be placed in 
        the row equal to the number of queens currently on the board.
        """
        next_row = len(state.queens_positions)  # Row to place the next queen
        valid_columns = [
            col for col in range(self.board_dimension) 
            if self._is_safe(state, next_row, col)
        ]
        return valid_columns
    
    def _is_safe(self, state: State, row: int, col: int) -> bool:
            """Check if placing a queen at (row, col) does not threaten existing queens."""
            for r, c in enumerate(state.queens_positions):
                if c == col or abs(r - row) == abs(c - col):  # Same column or diagonal
                    return False
            return True


    def get_result(self, state: State, action: int) -> Tuple[State, float]:
        """Return a new state with a queen added in the next row and specified column, with a cost of 1."""
                     
        # Create a new state with the updated queen positions
        new_positions = state.queens_positions + [action]
        next_state = self.State(self.board_dimension, new_positions)
        return next_state, 1.0  # Return the new state and a cost of 1


    def get_initial_state(self) -> State:
        """Return the initial state, which is an empty board for the 8-queens problem."""
        return self.initial_state
    





if __name__ == "__main__":
    problem = EightQueensProblem(4)
    initial_state = problem.get_initial_state()
    print(initial_state)
    print(problem.is_goal(initial_state))