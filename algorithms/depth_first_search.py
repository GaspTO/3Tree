from .search_algorithm import SearchAlgorithm
from collections import deque

class DepthFirstSearch(SearchAlgorithm):
    """Breadth-First Search algorithm, exploring nodes layer-by-layer from the start state."""


    def initialize(self, problem):
        """Set up search structures based on the specific problem instance."""
        self.problem = problem  
        self.initial_state = self.problem.get_initial_state()
        self.queue = deque([self.initial_state])   
        self.visited = set()
        self.result = None
        if self.problem.is_goal(self.initial_state):  # Check if the initial state is the goal
            self.result = self.initial_state  # Set the result directly if goal is found

    def is_search_complete(self):
        """Check if the search queue is empty or if a result has been found."""
        return not self.queue or self.result is not None

    def next_node(self):
        """Pop the next node from the queue for exploration."""
        super().next_node()
        self.current_state = self.queue.pop()  # Set current state by removing from the back of the queue

    def evaluate_node(self):
        """Evaluate if the current state meets the goal conditions (now only for non-goal states)."""
        super().evaluate_node()
        # This method can remain empty or be skipped, as goal-checking occurs in `expand_node`.

    def expand_node(self):
        """Generate child states and add them to the queue if they haven't been visited."""
        super().expand_node()
        add_to_queue = []
        for action in self.problem.get_actions(self.current_state):
            new_state, _ = self.problem.get_result(self.current_state, action)
            if self.problem.is_goal(new_state):  # Check if the child is the goal
                self.result = new_state
                return  # Stop expanding further if goal is found
            if new_state not in self.visited:
                self.visited.add(new_state)
                add_to_queue.insert(0, new_state) # First state discovered, will be first state retrueved
        self.queue.extend(add_to_queue)

    def retrieve_result(self):
        """Return the final state or result based on the search completion."""
        return self.result
