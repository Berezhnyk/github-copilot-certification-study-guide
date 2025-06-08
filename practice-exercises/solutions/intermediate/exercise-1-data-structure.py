# Exercise 1: Data Structure Implementation
# Task: Implement a balanced binary search tree (AVL tree)

from typing import Optional, List, Tuple

class AVLNode:
    """AVL Tree node with automatic height tracking."""
    
    def __init__(self, value):
        """
        Initialize AVL node.
        
        Args:
            value: The value to store in the node
        """
        # TODO: Let Copilot initialize node properties
        # Should include: value, height, left, right
        pass

class AVLTree:
    """
    AVL Tree implementation with automatic balancing.
    Supports insert, delete, search, and traversal operations.
    Maintains O(log n) height through rotations.
    """
    
    def __init__(self):
        """Initialize empty AVL tree."""
        # TODO: Initialize empty tree
        pass
    
    def insert(self, value) -> None:
        """
        Insert operation with automatic balancing.
        Should update heights and perform rotations as needed.
        
        Args:
            value: Value to insert
        """
        # TODO: Let Copilot implement with balancing logic
        pass
    
    def delete(self, value) -> bool:
        """
        Delete operation maintaining AVL properties.
        
        Args:
            value: Value to delete
        
        Returns:
            bool: True if value was found and deleted, False otherwise
        """
        # TODO: Let Copilot implement with rebalancing
        pass
    
    def search(self, value) -> bool:
        """
        Search operation in O(log n) time.
        
        Args:
            value: Value to search for
        
        Returns:
            bool: True if value exists, False otherwise
        """
        # TODO: Let Copilot implement efficient search
        pass
    
    def inorder_traversal(self) -> List:
        """
        Return inorder traversal of the tree.
        
        Returns:
            list: Values in sorted order
        """
        # TODO: Let Copilot implement traversal
        pass
    
    def get_height(self, node: Optional[AVLNode]) -> int:
        """Helper method to get node height."""
        # TODO: Let Copilot implement height calculation
        pass
    
    def get_balance(self, node: Optional[AVLNode]) -> int:
        """Helper method to get balance factor."""
        # TODO: Let Copilot implement balance factor calculation
        pass
    
    # TODO: Let Copilot suggest and implement rotation methods
    # - rotate_left
    # - rotate_right
    # - update_height


if __name__ == "__main__":
    # Test the AVL tree implementation
    tree = AVLTree()
    
    # Insert test values
    values = [10, 20, 30, 40, 50, 25, 35, 45]
    print(f"Inserting values: {values}")
    
    for value in values:
        tree.insert(value)
        print(f"Inserted {value}, tree height: {tree.get_height(tree.root) if hasattr(tree, 'root') else 'N/A'}")
    
    # Test traversal
    print(f"Inorder traversal: {tree.inorder_traversal()}")
    
    # Test search
    print(f"Search 25: {tree.search(25)}")
    print(f"Search 99: {tree.search(99)}")
    
    # Test deletion
    print(f"Delete 30: {tree.delete(30)}")
    print(f"Inorder after deletion: {tree.inorder_traversal()}")
