from .problem import Problem
from typing import Any, List, Tuple

class MockProblem(Problem):
    """A mock problem to simulate states and actions for BFS testing."""

    class State:
        """Represents a simplified state, identified by a unique integer ID."""
        def __init__(self, id: int):
            self.id = id

        def __hash__(self):
            return hash(self.id)

        def __eq__(self, other):
            return isinstance(other, MockProblem.State) and self.id == other.id

        def __repr__(self):
            return f"State({self.id})"

    def __init__(self, transitions, initial_state_id, goal_state_id):
        """Initialize with a dictionary of transitions, initial, and goal state IDs."""
        self.transitions = transitions
        self.initial_state = self.State(initial_state_id)
        self.goal_state = self.State(goal_state_id)
        self.discovered_transitions = []

    def get_initial_state(self) -> State:
        return self.initial_state

    def is_goal(self, state: State) -> bool:
        return state == self.goal_state

    def get_actions(self, state: State) -> List[int]:
        """Return a list of neighbor state IDs."""
        return [neighbor for neighbor, _ in self.transitions.get(state.id, [])]

    def get_result(self, state: State, action: Any) -> Tuple[State, float]:
        """Return the resulting state from an action and its cost."""
        self.discovered_transitions.append((state.id, action)) # Track transitions

        for neighbor, cost in self.transitions.get(state.id, []):
            if neighbor == action:
                return self.State(neighbor), cost
        raise ValueError("Invalid action for the given state")
