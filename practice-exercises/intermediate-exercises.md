# Intermediate Practice Exercises

## Exercise 1: Data Structure Implementation

### Task
Implement a custom data structure with GitHub Copilot's assistance.

### Instructions
1. Create a balanced binary search tree (AVL tree)
2. Use detailed comments to guide implementation
3. Include all necessary operations

### Starting Code
```python
# AVL Tree implementation with automatic balancing
# Supports insert, delete, search, and traversal operations
# Maintains O(log n) height through rotations
# Each node stores value, height, and left/right children
class AVLNode:
    def __init__(self, value):
        # Let Copilot initialize node properties
        
class AVLTree:
    def __init__(self):
        # Initialize empty tree
        
    # Insert operation with automatic balancing
    # Should update heights and perform rotations as needed
    def insert(self, value):
        # Let Copilot implement with balancing logic
        
    # Delete operation maintaining AVL properties
    def delete(self, value):
        # Let Copilot implement with rebalancing
        
    # Search operation in O(log n) time
    def search(self, value):
        # Let Copilot implement efficient search
        
    # Helper methods for rotations and height calculation
    # Let Copilot suggest and implement helper methods
```

---

## Exercise 2: Design Pattern Implementation

### Task
Implement the Observer pattern for a notification system.

### Instructions
1. Create a robust notification system using the Observer pattern
2. Use comments to specify the pattern requirements
3. Include type safety and error handling

### Starting Code
```python
# Observer pattern implementation for notification system
# Publisher maintains list of subscribers and notifies them of events
# Supports multiple event types and selective subscription
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from enum import Enum

class EventType(Enum):
    USER_CREATED = "user_created"
    USER_UPDATED = "user_updated"
    USER_DELETED = "user_deleted"
    ORDER_PLACED = "order_placed"

# Observer interface that all subscribers must implement
class Observer(ABC):
    # Let Copilot define the observer interface
    
# Subject/Publisher that manages observers and sends notifications
class NotificationPublisher:
    def __init__(self):
        # Initialize observer management system
        # Should support multiple event types
        
    # Subscribe observer to specific event types
    def subscribe(self, observer: Observer, event_types: List[EventType]):
        # Let Copilot implement subscription logic
        
    # Unsubscribe observer from events
    def unsubscribe(self, observer: Observer, event_types: List[EventType] = None):
        # Let Copilot implement unsubscription
        
    # Notify all relevant observers of an event
    def notify(self, event_type: EventType, data: Dict[str, Any]):
        # Let Copilot implement notification logic
        
# Concrete observer implementations
class EmailNotifier(Observer):
    # Email notification implementation
    
class SMSNotifier(Observer):
    # SMS notification implementation
    
class DatabaseLogger(Observer):
    # Database logging implementation
```

---

## Exercise 3: Async/Await Patterns

### Task
Build an asynchronous web scraper with proper concurrency control.

### Instructions
1. Use async/await for concurrent HTTP requests
2. Implement rate limiting and error handling
3. Include progress tracking and result aggregation

### Starting Code
```python
# Asynchronous web scraper with rate limiting and error handling
# Supports concurrent requests with configurable limits
# Includes retry logic, timeout handling, and progress tracking
import asyncio
import aiohttp
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ScrapeResult:
    url: str
    content: Optional[str]
    status_code: int
    error: Optional[str]
    timestamp: datetime

# Async web scraper with advanced features
class AsyncWebScraper:
    def __init__(self, max_concurrent: int = 10, rate_limit: float = 1.0):
        # Initialize scraper with concurrency and rate limiting
        # max_concurrent: maximum simultaneous requests
        # rate_limit: minimum seconds between requests
        
    # Scrape multiple URLs concurrently with rate limiting
    async def scrape_urls(self, urls: List[str], timeout: int = 30) -> List[ScrapeResult]:
        # Let Copilot implement concurrent scraping with:
        # - Semaphore for concurrency control
        # - Rate limiting between requests  
        # - Proper error handling and timeouts
        # - Progress tracking
        
    # Single URL scraping with retry logic
    async def scrape_single_url(self, session: aiohttp.ClientSession, url: str, 
                                timeout: int, retries: int = 3) -> ScrapeResult:
        # Let Copilot implement with exponential backoff retry
        
    # Progress callback for tracking scraping status
    async def _progress_callback(self, completed: int, total: int):
        # Let Copilot implement progress reporting
```

---

## Exercise 4: Algorithm Optimization

### Task
Optimize a pathfinding algorithm using advanced techniques.

### Instructions
1. Implement A* pathfinding with heuristics
2. Include performance optimizations
3. Support different grid types and obstacles

### Starting Code
```python
# A* pathfinding algorithm with optimizations
# Supports weighted grids, diagonal movement, and custom heuristics
# Includes performance optimizations for large grids
import heapq
from typing import List, Tuple, Set, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum

class CellType(Enum):
    EMPTY = 0
    WALL = 1
    WATER = 2  # Higher movement cost
    GRASS = 3  # Lower movement cost

@dataclass
class GridCell:
    x: int
    y: int
    cell_type: CellType
    movement_cost: float = 1.0

@dataclass
class PathNode:
    position: Tuple[int, int]
    g_cost: float  # Distance from start
    h_cost: float  # Heuristic distance to goal
    f_cost: float = field(init=False)  # Total cost
    parent: Optional['PathNode'] = None
    
    def __post_init__(self):
        self.f_cost = self.g_cost + self.h_cost

# A* pathfinding implementation with advanced features
class AStarPathfinder:
    def __init__(self, grid: List[List[GridCell]], allow_diagonal: bool = True):
        # Initialize pathfinder with grid and movement options
        
    # Main pathfinding method using A* algorithm
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int], 
                  heuristic: Callable = None) -> Optional[List[Tuple[int, int]]]:
        # Let Copilot implement A* with:
        # - Priority queue using heapq
        # - Efficient neighbor generation
        # - Custom heuristic support
        # - Path reconstruction
        
    # Heuristic function (Manhattan distance by default)
    def manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        # Let Copilot implement Manhattan distance
        
    # Alternative heuristic (Euclidean distance)
    def euclidean_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        # Let Copilot implement Euclidean distance
        
    # Get valid neighbors with movement costs
    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[Tuple[int, int], float]]:
        # Let Copilot implement neighbor generation with costs
        
    # Optimize path by removing unnecessary waypoints
    def smooth_path(self, path: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        # Let Copilot implement path smoothing algorithm
```

---

## Exercise 5: Database Integration

### Task
Create a database abstraction layer with connection pooling and query optimization.

### Instructions
1. Support multiple database backends
2. Implement connection pooling and transaction management
3. Include query building and result mapping

### Starting Code
```python
# Database abstraction layer with connection pooling
# Supports PostgreSQL, MySQL, and SQLite backends
# Includes query building, transaction management, and result mapping
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Union, AsyncContextManager
from contextlib import asynccontextmanager
import asyncio
from dataclasses import dataclass
from enum import Enum

class DatabaseType(Enum):
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    SQLITE = "sqlite"

@dataclass
class ConnectionConfig:
    db_type: DatabaseType
    host: str = "localhost"
    port: int = 5432
    database: str = ""
    username: str = ""
    password: str = ""
    max_connections: int = 10
    min_connections: int = 1

# Abstract database interface
class DatabaseInterface(ABC):
    # Let Copilot define abstract methods for database operations
    
# Connection pool manager
class ConnectionPool:
    def __init__(self, config: ConnectionConfig):
        # Initialize connection pool with configuration
        # Should manage connection lifecycle and reuse
        
    # Get connection from pool
    async def get_connection(self):
        # Let Copilot implement connection acquisition with waiting
        
    # Return connection to pool
    async def return_connection(self, connection):
        # Let Copilot implement connection return logic
        
    # Close all connections in pool
    async def close_all(self):
        # Let Copilot implement pool cleanup

# Main database manager class
class DatabaseManager:
    def __init__(self, config: ConnectionConfig):
        # Initialize database manager with connection pooling
        
    # Execute query with automatic connection management
    async def execute(self, query: str, params: List[Any] = None) -> int:
        # Let Copilot implement query execution with connection pooling
        
    # Fetch query results with result mapping
    async def fetch(self, query: str, params: List[Any] = None) -> List[Dict[str, Any]]:
        # Let Copilot implement result fetching and mapping
        
    # Transaction context manager
    @asynccontextmanager
    async def transaction(self):
        # Let Copilot implement transaction management
        
    # Query builder for common operations
    class QueryBuilder:
        def __init__(self):
            # Initialize query builder state
            
        # Build SELECT queries with joins and conditions
        def select(self, columns: List[str], table: str) -> 'QueryBuilder':
            # Let Copilot implement SELECT query building
            
        # Add WHERE conditions
        def where(self, condition: str, params: List[Any] = None) -> 'QueryBuilder':
            # Let Copilot implement WHERE clause building
            
        # Add JOIN clauses
        def join(self, table: str, on_condition: str, join_type: str = "INNER") -> 'QueryBuilder':
            # Let Copilot implement JOIN clause building
            
        # Build final query string
        def build(self) -> Tuple[str, List[Any]]:
            # Let Copilot implement query string generation
```

---

## Exercise 6: Caching System

### Task
Implement a multi-level caching system with different eviction policies.

### Instructions
1. Support multiple cache levels (L1, L2, disk)
2. Implement LRU, LFU, and TTL eviction policies
3. Include cache statistics and monitoring

### Starting Code
```python
# Multi-level caching system with configurable eviction policies
# Supports in-memory (L1), compressed (L2), and disk (L3) caching
# Includes LRU, LFU, and TTL eviction strategies
from abc import ABC, abstractmethod
from typing import Any, Optional, Dict, List, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import threading
import pickle
import gzip

class EvictionPolicy(Enum):
    LRU = "lru"  # Least Recently Used
    LFU = "lfu"  # Least Frequently Used
    TTL = "ttl"  # Time To Live

@dataclass
class CacheEntry:
    key: str
    value: Any
    access_count: int = 0
    last_accessed: datetime = field(default_factory=datetime.now)
    created_at: datetime = field(default_factory=datetime.now)
    ttl: Optional[timedelta] = None
    
    @property
    def is_expired(self) -> bool:
        # Let Copilot implement TTL expiration check
        
# Abstract cache interface
class CacheLevel(ABC):
    # Let Copilot define abstract cache interface methods
    
# L1 Cache - Fast in-memory cache
class L1Cache(CacheLevel):
    def __init__(self, max_size: int, eviction_policy: EvictionPolicy):
        # Initialize L1 cache with size limit and eviction policy
        # Should use thread-safe data structures
        
    # Get value from L1 cache
    def get(self, key: str) -> Optional[Any]:
        # Let Copilot implement thread-safe cache retrieval
        
    # Put value in L1 cache with eviction if needed
    def put(self, key: str, value: Any, ttl: Optional[timedelta] = None):
        # Let Copilot implement cache insertion with eviction logic
        
    # Evict entries based on policy
    def _evict(self) -> str:
        # Let Copilot implement eviction based on configured policy
        
# L2 Cache - Compressed in-memory cache  
class L2Cache(CacheLevel):
    def __init__(self, max_size: int, compression_level: int = 6):
        # Initialize L2 cache with compression
        
    # Get and decompress value from L2 cache
    def get(self, key: str) -> Optional[Any]:
        # Let Copilot implement compressed cache retrieval
        
    # Compress and store value in L2 cache
    def put(self, key: str, value: Any, ttl: Optional[timedelta] = None):
        # Let Copilot implement compressed cache storage
        
# L3 Cache - Disk-based cache
class L3Cache(CacheLevel):
    def __init__(self, cache_dir: str, max_size_mb: int):
        # Initialize disk cache with size limits
        
    # Get value from disk cache
    def get(self, key: str) -> Optional[Any]:
        # Let Copilot implement disk cache retrieval
        
    # Store value to disk cache
    def put(self, key: str, value: Any, ttl: Optional[timedelta] = None):
        # Let Copilot implement disk cache storage
        
# Multi-level cache coordinator
class MultiLevelCache:
    def __init__(self, l1_cache: L1Cache, l2_cache: L2Cache, l3_cache: L3Cache):
        # Initialize multi-level cache system
        
    # Get value checking all cache levels
    def get(self, key: str) -> Optional[Any]:
        # Let Copilot implement cache hierarchy traversal
        # Should promote values to higher levels on access
        
    # Put value in appropriate cache level
    def put(self, key: str, value: Any, ttl: Optional[timedelta] = None):
        # Let Copilot implement intelligent cache placement
        
    # Get cache statistics across all levels
    def get_stats(self) -> Dict[str, Any]:
        # Let Copilot implement comprehensive cache statistics
```

---

## Evaluation Criteria

For intermediate exercises, focus on:

1. **Architecture Quality**: Well-structured, maintainable code
2. **Performance**: Efficient algorithms and data structures
3. **Error Handling**: Robust error management and edge cases
4. **Design Patterns**: Proper use of software design principles
5. **Concurrency**: Thread safety and async programming
6. **Testing**: Comprehensive test coverage
7. **Documentation**: Clear comments and docstrings

## Advanced Tips

1. **Contextual Prompting**: Reference related patterns and best practices
2. **Incremental Development**: Build complex features step by step
3. **Pattern Recognition**: Help Copilot understand design patterns you're using
4. **Performance Hints**: Specify performance requirements in comments
5. **Type Safety**: Use type hints to guide better suggestions

---
*Continue to: [advanced-exercises.md](./advanced-exercises.md)*
