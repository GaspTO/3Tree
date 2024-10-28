from abc import ABC, abstractmethod

class SearchAlgorithm(ABC):
    """Abstract base class for search algorithms with generalized success evaluation."""

    def search(self, problem):
        """Template method for general search, handling both goal-based and reward-based searches."""
        self.initialize(problem)  # Reset any search-specific state
        while not self.is_search_complete():
            self.next_node()  # Sets self.current_node
            self.evaluate_node()  # Each subclass updates state or tracks the result as needed
            self.expand_node()
        self.finish()  # Final cleanup or logging after the search completes
        return self.retrieve_result() is not None

    @abstractmethod
    def retrieve_result(self):
        """Retrieve the final result node or state based on algorithm-specific criteria."""
        pass

    @abstractmethod
    def initialize(self):
        """Initialize or reset search-specific structures (e.g., queue, priority structures)."""
        pass

    @abstractmethod
    def is_search_complete(self):
        """Check if search should terminate (e.g., queue empty, max iterations, sufficient reward)."""
        pass

    @abstractmethod
    def next_node(self):
        """Set the next node to visit by updating self.current_node."""
        pass

    @abstractmethod
    def evaluate_node(self):
        """Generalized success evaluation (goal-check or reward maximization).
           Each subclass will handle its own tracking of best nodes or stopping conditions."""
        pass

    @abstractmethod
    def expand_node(self):
        """Expand the current node by adding its neighbors."""
        pass

    def finish(self):
        """Optional cleanup after search completes. Subclasses can override if needed."""
        pass
