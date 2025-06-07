# Beginner Practice Exercises

## Exercise 1: Basic Function Creation

### Task
Use GitHub Copilot to create a function that calculates the area of different geometric shapes.

### Instructions
1. Write a comment describing the function
2. Let Copilot suggest the implementation
3. Test with different inputs

### Starting Code
```python
# Function to calculate area of geometric shapes
# Supports circle, rectangle, and triangle
# Parameters: shape_type (string), dimensions (list or dict)
# Returns: area as float, or None if invalid shape
def calculate_area(shape_type, dimensions):
    # Let Copilot complete this function
```

### Expected Features
- Handle circles (radius)
- Handle rectangles (width, height)
- Handle triangles (base, height)
- Error handling for invalid inputs
- Type hints if possible

### Test Cases
```python
# Test your function with these cases:
print(calculate_area("circle", {"radius": 5}))  # Should return ~78.54
print(calculate_area("rectangle", {"width": 4, "height": 6}))  # Should return 24
print(calculate_area("triangle", {"base": 10, "height": 8}))  # Should return 40
print(calculate_area("invalid", {}))  # Should return None or raise error
```

---

## Exercise 2: Data Processing

### Task
Create a function that processes a list of student records and returns statistics.

### Instructions
1. Start with a clear comment about the function's purpose
2. Use Copilot to generate the implementation
3. Include error handling

### Starting Code
```python
# Function to analyze student grades
# Input: list of dictionaries with 'name', 'grade', 'subject' keys
# Output: dictionary with statistics (average, highest, lowest, pass_rate)
# Pass rate is percentage of grades >= 60
def analyze_student_grades(students):
    # Let Copilot implement this
```

### Sample Data
```python
students = [
    {"name": "Alice", "grade": 85, "subject": "Math"},
    {"name": "Bob", "grade": 76, "subject": "Math"},
    {"name": "Charlie", "grade": 92, "subject": "Science"},
    {"name": "Diana", "grade": 58, "subject": "Math"},
    {"name": "Eve", "grade": 88, "subject": "Science"}
]
```

---

## Exercise 3: String Manipulation

### Task
Create a function that validates and formats phone numbers.

### Instructions
1. Write descriptive comments about the expected behavior
2. Use Copilot to implement the logic
3. Handle various input formats

### Starting Code
```javascript
// Function to validate and format phone numbers
// Accepts various formats: (123) 456-7890, 123-456-7890, 1234567890
// Returns formatted as: (123) 456-7890
// Returns null for invalid numbers
function formatPhoneNumber(phoneNumber) {
    // Let Copilot complete this
}
```

### Test Cases
```javascript
console.log(formatPhoneNumber("1234567890"));        // "(123) 456-7890"
console.log(formatPhoneNumber("123-456-7890"));      // "(123) 456-7890"
console.log(formatPhoneNumber("(123) 456-7890"));    // "(123) 456-7890"
console.log(formatPhoneNumber("123"));                // null
console.log(formatPhoneNumber("12345678901"));       // null
```

---

## Exercise 4: API Response Handler

### Task
Create a function that processes API responses and handles errors gracefully.

### Instructions
1. Comment about the expected API response structure
2. Let Copilot generate error handling logic
3. Include data transformation

### Starting Code
```python
# Function to process API response from user service
# Expected response: {"status": "success", "data": {...}, "message": "..."}
# For errors: {"status": "error", "error_code": 400, "message": "..."}
# Returns: user data dict if successful, None if error
# Should log errors appropriately
def process_user_api_response(response_json):
    # Let Copilot implement this
```

### Sample Responses
```python
# Success response
success_response = {
    "status": "success",
    "data": {
        "id": 123,
        "name": "John Doe",
        "email": "john@example.com"
    },
    "message": "User retrieved successfully"
}

# Error response
error_response = {
    "status": "error",
    "error_code": 404,
    "message": "User not found"
}
```

---

## Exercise 5: File Operations

### Task
Create a utility function for reading and parsing configuration files.

### Instructions
1. Write comments about supported file formats
2. Use Copilot to handle different file types
3. Include error handling for file operations

### Starting Code
```python
# Function to read and parse configuration files
# Supports JSON, YAML, and INI formats
# Returns: dictionary with configuration data
# Handles file not found, invalid format, and permission errors
def read_config_file(file_path):
    # Let Copilot complete this implementation
```

---

## Exercise 6: Class Design

### Task
Create a simple class for managing a shopping cart.

### Instructions
1. Start with a class comment describing its purpose
2. Let Copilot suggest methods and properties
3. Include input validation

### Starting Code
```python
# Shopping cart class for e-commerce application
# Should track items, quantities, and calculate totals
# Include methods for add, remove, update quantity, and get total
class ShoppingCart:
    def __init__(self):
        # Let Copilot initialize the cart
        
    # Let Copilot suggest and implement methods
```

---

## Exercise 7: Algorithm Implementation

### Task
Implement a binary search algorithm with Copilot's help.

### Instructions
1. Write a clear comment about the algorithm
2. Specify time complexity requirements
3. Include edge case handling

### Starting Code
```python
# Binary search implementation
# Search for target in sorted array
# Time complexity: O(log n)
# Returns: index of target if found, -1 if not found
# Handles empty arrays and single-element arrays
def binary_search(arr, target):
    # Let Copilot implement the algorithm
```

---

## Exercise 8: Test Generation

### Task
Use Copilot to generate unit tests for a simple function.

### Instructions
1. First, implement a function to test
2. Write a comment about what tests are needed
3. Let Copilot generate test cases

### Starting Code
```python
def fibonacci(n):
    """Generate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Generate comprehensive unit tests for the fibonacci function
# Include edge cases: negative numbers, zero, one, and larger numbers
# Test both correctness and performance considerations
import unittest

class TestFibonacci(unittest.TestCase):
    # Let Copilot generate test methods
```

---

## Evaluation Criteria

For each exercise, evaluate:

1. **Prompt Quality**: How well did your comments guide Copilot?
2. **Code Quality**: Is the generated code readable and maintainable?
3. **Completeness**: Does it handle all specified requirements?
4. **Error Handling**: Are edge cases properly managed?
5. **Performance**: Is the solution efficient?

## Tips for Success

1. **Start Simple**: Begin with basic comments and add detail as needed
2. **Be Specific**: Clear requirements lead to better suggestions
3. **Iterate**: Refine your prompts based on initial results
4. **Test Thoroughly**: Always verify the generated code works correctly
5. **Learn Patterns**: Notice what comment styles work best

---
*Continue to: [intermediate-exercises.md](./intermediate-exercises.md)*
