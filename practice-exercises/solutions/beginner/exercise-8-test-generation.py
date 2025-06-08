# Exercise 8: Test Generation
# Task: Use Copilot to generate unit tests for a simple function

import unittest
import time
from typing import List

def fibonacci(n: int) -> int:
    """Generate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_iterative(n: int) -> int:
    """Generate the nth Fibonacci number using iterative approach."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_memoized(n: int, memo: dict = None) -> int:
    """Generate the nth Fibonacci number with memoization."""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
        return memo[n]


def fibonacci_sequence(n: int) -> List[int]:
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence


# Generate comprehensive unit tests for the fibonacci function
# Include edge cases: negative numbers, zero, one, and larger numbers
# Test both correctness and performance considerations
class TestFibonacci(unittest.TestCase):
    """
    Comprehensive test suite for Fibonacci implementations.
    
    Tests cover:
    - Edge cases (negative, zero, one)
    - Small positive numbers
    - Larger numbers for performance
    - Different implementation approaches
    - Error handling
    """
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # TODO: Let Copilot set up any needed test data
        # Known Fibonacci values for verification
        pass
    
    def test_fibonacci_edge_cases(self):
        """Test edge cases for Fibonacci function."""
        # TODO: Let Copilot generate tests for:
        # - Negative numbers
        # - Zero
        # - One
        # - Two
        pass
    
    def test_fibonacci_small_numbers(self):
        """Test Fibonacci function with small positive numbers."""
        # TODO: Let Copilot generate tests for numbers 0-15
        # Include known Fibonacci values: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
        pass
    
    def test_fibonacci_iterative_vs_recursive(self):
        """Compare iterative and recursive implementations."""
        # TODO: Let Copilot generate tests comparing both approaches
        # Ensure they produce same results for same inputs
        pass
    
    def test_fibonacci_memoized_performance(self):
        """Test memoized version for performance improvements."""
        # TODO: Let Copilot generate performance tests
        # Compare execution times between implementations
        pass
    
    def test_fibonacci_sequence_generation(self):
        """Test generation of Fibonacci sequences."""
        # TODO: Let Copilot generate tests for sequence generation
        # Test different sequence lengths
        pass
    
    def test_fibonacci_input_validation(self):
        """Test input validation and error handling."""
        # TODO: Let Copilot generate tests for:
        # - Non-integer inputs (if applicable)
        # - Very large numbers
        # - Type checking
        pass
    
    def test_fibonacci_performance_benchmarks(self):
        """Benchmark different Fibonacci implementations."""
        # TODO: Let Copilot generate performance benchmarks
        # Test with larger numbers to compare efficiency
        pass
    
    def tearDown(self):
        """Clean up after each test method."""
        # TODO: Let Copilot add any necessary cleanup
        pass


class TestFibonacciSequence(unittest.TestCase):
    """Test suite specifically for Fibonacci sequence generation."""
    
    def test_empty_sequence(self):
        """Test generation of empty sequence."""
        # TODO: Let Copilot test edge case of n <= 0
        pass
    
    def test_single_element_sequence(self):
        """Test generation of single-element sequence."""
        # TODO: Let Copilot test n = 1
        pass
    
    def test_sequence_correctness(self):
        """Test correctness of generated sequences."""
        # TODO: Let Copilot test various sequence lengths
        pass
    
    def test_sequence_length(self):
        """Test that generated sequences have correct length."""
        # TODO: Let Copilot verify sequence lengths
        pass


# Performance testing utilities
class FibonacciPerformanceTests(unittest.TestCase):
    """Performance-focused tests for Fibonacci implementations."""
    
    @unittest.skipIf(True, "Skip performance tests by default")
    def test_recursive_performance_limit(self):
        """Test recursive implementation performance limits."""
        # TODO: Let Copilot generate tests that identify
        # performance breaking points for recursive approach
        pass
    
    @unittest.skipIf(True, "Skip performance tests by default")
    def test_iterative_large_numbers(self):
        """Test iterative implementation with large numbers."""
        # TODO: Let Copilot test iterative approach with large n
        pass
    
    def test_memoization_effectiveness(self):
        """Test that memoization improves performance."""
        # TODO: Let Copilot compare performance with/without memoization
        pass


# Custom test runner with timing
def run_timed_tests():
    """Run tests with execution timing."""
    # TODO: Let Copilot implement custom test runner
    # Include timing information for each test
    pass


if __name__ == "__main__":
    # TODO: Let Copilot set up test execution
    # Include options for:
    # - Running specific test suites
    # - Verbose output
    # - Performance testing
    # - Coverage reporting
    
    print("Running Fibonacci Function Test Suite")
    print("=" * 50)
    
    # Run basic tests
    print("\\n1. Running basic functionality tests...")
    basic_suite = unittest.TestLoader().loadTestsFromTestCase(TestFibonacci)
    unittest.TextTestRunner(verbosity=2).run(basic_suite)
    
    # Run sequence tests  
    print("\\n2. Running sequence generation tests...")
    sequence_suite = unittest.TestLoader().loadTestsFromTestCase(TestFibonacciSequence)
    unittest.TextTestRunner(verbosity=2).run(sequence_suite)
    
    # Optional: Run performance tests
    print("\\n3. Performance tests available (modify decorators to enable)")
    
    print("\\n" + "=" * 50)
    print("Test suite completed!")
    
    # TODO: Let Copilot add summary reporting
    # Include test coverage, performance metrics, recommendations
