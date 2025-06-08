# Exercise 7: Algorithm Implementation
# Task: Implement a binary search algorithm with Copilot's help

from typing import List, Optional

# Binary search implementation
# Search for target in sorted array
# Time complexity: O(log n)
# Returns: index of target if found, -1 if not found
# Handles empty arrays and single-element arrays
def binary_search(arr: List[int], target: int) -> int:
    """
    Perform binary search on a sorted array.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
    
    Returns:
        int: Index of target if found, -1 if not found
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # TODO: Let Copilot implement the binary search algorithm
    # Requirements:
    # - Handle empty arrays
    # - Handle single-element arrays
    # - Use iterative approach for O(1) space complexity
    # - Ensure proper boundary checking
    pass


def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: Optional[int] = None) -> int:
    """
    Recursive implementation of binary search.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
        left (int): Left boundary of search range
        right (int): Right boundary of search range
    
    Returns:
        int: Index of target if found, -1 if not found
    """
    # TODO: Let Copilot implement recursive binary search
    # Include base cases and recursive calls
    pass


def binary_search_first_occurrence(arr: List[int], target: int) -> int:
    """
    Find the first occurrence of target in a sorted array with duplicates.
    
    Args:
        arr (List[int]): Sorted array (may contain duplicates)
        target (int): Value to search for
    
    Returns:
        int: Index of first occurrence, -1 if not found
    """
    # TODO: Let Copilot implement modified binary search
    # for finding first occurrence
    pass


def binary_search_last_occurrence(arr: List[int], target: int) -> int:
    """
    Find the last occurrence of target in a sorted array with duplicates.
    
    Args:
        arr (List[int]): Sorted array (may contain duplicates)  
        target (int): Value to search for
    
    Returns:
        int: Index of last occurrence, -1 if not found
    """
    # TODO: Let Copilot implement modified binary search
    # for finding last occurrence
    pass


def binary_search_range(arr: List[int], target: int) -> tuple[int, int]:
    """
    Find the range of indices where target appears in sorted array.
    
    Args:
        arr (List[int]): Sorted array
        target (int): Value to search for
    
    Returns:
        tuple: (first_index, last_index) or (-1, -1) if not found
    """
    # TODO: Let Copilot implement range finding using binary search
    pass


# Test cases to verify implementations
if __name__ == "__main__":
    # Test arrays
    empty_array = []
    single_element = [5]
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    with_duplicates = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    
    print("Testing Binary Search Implementations")
    print("=" * 40)
    
    # Test basic binary search
    print("\\n1. Basic Binary Search:")
    test_cases = [
        (sorted_array, 7, 3),    # Found
        (sorted_array, 1, 0),    # First element
        (sorted_array, 19, 9),   # Last element
        (sorted_array, 10, -1),  # Not found
        (empty_array, 5, -1),    # Empty array
        (single_element, 5, 0),  # Single element found
        (single_element, 3, -1), # Single element not found
    ]
    
    for arr, target, expected in test_cases:
        result = binary_search(arr, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} Search {target} in {arr[:5]}{'...' if len(arr) > 5 else ''}: "
              f"Expected {expected}, Got {result}")
    
    # Test recursive implementation
    print("\\n2. Recursive Binary Search:")
    for arr, target, expected in test_cases:
        result = binary_search_recursive(arr, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} Search {target}: Expected {expected}, Got {result}")
    
    # Test with duplicates
    print("\\n3. First/Last Occurrence:")
    duplicate_tests = [
        (with_duplicates, 2, "first"),
        (with_duplicates, 2, "last"),
        (with_duplicates, 5, "first"),
        (with_duplicates, 5, "last"),
        (with_duplicates, 7, "first"),  # Not found
    ]
    
    for arr, target, search_type in duplicate_tests:
        if search_type == "first":
            result = binary_search_first_occurrence(arr, target)
        else:
            result = binary_search_last_occurrence(arr, target)
        print(f"Find {search_type} occurrence of {target} in {arr}: {result}")
    
    # Test range finding
    print("\\n4. Range Finding:")
    range_tests = [2, 4, 5, 7]  # Different targets to test ranges
    for target in range_tests:
        result = binary_search_range(with_duplicates, target)
        print(f"Range for {target} in {with_duplicates}: {result}")
    
    print("\\n" + "=" * 40)
    print("All tests completed!")
    print("\\nPerformance Notes:")
    print("- Time Complexity: O(log n)")
    print("- Space Complexity: O(1) for iterative, O(log n) for recursive")
    print("- Works only on sorted arrays")
    print("- Efficient for large datasets")
