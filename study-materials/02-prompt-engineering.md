# Prompt Engineering for GitHub Copilot

## Introduction
Prompt engineering is the art and science of crafting effective inputs to get the best outputs from GitHub Copilot. The quality of your prompts directly impacts the relevance and usefulness of Copilot's suggestions.

## Core Principles

### 1. Clarity and Specificity
- Be explicit about your intentions
- Use precise language
- Avoid ambiguous terms
- Specify expected behavior

### 2. Context Provision
- Include relevant background information
- Provide examples when helpful
- Reference existing code patterns
- Mention constraints and requirements

### 3. Progressive Elaboration
- Start with high-level descriptions
- Add details incrementally
- Build complexity gradually
- Refine based on responses

## Effective Prompt Patterns

### 1. Function Description Pattern
```python
# Function to validate email addresses using regex
# Should return True for valid emails, False otherwise
# Handle edge cases like missing @ symbol, invalid domains
def validate_email(email: str) -> bool:
```

### 2. Example-Driven Pattern
```javascript
// Create a function that formats currency
// Example: formatCurrency(1234.56, 'USD') -> '$1,234.56'
// Example: formatCurrency(1000, 'EUR') -> '€1,000.00'
function formatCurrency(amount, currency) {
```

### 3. Constraint-Specification Pattern
```python
# Sort algorithm that must be:
# - In-place (O(1) space complexity)
# - Stable (maintains relative order of equal elements)
# - Efficient for small arrays (< 50 elements)
def hybrid_sort(arr):
```

### 4. Step-by-Step Pattern
```java
// User authentication method that should:
// 1. Hash the provided password
// 2. Compare with stored hash
// 3. Update last login timestamp
// 4. Generate session token
// 5. Return authentication result
public AuthResult authenticateUser(String username, String password) {
```

## Comment Strategies

### 1. Intent Comments
```python
# Calculate the optimal route between multiple waypoints
# using the traveling salesman problem algorithm
```

### 2. Implementation Hints
```javascript
// Use binary search for O(log n) performance
// Array is already sorted by timestamp
function findEventByTime(events, targetTime) {
```

### 3. Expected Behavior
```python
# Should handle both IPv4 and IPv6 addresses
# Return normalized format: 192.168.1.1 or 2001:db8::1
def normalize_ip_address(ip_string):
```

### 4. Edge Case Specifications
```java
// Handle null inputs, empty strings, and whitespace-only strings
// Throw IllegalArgumentException for invalid formats
public PhoneNumber parsePhoneNumber(String input) {
```

## Advanced Prompting Techniques

### 1. Multi-Language Context
```python
# Create a Python wrapper for the JavaScript crypto library
# Should provide the same interface as the JS version:
# encrypt(data, key) and decrypt(ciphertext, key)
```

### 2. Framework-Specific Prompts
```typescript
// React component for user profile display
// Uses Material-UI styling and handles loading states
// Props: userId (string), onEdit (function)
interface UserProfileProps {
```

### 3. Performance-Conscious Prompts
```python
# High-performance image processing function
# Process 4K images in under 100ms
# Use NumPy for vectorized operations
def enhance_image_contrast(image_array):
```

### 4. Test-Driven Prompts
```javascript
// Function should pass these test cases:
// fibonacci(0) -> 0, fibonacci(1) -> 1
// fibonacci(5) -> 5, fibonacci(10) -> 55
// Should handle negative inputs gracefully
function fibonacci(n) {
```

## Context Optimization

### 1. File-Level Context
- Keep related functions together
- Use consistent naming conventions
- Maintain clear file organization
- Include relevant imports at the top

### 2. Project-Level Context
- Follow established patterns
- Use existing utility functions
- Match the codebase style
- Reference shared constants

### 3. Documentation Context
```python
"""
User management module for the e-commerce platform.
Handles user registration, authentication, and profile management.
Integrates with PostgreSQL database and Redis cache.
"""

# New function to update user preferences
# Should update both database and cache
def update_user_preferences(user_id, preferences):
```

## Language-Specific Considerations

### Python
```python
# Use type hints for better suggestions
from typing import List, Dict, Optional

# Function to process customer data with pandas
# Return summary statistics as a dictionary
def analyze_customer_data(df: pd.DataFrame) -> Dict[str, float]:
```

### JavaScript/TypeScript
```typescript
// Async function using modern ES6+ features
// Handle API rate limiting with exponential backoff
// Return typed response object
async function fetchUserData(userId: string): Promise<UserData> {
```

### Java
```java
// Service class following Spring Boot conventions
// Use dependency injection for repository
// Implement proper exception handling
@Service
public class UserService {
```

### C#
```csharp
// LINQ-based data processing method
// Filter and transform collections efficiently
// Return IEnumerable for lazy evaluation
public IEnumerable<ProcessedItem> ProcessItems(IEnumerable<RawItem> items) {
```

## Common Anti-Patterns

### 1. Vague Prompts
❌ **Bad**: "Make a function"
✅ **Good**: "Create a function to validate credit card numbers using the Luhn algorithm"

### 2. Over-Specification
❌ **Bad**: Extremely long comments with every implementation detail
✅ **Good**: Clear intent with key requirements and constraints

### 3. Inconsistent Context
❌ **Bad**: Mixed coding styles and naming conventions
✅ **Good**: Consistent patterns that help Copilot understand your style

### 4. Missing Error Handling Hints
❌ **Bad**: No mention of error scenarios
✅ **Good**: Specify how to handle edge cases and errors

## Prompt Refinement Process

### 1. Initial Prompt
Start with a basic description of what you want

### 2. Evaluate Suggestion
Review the generated code for accuracy and completeness

### 3. Refine Context
Add more details or constraints based on the initial response

### 4. Iterate
Continue refining until you get the desired output

## Testing Your Prompts

### 1. Consistency Check
- Try the same prompt multiple times
- Verify consistent quality
- Look for variation in approaches

### 2. Clarity Validation
- Test with minimal context
- Add context incrementally
- Measure improvement in suggestions

### 3. Edge Case Coverage
- Include error scenarios in prompts
- Test boundary conditions
- Verify robust handling

## Best Practices Summary

1. **Be Specific**: Clear, detailed descriptions work better
2. **Provide Examples**: Show expected input/output when helpful
3. **Set Context**: Include relevant background and constraints
4. **Use Good Names**: Descriptive variable and function names
5. **Iterate**: Refine prompts based on initial results
6. **Stay Consistent**: Follow established patterns in your codebase
7. **Think Like AI**: Consider how the model interprets your prompt

## Practice Exercises

1. Write prompts for common algorithms (sorting, searching)
2. Create prompts for API integration functions
3. Practice prompts for different programming paradigms
4. Experiment with prompts for testing and documentation

---
*Continue to: [03-advanced-features.md](./03-advanced-features.md)*
