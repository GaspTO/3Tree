from abc import ABC, abstractmethod
from typing import Any, List, Tuple


class Problem(ABC):
    """
    Defines the structure of a search problem with dynamic initial states, 
    transition-based costs, and an abstract state representation.
    
    Each instance of `Problem` represents a particular instance of a problem, 
    including its own initial state. Unlike a generic problem template, 
    a `Problem` instance may have its starting conditions set dynamically 
    (e.g., randomly) or predefined within the class. This allows different 
    problem instances, such as unique configurations of a puzzle, while 
    maintaining a consistent structure.

    A `Problem` defines:
    - `is_goal`: A method to check if a given state satisfies the goal conditions.
    - `get_actions`: A method that provides possible actions available from a given state.
    - `get_result`: A method that applies an action to a state and returns the resulting state 
                    and the cost associated with the transition.
    - `get_cost`: An optional method to calculate the cost of transitioning between states 
                  via a specified action, if not directly handled in `get_result`.
    - `get_initial_state`: A method to retrieve the initial state of the problem instance.

    The `State` inner class serves as a placeholder for defining the structure of 
    individual states. Subclasses should define this based on the specific 
    requirements of the problem domain.
    """

    class State:
        """Represents a state within the problem. This is a placeholder for problem-specific state implementations."""
        pass

    @abstractmethod
    def is_goal(self, state: State) -> bool:
        """Check if a given state meets the goal criteria."""
        pass

    @abstractmethod
    def get_actions(self, state: State) -> List[Any]:
        """Return possible actions from a given state."""
        pass

    @abstractmethod
    def get_result(self, state: State, action: Any) -> Tuple[State, float]:
        """Return the resulting state and cost from taking an action at the given state."""
        pass

    @abstractmethod
    def get_initial_state(self) -> State:
        """Return the initial state of the problem instance."""
        pass
