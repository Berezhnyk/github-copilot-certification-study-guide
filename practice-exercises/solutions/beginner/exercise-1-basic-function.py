# Exercise 1: Basic Function Creation
# Task: Create a function that calculates the area of different geometric shapes

# Function to calculate area of geometric shapes
# Supports circle, rectangle, and triangle
# Parameters: shape_type (string), dimensions (dict)
# Returns: area as float, or None if invalid shape
def calculate_area(shape_type, dimensions):
    """
    Calculate the area of different geometric shapes.
    
    Args:
        shape_type (str): Type of shape ('circle', 'rectangle', 'triangle')
        dimensions (dict): Shape-specific dimensions
    
    Returns:
        float: Area of the shape, or None if invalid
    """
    # TODO: Let Copilot complete this function
    pass


# Test cases to verify your implementation
if __name__ == "__main__":
    # Test circle
    print(f"Circle area (radius=5): {calculate_area('circle', {'radius': 5})}")
    
    # Test rectangle
    print(f"Rectangle area (4x6): {calculate_area('rectangle', {'width': 4, 'height': 6})}")
    
    # Test triangle
    print(f"Triangle area (base=10, height=8): {calculate_area('triangle', {'base': 10, 'height': 8})}")
    
    # Test invalid shape
    print(f"Invalid shape: {calculate_area('invalid', {})}")
