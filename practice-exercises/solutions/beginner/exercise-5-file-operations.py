# Exercise 5: File Operations
# Task: Create a utility function for reading and parsing configuration files

import json
import yaml
import configparser
import os
from typing import Dict, Any, Optional

# Function to read and parse configuration files
# Supports JSON, YAML, and INI formats
# Returns: dictionary with configuration data
# Handles file not found, invalid format, and permission errors
def read_config_file(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Read and parse configuration files in multiple formats.
    
    Args:
        file_path (str): Path to the configuration file
    
    Returns:
        dict: Configuration data as dictionary, None if error
    
    Supported formats:
        - JSON (.json)
        - YAML (.yaml, .yml)
        - INI (.ini, .cfg)
    """
    # TODO: Let Copilot implement file reading and parsing logic
    # Handle different file extensions
    # Include proper error handling for:
    # - File not found
    # - Permission errors
    # - Invalid format/syntax errors
    # - Unsupported file types
    pass


# Test cases to verify your implementation
if __name__ == "__main__":
    # Test with sample config files
    test_configs = [
        "config.json",
        "settings.yaml", 
        "app.ini",
        "nonexistent.json"
    ]
    
    for config_file in test_configs:
        print(f"Reading {config_file}:")
        result = read_config_file(config_file)
        print(f"Result: {result}")
        print("---")
    
    # Create sample config files for testing
    sample_json = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp"
        },
        "debug": True
    }
    
    sample_yaml = """
database:
  host: localhost
  port: 5432
  name: myapp
debug: true
logging:
  level: INFO
  file: app.log
"""
    
    # TODO: Let Copilot complete test file creation
    # Write sample config files for testing
    # Test error handling with invalid files
