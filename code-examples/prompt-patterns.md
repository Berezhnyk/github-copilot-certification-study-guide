# Effective Prompt Patterns for GitHub Copilot

This document contains proven prompt patterns and techniques for getting the best results from GitHub Copilot.

## 1. Function Documentation Pattern

### Pattern
```python
# [Detailed function description]
# Parameters: [parameter descriptions with types]
# Returns: [return value description]
# Raises: [exception descriptions]
# Example: [usage example]
def function_name(parameters):
```

### Example
```python
# Validates email addresses using comprehensive regex pattern
# Parameters: 
#   email (str): Email address to validate
#   allow_international (bool): Whether to allow international domains
# Returns: bool - True if valid email, False otherwise
# Raises: TypeError if email is not a string
# Example: validate_email("user@example.com") -> True
def validate_email(email: str, allow_international: bool = True) -> bool:
    import re
    
    if not isinstance(email, str):
        raise TypeError("Email must be a string")
    
    # Basic email pattern
    if not allow_international:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    else:
        # More comprehensive pattern for international emails
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return bool(re.match(pattern, email))
```

## 2. Class Design Pattern

### Pattern
```python
# [Class purpose and responsibility]
# Attributes: [attribute descriptions]
# Methods: [method descriptions]
# Usage: [example usage]
class ClassName:
```

### Example
```python
# User session manager for web applications
# Attributes:
#   - sessions: dict storing active user sessions
#   - timeout: session timeout in seconds
# Methods:
#   - create_session: creates new user session
#   - validate_session: checks if session is valid
#   - destroy_session: removes session
# Usage: session_mgr = SessionManager(timeout=3600)
class SessionManager:
    def __init__(self, timeout: int = 3600):
        self.sessions = {}
        self.timeout = timeout
        self._cleanup_interval = 300  # 5 minutes
        
    def create_session(self, user_id: str) -> str:
        """Create a new session for the user."""
        import uuid
        from datetime import datetime, timedelta
        
        session_id = str(uuid.uuid4())
        expires_at = datetime.now() + timedelta(seconds=self.timeout)
        
        self.sessions[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now(),
            'expires_at': expires_at,
            'last_activity': datetime.now()
        }
        
        return session_id
    
    def validate_session(self, session_id: str) -> bool:
        """Check if session exists and is not expired."""
        from datetime import datetime
        
        if session_id not in self.sessions:
            return False
            
        session = self.sessions[session_id]
        if datetime.now() > session['expires_at']:
            del self.sessions[session_id]
            return False
            
        # Update last activity
        session['last_activity'] = datetime.now()
        return True
```

## 3. Algorithm Implementation Pattern

### Pattern
```python
# [Algorithm name and description]
# Time complexity: O(...)
# Space complexity: O(...)
# Approach: [brief explanation of approach]
# Edge cases: [list of edge cases handled]
def algorithm_name(parameters):
```

### Example
```python
# Quick sort implementation with random pivot selection
# Time complexity: O(n log n) average, O(n²) worst case
# Space complexity: O(log n) for recursion stack
# Approach: Divide and conquer with in-place partitioning
# Edge cases: empty array, single element, duplicate elements
def quick_sort(arr: list, low: int = 0, high: int = None) -> None:
    import random
    
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Random pivot selection for better average performance
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        
        # Partition array around pivot
        partition_idx = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, partition_idx - 1)
        quick_sort(arr, partition_idx + 1, high)

def partition(arr: list, low: int, high: int) -> int:
    """Partition array using last element as pivot."""
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

## 4. API Integration Pattern

### Pattern
```python
# [API description and purpose]
# Endpoints: [list of endpoints used]
# Authentication: [auth method]
# Rate limiting: [rate limit handling]
# Error handling: [error scenarios covered]
class APIClient:
```

### Example
```python
# GitHub API client with rate limiting and error handling
# Endpoints: /user, /repos, /issues, /pulls
# Authentication: Personal access token
# Rate limiting: 5000 requests per hour, implements exponential backoff
# Error handling: network errors, API errors, rate limits
import requests
import time
from typing import Dict, List, Optional
from datetime import datetime, timedelta

class GitHubAPIClient:
    def __init__(self, token: str, base_url: str = "https://api.github.com"):
        self.token = token
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        })
        self._rate_limit_remaining = 5000
        self._rate_limit_reset = datetime.now() + timedelta(hours=1)
    
    def get_user_repos(self, username: str) -> List[Dict]:
        """Get all repositories for a user."""
        return self._paginated_request(f'/users/{username}/repos')
    
    def _paginated_request(self, endpoint: str, params: Dict = None) -> List[Dict]:
        """Handle paginated API responses."""
        results = []
        page = 1
        
        while True:
            page_params = {'page': page, 'per_page': 100}
            if params:
                page_params.update(params)
            
            response = self._make_request('GET', endpoint, params=page_params)
            page_data = response.json()
            
            if not page_data:
                break
                
            results.extend(page_data)
            page += 1
            
            # Check if we've reached the last page
            if len(page_data) < 100:
                break
        
        return results
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make API request with rate limiting and error handling."""
        self._check_rate_limit()
        
        url = f"{self.base_url}{endpoint}"
        
        for attempt in range(3):  # Retry up to 3 times
            try:
                response = self.session.request(method, url, **kwargs)
                
                # Update rate limit info
                self._update_rate_limit(response)
                
                if response.status_code == 429:  # Rate limited
                    self._handle_rate_limit(response)
                    continue
                
                response.raise_for_status()
                return response
                
            except requests.exceptions.RequestException as e:
                if attempt == 2:  # Last attempt
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
        
        raise Exception("Max retries exceeded")
```

## 5. Data Processing Pipeline Pattern

### Pattern
```python
# [Pipeline description and purpose]
# Input: [input data format and source]
# Output: [output data format and destination]
# Steps: [list of processing steps]
# Performance: [performance characteristics]
# Error handling: [error recovery strategies]
class DataPipeline:
```

### Example
```python
# ETL pipeline for processing customer transaction data
# Input: CSV files from S3 bucket, JSON from REST API
# Output: Cleaned data to PostgreSQL database
# Steps: extract, validate, transform, aggregate, load
# Performance: Processes 1M+ records efficiently using chunking
# Error handling: Dead letter queue for failed records, retry logic
import pandas as pd
import logging
from typing import List, Dict, Any, Generator
from datetime import datetime
from dataclasses import dataclass

@dataclass
class PipelineConfig:
    batch_size: int = 10000
    max_retries: int = 3
    dead_letter_queue: str = "failed_records.json"

class CustomerTransactionPipeline:
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.failed_records = []
    
    def process_transactions(self, data_source: str) -> Dict[str, Any]:
        """Main pipeline execution method."""
        stats = {
            'total_processed': 0,
            'successful': 0,
            'failed': 0,
            'start_time': datetime.now()
        }
        
        try:
            # Extract data in chunks
            for chunk in self._extract_data(data_source):
                processed_chunk = self._process_chunk(chunk)
                stats['total_processed'] += len(chunk)
                stats['successful'] += len(processed_chunk)
                stats['failed'] += len(chunk) - len(processed_chunk)
                
                # Load processed data
                self._load_data(processed_chunk)
                
        except Exception as e:
            self.logger.error(f"Pipeline failed: {e}")
            raise
        finally:
            stats['end_time'] = datetime.now()
            stats['duration'] = stats['end_time'] - stats['start_time']
            
        return stats
    
    def _extract_data(self, source: str) -> Generator[pd.DataFrame, None, None]:
        """Extract data in configurable chunks."""
        if source.endswith('.csv'):
            chunk_iter = pd.read_csv(source, chunksize=self.config.batch_size)
            for chunk in chunk_iter:
                yield chunk
        else:
            # Handle other data sources (API, database, etc.)
            pass
    
    def _process_chunk(self, chunk: pd.DataFrame) -> pd.DataFrame:
        """Process a single chunk of data."""
        # Validate data
        valid_chunk = self._validate_data(chunk)
        
        # Transform data
        transformed_chunk = self._transform_data(valid_chunk)
        
        # Aggregate if needed
        aggregated_chunk = self._aggregate_data(transformed_chunk)
        
        return aggregated_chunk
```

## 6. Testing Pattern

### Pattern
```python
# [Test description and scope]
# Test cases: [list of scenarios tested]
# Fixtures: [test data and setup]
# Mocking: [external dependencies mocked]
# Coverage: [coverage requirements]
class TestClassName:
```

### Example
```python
# Comprehensive tests for user authentication service
# Test cases: valid login, invalid credentials, account lockout, session management
# Fixtures: test users, mock database, fake time
# Mocking: database calls, email service, cache layer
# Coverage: 100% line coverage, all edge cases
import pytest
import unittest.mock as mock
from datetime import datetime, timedelta
from auth_service import AuthenticationService, User, LoginResult

class TestAuthenticationService:
    @pytest.fixture
    def auth_service(self):
        """Create authentication service with mocked dependencies."""
        with mock.patch('auth_service.Database') as mock_db, \
             mock.patch('auth_service.CacheService') as mock_cache:
            service = AuthenticationService(mock_db, mock_cache)
            service.max_login_attempts = 3
            service.lockout_duration = timedelta(minutes=15)
            return service, mock_db, mock_cache
    
    @pytest.fixture
    def test_user(self):
        """Create test user data."""
        return User(
            id=1,
            username="testuser",
            password_hash="$2b$12$hashed_password",
            email="test@example.com",
            is_active=True,
            failed_login_attempts=0,
            locked_until=None
        )
    
    def test_successful_login(self, auth_service, test_user):
        """Test successful user authentication."""
        service, mock_db, mock_cache = auth_service
        
        # Setup mocks
        mock_db.get_user_by_username.return_value = test_user
        
        # Execute
        result = service.authenticate("testuser", "correct_password")
        
        # Verify
        assert result.success is True
        assert result.user_id == test_user.id
        assert result.session_token is not None
        mock_db.reset_failed_attempts.assert_called_once_with(test_user.id)
    
    def test_invalid_credentials(self, auth_service, test_user):
        """Test authentication with wrong password."""
        service, mock_db, mock_cache = auth_service
        
        # Setup mocks
        mock_db.get_user_by_username.return_value = test_user
        
        # Execute
        result = service.authenticate("testuser", "wrong_password")
        
        # Verify
        assert result.success is False
        assert result.error == "Invalid credentials"
        mock_db.increment_failed_attempts.assert_called_once_with(test_user.id)
    
    def test_account_lockout_after_max_attempts(self, auth_service, test_user):
        """Test account lockout after exceeding max login attempts."""
        service, mock_db, mock_cache = auth_service
        
        # Setup user with max failed attempts
        test_user.failed_login_attempts = 3
        mock_db.get_user_by_username.return_value = test_user
        
        # Execute
        result = service.authenticate("testuser", "wrong_password")
        
        # Verify
        assert result.success is False
        assert result.error == "Account locked"
        mock_db.lock_account.assert_called_once()
```

## Tips for Using These Patterns

1. **Adapt to Context**: Modify patterns based on your specific needs
2. **Be Specific**: Include concrete details in your prompts
3. **Layer Information**: Start with basic pattern, add complexity gradually
4. **Include Examples**: Show expected input/output when helpful
5. **Specify Constraints**: Mention performance, security, or other requirements
6. **Test Patterns**: Experiment with variations to find what works best

## Pattern Combination

You can combine multiple patterns for complex scenarios:

```python
# RESTful API endpoint with caching and rate limiting
# Endpoint: GET /api/users/{user_id}/recommendations
# Caching: Redis with 15-minute TTL
# Rate limiting: 100 requests per minute per user
# Authentication: JWT token required
# Response: JSON with user recommendations and metadata
@app.route('/api/users/<int:user_id>/recommendations')
@jwt_required
@rate_limit(100, per_minute=True)
def get_user_recommendations(user_id: int):
    # Let Copilot implement with all specified features
```

This approach helps Copilot understand the complete context and generate more appropriate solutions.
