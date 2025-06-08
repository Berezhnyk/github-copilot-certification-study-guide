# Exercise 4: API Response Handler
# Task: Create a robust API response handler with error management

import json
from typing import Dict, Any, Optional, Union

class APIResponseHandler:
    """
    Handle API responses with proper error handling and data extraction.
    """
    
    def __init__(self):
        self.last_response = None
        self.last_error = None
    
    def handle_response(self, response_data: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Process API response and extract relevant data.
        
        Args:
            response_data: Raw API response (JSON string or dict)
        
        Returns:
            dict: Processed response with status, data, and error information
        """
        # TODO: Let Copilot implement response handling logic
        pass
    
    def extract_user_data(self, response: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Extract user data from successful API responses.
        
        Args:
            response: Processed API response
        
        Returns:
            dict: User data if available, None otherwise
        """
        # TODO: Let Copilot implement data extraction
        pass
    
    def get_error_message(self, response: Dict[str, Any]) -> Optional[str]:
        """
        Extract error message from failed API responses.
        
        Args:
            response: Processed API response
        
        Returns:
            str: Error message if available, None otherwise
        """
        # TODO: Let Copilot implement error extraction
        pass


# Test data
success_response = {
    "status": "success",
    "data": {
        "id": 123,
        "name": "John Doe",
        "email": "john@example.com",
        "profile": {
            "age": 30,
            "location": "New York"
        }
    },
    "message": "User retrieved successfully"
}

error_response = {
    "status": "error",
    "error_code": 404,
    "message": "User not found",
    "details": "No user with the specified ID exists"
}

if __name__ == "__main__":
    handler = APIResponseHandler()
    
    # Test success response
    result = handler.handle_response(success_response)
    print("Success response handling:")
    print(json.dumps(result, indent=2))
    
    # Test error response
    result = handler.handle_response(error_response)
    print("\nError response handling:")
    print(json.dumps(result, indent=2))
