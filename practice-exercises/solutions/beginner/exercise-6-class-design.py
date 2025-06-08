# Exercise 6: Class Design
# Task: Create a simple class for managing a shopping cart

from typing import Dict, List, Optional
from decimal import Decimal

# Shopping cart class for e-commerce application
# Should track items, quantities, and calculate totals
# Include methods for add, remove, update quantity, and get total
class ShoppingCart:
    """
    Shopping cart for e-commerce application.
    
    Features:
    - Add items with quantities
    - Remove items
    - Update quantities
    - Calculate totals with tax
    - Apply discounts
    - Clear cart
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        # TODO: Let Copilot initialize the cart data structure
        # Consider: items storage, tax rate, discount tracking
        pass
    
    def add_item(self, item_id: str, name: str, price: float, quantity: int = 1) -> bool:
        """
        Add an item to the cart.
        
        Args:
            item_id (str): Unique identifier for the item
            name (str): Item name
            price (float): Item price
            quantity (int): Quantity to add
        
        Returns:
            bool: True if successful, False otherwise
        """
        # TODO: Let Copilot implement add logic
        # Include validation for price > 0, quantity > 0
        pass
    
    def remove_item(self, item_id: str) -> bool:
        """
        Remove an item completely from the cart.
        
        Args:
            item_id (str): Item to remove
        
        Returns:
            bool: True if removed, False if not found
        """
        # TODO: Let Copilot implement remove logic
        pass
    
    def update_quantity(self, item_id: str, quantity: int) -> bool:
        """
        Update the quantity of an item in the cart.
        
        Args:
            item_id (str): Item to update
            quantity (int): New quantity (0 to remove)
        
        Returns:
            bool: True if updated, False if item not found
        """
        # TODO: Let Copilot implement quantity update
        pass
    
    def get_total(self, tax_rate: float = 0.0) -> float:
        """
        Calculate the total cost of items in the cart.
        
        Args:
            tax_rate (float): Tax rate as decimal (0.08 = 8%)
        
        Returns:
            float: Total cost including tax
        """
        # TODO: Let Copilot calculate subtotal + tax
        pass
    
    def get_items(self) -> List[Dict]:
        """
        Get all items in the cart.
        
        Returns:
            list: List of item dictionaries
        """
        # TODO: Let Copilot return formatted item list
        pass
    
    def clear(self) -> None:
        """Clear all items from the cart."""
        # TODO: Let Copilot implement cart clearing
        pass
    
    def apply_discount(self, discount_percent: float) -> bool:
        """
        Apply a percentage discount to the cart.
        
        Args:
            discount_percent (float): Discount as percentage (10.0 = 10%)
        
        Returns:
            bool: True if applied successfully
        """
        # TODO: Let Copilot implement discount logic
        pass


# Test the shopping cart implementation
if __name__ == "__main__":
    # Create a new cart
    cart = ShoppingCart()
    
    # Test adding items
    print("Testing cart functionality:")
    print(f"Add laptop: {cart.add_item('laptop', 'Gaming Laptop', 999.99, 1)}")
    print(f"Add mouse: {cart.add_item('mouse', 'Wireless Mouse', 29.99, 2)}")
    print(f"Add keyboard: {cart.add_item('keyboard', 'Mechanical Keyboard', 79.99, 1)}")
    
    # Display current items
    print(f"\\nItems in cart: {cart.get_items()}")
    
    # Test total calculation
    print(f"Subtotal: ${cart.get_total():.2f}")
    print(f"Total with 8% tax: ${cart.get_total(0.08):.2f}")
    
    # Test quantity update
    print(f"\\nUpdate mouse quantity to 1: {cart.update_quantity('mouse', 1)}")
    print(f"New total: ${cart.get_total():.2f}")
    
    # Test discount
    print(f"Apply 10% discount: {cart.apply_discount(10.0)}")
    print(f"Total after discount: ${cart.get_total():.2f}")
    
    # Test removal
    print(f"\\nRemove keyboard: {cart.remove_item('keyboard')}")
    print(f"Final items: {cart.get_items()}")
    print(f"Final total: ${cart.get_total():.2f}")
    
    # Clear cart
    cart.clear()
    print(f"\\nCart after clearing: {cart.get_items()}")
