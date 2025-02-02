"""
we define a tree ADT using the concept of a position as an abstraction for a node of a tree. 
An element is stored at each position, and positions satisfy parent-child relationships that 
define the tree structure. 
"""
from abc import abstractmethod


class Position:
    """An abstraction representing the location of a single element."""
    
    @abstractmethod
    def element(self):
        """Return the element stores at this Position."""
        raise NotImplementedError('Must be implemented by subclass!')
    
    @abstractmethod
    def __eq__(self, o: object) -> bool:
        """Returns True if other Position represents the same location."""
        raise NotImplementedError('Must be implemented by subclass!')

    @abstractmethod
    def __ne__(self, other: object) -> bool:
        """Returns True if other Position represents the same location."""
        raise NotImplementedError('Must be implemented by subclass!')


class Tree:
    """Abstract base class representing a tree structure."""

    @abstractmethod
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('Must be implemented by subclass!')

    @abstractmethod
    def parent(self, p: Position):
        """Return Position representing the p's parent (or None if empty)."""
        raise NotImplementedError('Must be implemented by subclass!')

    @abstractmethod
    def num_children(self, p: Position):
        """Return the number of children that Position p has."""
        raise NotImplementedError('Must be implemented by subclass!')

    @abstractmethod
    def children(self, p: Position):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('Must be implemented by subclass!')

    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('Must be implemented by subclass!')

    def is_root(self, p: Position) -> bool:
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p: Position) -> bool:
        """Return True if Position p represents the leaf of the tree."""
        return self.num_children(p) == 0

    def is_empty(self) -> bool:
        """Return True if the tree if empty."""
        return len(self) == 0
    
    def depth(self, p: Position) -> int:
        """Return the number of leaves separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height(self, p: Position) -> int:
        """Helper function -- Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))
        
    def height(self, p: Position = None) -> int:
        """Return the height of the subtree rooted at Position p.
        
        If p is None, return the height of the entire tree.
        """
        if not p:
            p = self.root()
        return self._height(p)
