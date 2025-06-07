# GitHub Copilot Coding Challenges

## Overview
Real-world coding challenges designed to test and improve your GitHub Copilot skills across various scenarios and programming languages.

## Table of Contents
1. [Algorithm Implementation](#algorithm-implementation)
2. [Web Development](#web-development)
3. [Data Processing](#data-processing)
4. [System Design](#system-design)
5. [Testing and Debugging](#testing-and-debugging)
6. [Performance Optimization](#performance-optimization)

## Algorithm Implementation

### Challenge 1: Rate Limiter
**Difficulty**: Medium  
**Time**: 30 minutes

**Description**: Implement a sliding window rate limiter that can handle multiple users with different rate limits.

**Requirements**:
- Support multiple algorithms (fixed window, sliding window, token bucket)
- Redis backend for distributed systems
- Configurable rate limits per user/API key
- Detailed logging and metrics

**Starting Prompt**:
```python
# Implement a distributed rate limiter with multiple algorithms
# Requirements:
# - Fixed window: 100 requests per minute
# - Sliding window: 100 requests per 60-second sliding window
# - Token bucket: 10 requests burst, refill 1 per 6 seconds
# - Support different limits per user tier (basic, premium, enterprise)
# - Redis for persistence and distribution
# - Async/await support

import asyncio
import redis.asyncio as redis
from typing import Dict, Optional
from enum import Enum

class RateLimitAlgorithm(Enum):
    FIXED_WINDOW = "fixed_window"
    SLIDING_WINDOW = "sliding_window"
    TOKEN_BUCKET = "token_bucket"

class RateLimiter:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
    
    # TODO: Implement complete rate limiter
```

**Expected Output**: Complete rate limiter implementation with all three algorithms.

### Challenge 2: Graph Algorithm Optimization
**Difficulty**: Hard  
**Time**: 45 minutes

**Description**: Implement an optimized shortest path algorithm for a social network graph.

**Starting Context**:
```javascript
// Social Network Graph Shortest Path
// Find shortest path between two users considering:
// - Friend connections (weight 1)
// - Mutual friends (weight 0.5)
// - Common interests (weight 0.8)
// - Geographic proximity (weight 0.7)

class SocialNetworkGraph {
  constructor() {
    this.nodes = new Map(); // user_id -> User
    this.edges = new Map(); // user_id -> Map(connected_user_id -> weight)
  }
  
  // TODO: Implement optimized shortest path with A* algorithm
}
```

## Web Development

### Challenge 3: Real-time Collaboration System
**Difficulty**: Hard  
**Time**: 60 minutes

**Description**: Create a real-time collaborative document editor with conflict resolution.

**Requirements**:
- WebSocket connections
- Operational Transform for conflict resolution
- User presence indicators
- Offline support with sync

**Starting Framework**:
```typescript
// Real-time collaborative document editor
// Features: Live cursors, conflict resolution, offline support
import { WebSocket } from 'ws';

interface DocumentOperation {
  type: 'insert' | 'delete' | 'retain';
  position: number;
  content?: string;
  length?: number;
  userId: string;
  timestamp: number;
}

class CollaborativeDocument {
  private content: string = '';
  private operations: DocumentOperation[] = [];
  private clients: Map<string, WebSocket> = new Map();
  
  // TODO: Implement operational transform and conflict resolution
}
```

### Challenge 4: E-commerce Cart with Advanced Features
**Difficulty**: Medium  
**Time**: 45 minutes

**Description**: Build a shopping cart system with complex pricing rules and inventory management.

**Features Required**:
- Dynamic pricing based on quantity
- Coupon system with multiple types
- Real-time inventory checking
- Cart persistence across sessions
- Tax calculation by location

**Starting Point**:
```python
# Advanced E-commerce Shopping Cart
# Features: Dynamic pricing, coupons, inventory, tax calculation
from typing import List, Dict, Optional
from decimal import Decimal
from datetime import datetime

class CartItem:
    def __init__(self, product_id: str, quantity: int, price: Decimal):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

class ShoppingCart:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.items: List[CartItem] = []
        self.coupons: List[str] = []
        self.shipping_address = None
    
    # TODO: Implement complete cart system with all features
```

## Data Processing

### Challenge 5: Stream Processing Pipeline
**Difficulty**: Hard  
**Time**: 60 minutes

**Description**: Build a real-time data processing pipeline for IoT sensor data.

**Requirements**:
- Handle 100k+ events per second
- Real-time anomaly detection
- Data aggregation and windowing
- Fault tolerance and recovery

**Starting Setup**:
```rust
// High-performance IoT data processing pipeline
// Process sensor data in real-time with anomaly detection
use tokio::stream::StreamExt;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct SensorReading {
    sensor_id: String,
    timestamp: u64,
    temperature: f64,
    humidity: f64,
    pressure: f64,
    location: (f64, f64), // lat, lng
}

struct StreamProcessor {
    // TODO: Implement high-performance stream processing
}
```

### Challenge 6: Machine Learning Feature Pipeline
**Difficulty**: Medium  
**Time**: 45 minutes

**Description**: Create a feature engineering pipeline for a recommendation system.

**Requirements**:
- Real-time feature computation
- Feature store integration
- A/B testing support
- Model serving pipeline

**Framework**:
```python
# ML Feature Pipeline for Recommendation System
# Real-time feature engineering with A/B testing support
import pandas as pd
import numpy as np
from typing import Dict, List, Any
from datetime import datetime, timedelta

class FeaturePipeline:
    def __init__(self):
        self.feature_store = {}
        self.model_versions = {}
    
    def compute_user_features(self, user_id: str) -> Dict[str, float]:
        # TODO: Implement real-time user feature computation
        pass
    
    # TODO: Complete feature pipeline implementation
```

## System Design

### Challenge 7: Distributed Cache System
**Difficulty**: Hard  
**Time**: 60 minutes

**Description**: Design and implement a distributed caching system with consistent hashing.

**Requirements**:
- Consistent hashing for node distribution
- Replication and fault tolerance
- TTL support with eviction policies
- Monitoring and metrics

**Starting Architecture**:
```go
// Distributed Cache with Consistent Hashing
// Features: Replication, fault tolerance, TTL, monitoring
package main

import (
    "hash/crc32"
    "sort"
    "sync"
    "time"
)

type Node struct {
    ID       string
    Address  string
    IsAlive  bool
}

type DistributedCache struct {
    nodes     []Node
    ring      []uint32
    data      map[string]CacheItem
    replicas  int
    mutex     sync.RWMutex
}

// TODO: Implement complete distributed cache
```

### Challenge 8: Event-Driven Microservices
**Difficulty**: Hard  
**Time**: 90 minutes

**Description**: Design an event-driven microservices architecture for an e-commerce platform.

**Services Required**:
- User Service
- Product Service  
- Order Service
- Payment Service
- Notification Service
- Event Bus (Kafka/RabbitMQ)

**Starting Point**:
```java
// Event-Driven E-commerce Microservices
// Services: User, Product, Order, Payment, Notification
// Event Bus: Apache Kafka integration

@Service
public class OrderService {
    
    @Autowired
    private EventPublisher eventPublisher;
    
    @Autowired
    private PaymentServiceClient paymentClient;
    
    // TODO: Implement event-driven order processing
    public Order createOrder(CreateOrderRequest request) {
        // Implementation with event publishing
    }
}
```

## Testing and Debugging

### Challenge 9: Comprehensive Test Suite Generator
**Difficulty**: Medium  
**Time**: 45 minutes

**Description**: Create a system that generates comprehensive test suites for any given code.

**Requirements**:
- Unit test generation
- Integration test scenarios
- Edge case identification
- Mock generation
- Performance testing

**Test Generator Framework**:
```typescript
// Automated Test Suite Generator
// Analyzes code and generates comprehensive tests
interface CodeAnalysis {
  functions: FunctionInfo[];
  classes: ClassInfo[];
  dependencies: string[];
  complexity: number;
}

class TestSuiteGenerator {
  private codeAnalyzer: CodeAnalyzer;
  
  constructor() {
    this.codeAnalyzer = new CodeAnalyzer();
  }
  
  // TODO: Implement comprehensive test generation
  generateTestSuite(sourceCode: string): TestSuite {
    // Analysis and test generation logic
  }
}
```

### Challenge 10: Debugging Assistant
**Difficulty**: Medium  
**Time**: 40 minutes

**Description**: Build an intelligent debugging assistant that analyzes errors and suggests fixes.

**Features**:
- Error pattern recognition
- Stack trace analysis
- Solution suggestions
- Code fix generation

**Debug Assistant**:
```python
# Intelligent Debugging Assistant
# Analyzes errors and suggests fixes with Copilot assistance
import re
import ast
from typing import List, Dict, Optional

class DebuggingAssistant:
    def __init__(self):
        self.error_patterns = {}
        self.solution_database = {}
    
    def analyze_error(self, error_message: str, stack_trace: str, code: str) -> DebugSuggestion:
        # TODO: Implement intelligent error analysis
        pass
    
    # TODO: Complete debugging assistant
```

## Performance Optimization

### Challenge 11: Database Query Optimizer
**Difficulty**: Hard  
**Time**: 60 minutes

**Description**: Create a system that analyzes and optimizes database queries automatically.

**Requirements**:
- Query execution plan analysis
- Index recommendation
- Query rewriting
- Performance monitoring

**Optimizer Framework**:
```sql
-- Database Query Optimizer
-- Analyzes slow queries and suggests optimizations

-- Example slow query to optimize:
SELECT 
    u.name,
    COUNT(o.id) as order_count,
    SUM(oi.quantity * p.price) as total_spent,
    AVG(r.rating) as avg_rating
FROM users u
LEFT JOIN orders o ON u.id = o.customer_id
LEFT JOIN order_items oi ON o.id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.id
LEFT JOIN reviews r ON p.id = r.product_id
WHERE o.created_at >= '2023-01-01'
GROUP BY u.id, u.name
HAVING COUNT(o.id) > 5
ORDER BY total_spent DESC
LIMIT 100;

-- TODO: Implement query optimization analysis
```

### Challenge 12: Memory and CPU Profiler
**Difficulty**: Medium  
**Time**: 45 minutes

**Description**: Build a performance profiler that identifies bottlenecks and suggests optimizations.

**Profiler System**:
```python
# Performance Profiler and Optimizer
# Identifies memory leaks, CPU bottlenecks, and optimization opportunities
import cProfile
import tracemalloc
import psutil
from typing import Dict, List

class PerformanceProfiler:
    def __init__(self):
        self.cpu_profiler = cProfile.Profile()
        self.memory_tracker = None
    
    def start_profiling(self):
        # TODO: Implement comprehensive performance profiling
        pass
    
    def analyze_performance(self) -> PerformanceReport:
        # TODO: Generate performance analysis and optimization suggestions
        pass
```

## Evaluation Criteria

### Scoring Rubric (100 points total)

**Functionality (40 points)**
- Code correctness and completeness
- Requirement fulfillment
- Error handling

**Code Quality (25 points)**
- Clean, readable code
- Proper naming conventions
- Documentation and comments

**Copilot Usage (20 points)**
- Effective prompt engineering
- Leveraging AI suggestions appropriately
- Iterative improvement with Copilot

**Performance & Best Practices (15 points)**
- Efficient algorithms and data structures
- Security considerations
- Scalability and maintainability

### Time Management Tips

1. **Read requirements carefully** (5 minutes)
2. **Plan your approach** (5 minutes)
3. **Start with basic structure** (10 minutes)
4. **Use Copilot for implementation** (60-70% of time)
5. **Test and refine** (remaining time)

## Solution Guidelines

### Effective Copilot Prompts

**Good Prompts:**
- "Implement a rate limiter using sliding window algorithm with Redis backend"
- "Create comprehensive unit tests for the user authentication service with edge cases"
- "Optimize this database query for better performance with proper indexing"

**Poor Prompts:**
- "Write code"
- "Fix this"
- "Make it better"

### Best Practices

1. **Start with comments** describing requirements
2. **Use descriptive variable and function names**
3. **Break complex problems into smaller parts**
4. **Iterate on Copilot suggestions**
5. **Always review and understand generated code**

## Certification Readiness

Complete **8 out of 12 challenges** with a score of 80+ to demonstrate certification readiness.

**Next Steps:**
1. Practice with additional coding challenges
2. Review and understand all generated code
3. Take practice exams
4. Schedule certification exam

## Additional Resources

- [Competitive Programming Platforms](https://codeforces.com/)
- [System Design Interviews](https://github.com/donnemartin/system-design-primer)
- [Algorithm Visualization](https://visualgo.net/)
- [Performance Testing Tools](https://k6.io/)
