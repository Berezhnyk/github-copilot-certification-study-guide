# Advanced GitHub Copilot Practice Exercises

## Overview
Advanced exercises designed to test comprehensive GitHub Copilot skills across complex scenarios, enterprise features, and real-world applications.

## Table of Contents
1. [Advanced Prompt Engineering](#advanced-prompt-engineering)
2. [Enterprise Integration](#enterprise-integration)
3. [Multi-Language Projects](#multi-language-projects)
4. [Performance Optimization](#performance-optimization)
5. [Security and Compliance](#security-and-compliance)
6. [Team Collaboration](#team-collaboration)

## Advanced Prompt Engineering

### Exercise 1: Context-Aware API Development

**Scenario**: You're building a microservices architecture for an e-commerce platform. Create a sophisticated product recommendation API that considers user behavior, inventory, and business rules.

**Requirements**:
- Use TypeScript with Express.js
- Implement caching with Redis
- Add rate limiting and authentication
- Include comprehensive error handling
- Write unit and integration tests

**Starting Prompt**:
```typescript
// E-commerce Product Recommendation API
// Requirements:
// - Personalized recommendations based on user history
// - Real-time inventory checking
// - A/B testing support for recommendation algorithms
// - Caching layer for performance
// - Rate limiting per user tier
// - JWT authentication with role-based access

import express from 'express';
import Redis from 'ioredis';

interface User {
  id: string;
  tier: 'basic' | 'premium' | 'enterprise';
  preferences: UserPreferences;
  purchaseHistory: PurchaseHistory[];
}

interface RecommendationRequest {
  userId: string;
  category?: string;
  limit?: number;
  algorithm?: 'collaborative' | 'content-based' | 'hybrid';
}

// TODO: Implement complete recommendation service
```

**Expected Outcome**: Copilot should generate a comprehensive API with all required features, demonstrating advanced context understanding.

### Exercise 2: Machine Learning Pipeline

**Scenario**: Create a complete ML pipeline for fraud detection in financial transactions.

**Starting Context**:
```python
# Fraud Detection ML Pipeline
# Dataset: Financial transactions with features like amount, merchant, time, location
# Requirements:
# - Real-time feature engineering
# - Multiple model ensemble (Random Forest, XGBoost, Neural Network)
# - Model versioning and A/B testing
# - Explainable AI for compliance
# - Real-time scoring API

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import tensorflow as tf

class FraudDetectionPipeline:
    def __init__(self):
        self.models = {}
        self.feature_columns = []
        self.model_version = "1.0.0"
    
    # TODO: Implement complete fraud detection system
```

**Challenge**: Use advanced prompts to guide Copilot in creating a production-ready ML system.

## Enterprise Integration

### Exercise 3: GitHub Copilot for Business Implementation

**Scenario**: You're implementing GitHub Copilot for Business in a large enterprise with specific compliance requirements.

**Tasks**:
1. Configure content exclusions for sensitive repositories
2. Set up audit logging and monitoring
3. Create policy templates for different teams
4. Implement usage analytics dashboard

**Configuration Exercise**:
```yaml
# .github/copilot-config.yml
# Enterprise configuration for GitHub Copilot
# Requirements:
# - Exclude all repositories containing customer data
# - Block suggestions for files with financial information
# - Enable audit logging for compliance
# - Configure different policies for different teams

organization:
  name: "enterprise-corp"
  policies:
    # TODO: Configure comprehensive enterprise policies
```

**Deliverable**: Complete enterprise configuration with documentation.

### Exercise 4: Multi-Tenant SaaS Platform

**Scenario**: Build a multi-tenant SaaS platform with GitHub Copilot assistance.

**Requirements**:
- Tenant isolation at database and application level
- Role-based access control
- Usage analytics per tenant
- Configurable features per tenant
- Compliance with SOC 2 and GDPR

**Starting Point**:
```python
# Multi-Tenant SaaS Platform
# Architecture: Database per tenant with shared application layer
# Features: User management, billing, analytics, feature flags

from sqlalchemy import create_engine
from fastapi import FastAPI, Depends, HTTPException
from typing import Dict, List, Optional

class TenantManager:
    def __init__(self):
        self.tenant_configs: Dict[str, TenantConfig] = {}
        self.database_connections: Dict[str, Any] = {}
    
    # TODO: Implement complete multi-tenant architecture
```

## Multi-Language Projects

### Exercise 5: Full-Stack Application with Multiple Languages

**Scenario**: Create a real-time collaboration platform using multiple programming languages.

**Architecture**:
- Frontend: React with TypeScript
- Backend API: Python with FastAPI
- Real-time: Node.js with Socket.IO
- Database: PostgreSQL with Redis
- Mobile: React Native
- Infrastructure: Docker and Kubernetes

**Challenge**: Use Copilot to maintain consistency across languages and implement complex inter-service communication.

**Frontend Component**:
```typescript
// Real-time collaborative document editor
// Features: Live cursors, conflict resolution, offline support
import React, { useState, useEffect } from 'react';
import { useWebSocket } from './hooks/useWebSocket';

interface DocumentEditor {
  documentId: string;
  userId: string;
  permissions: EditorPermissions;
}

const CollaborativeEditor: React.FC<DocumentEditor> = ({ documentId, userId, permissions }) => {
  // TODO: Implement real-time collaborative editing
};
```

**Backend Service**:
```python
# Document collaboration service
# Features: Operational transforms, conflict resolution, real-time sync
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict
import asyncio

class DocumentCollaborationService:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}
        self.documents: Dict[str, Document] = {}
    
    # TODO: Implement collaborative editing backend
```

### Exercise 6: Microservices Communication

**Scenario**: Implement a complex microservices system with event-driven architecture.

**Services**:
- User Service (Go)
- Order Service (Java/Spring Boot)
- Payment Service (Python)
- Notification Service (Node.js)
- Event Bus (Apache Kafka)

**Go Service**:
```go
// User Management Service in Go
// Features: Authentication, user profiles, preferences
package main

import (
    "github.com/gin-gonic/gin"
    "gorm.io/gorm"
)

type UserService struct {
    db     *gorm.DB
    router *gin.Engine
}

// TODO: Implement complete user service with event publishing
```

## Performance Optimization

### Exercise 7: High-Performance Data Processing

**Scenario**: Build a system that processes millions of events per second.

**Requirements**:
- Streaming data processing
- Real-time analytics
- Horizontal scaling
- Sub-millisecond latency
- Fault tolerance

**Starting Point**:
```rust
// High-performance event processing system in Rust
// Requirements: Process 1M+ events/second with <1ms latency
use tokio::stream::StreamExt;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct Event {
    id: String,
    timestamp: u64,
    event_type: String,
    payload: serde_json::Value,
}

pub struct EventProcessor {
    // TODO: Implement high-performance event processing
}
```

### Exercise 8: Database Optimization Challenge

**Scenario**: Optimize a slow-performing e-commerce database.

**Given**:
```sql
-- Slow performing queries that need optimization
-- Customer orders with products and reviews
SELECT 
    c.name,
    COUNT(o.id) as order_count,
    SUM(oi.quantity * p.price) as total_spent,
    AVG(r.rating) as avg_rating
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
LEFT JOIN order_items oi ON o.id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.id
LEFT JOIN reviews r ON p.id = r.product_id
WHERE o.created_at >= '2023-01-01'
GROUP BY c.id, c.name
HAVING COUNT(o.id) > 5
ORDER BY total_spent DESC
LIMIT 100;
```

**Tasks**:
1. Identify performance bottlenecks
2. Create optimized indexes
3. Rewrite queries for better performance
4. Implement query caching strategy
5. Design data archiving strategy

## Security and Compliance

### Exercise 9: Secure Application Development

**Scenario**: Build a healthcare application that must comply with HIPAA.

**Requirements**:
- End-to-end encryption
- Audit logging for all data access
- Role-based access control
- Secure API authentication
- Data anonymization capabilities

**Security Framework**:
```python
# HIPAA-compliant healthcare application
# Requirements: PHI protection, audit trails, secure communications
from cryptography.fernet import Fernet
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

class SecureHealthcareAPI:
    def __init__(self):
        self.encryption_key = self.load_encryption_key()
        self.audit_logger = AuditLogger()
    
    # TODO: Implement complete secure healthcare system
```

### Exercise 10: Content Filtering and Privacy

**Scenario**: Implement advanced content filtering for GitHub Copilot in a regulated industry.

**Requirements**:
- Custom content exclusion patterns
- Real-time privacy violation detection
- Automated compliance reporting
- Integration with enterprise security tools

**Implementation**:
```typescript
// Advanced content filtering system
// Detects and prevents sensitive data suggestions
interface ContentFilter {
  patterns: RegExp[];
  severity: 'low' | 'medium' | 'high' | 'critical';
  action: 'warn' | 'block' | 'log';
}

class AdvancedContentFilter {
  private filters: Map<string, ContentFilter[]> = new Map();
  
  // TODO: Implement sophisticated content filtering
}
```

## Team Collaboration

### Exercise 11: Code Review Automation

**Scenario**: Create an intelligent code review system that integrates with GitHub Copilot.

**Features**:
- Automated code quality analysis
- Security vulnerability detection
- Performance impact assessment
- Test coverage analysis
- Documentation quality check

**System Design**:
```python
# Intelligent Code Review System
# Integrates with GitHub Copilot for enhanced review capabilities
from github import Github
from typing import List, Dict, Any

class IntelligentCodeReview:
    def __init__(self, github_token: str):
        self.github = Github(github_token)
        self.analyzers = self.load_analyzers()
    
    async def analyze_pull_request(self, repo: str, pr_number: int) -> ReviewResult:
        # TODO: Implement comprehensive PR analysis
        pass
```

### Exercise 12: Documentation Generation Pipeline

**Scenario**: Build an automated documentation system that uses Copilot to generate comprehensive project documentation.

**Requirements**:
- API documentation from code
- README generation
- Architecture diagrams
- Usage examples
- Deployment guides

**Generator System**:
```typescript
// Automated documentation generation system
// Uses Copilot to create comprehensive project documentation
interface DocumentationConfig {
  projectType: 'web' | 'mobile' | 'api' | 'library';
  frameworks: string[];
  deploymentTargets: string[];
  audience: 'developers' | 'end-users' | 'both';
}

class DocumentationGenerator {
  // TODO: Implement automated documentation generation
}
```

## Assessment Criteria

### Scoring Rubric

**Advanced Prompt Engineering (25 points)**
- Context awareness and prompt optimization
- Complex requirement handling
- Multi-step problem solving

**Enterprise Features (25 points)**
- Security and compliance implementation
- Content exclusion configuration
- Audit and monitoring setup

**Technical Implementation (25 points)**
- Code quality and architecture
- Performance optimization
- Error handling and testing

**Innovation and Creativity (25 points)**
- Novel use of Copilot features
- Creative problem-solving approaches
- Integration of multiple technologies

### Certification Readiness

To be certification-ready, you should be able to:

1. **Complete 80% of exercises successfully**
2. **Demonstrate advanced prompt engineering skills**
3. **Implement enterprise-grade security measures**
4. **Show proficiency across multiple programming languages**
5. **Design scalable and maintainable systems**
6. **Integrate Copilot into complex development workflows**

## Next Steps

1. Complete exercises in order of increasing difficulty
2. Document your solutions and learning insights
3. Practice explaining your approach to others
4. Create your own advanced scenarios
5. Contribute to open-source projects using Copilot
6. Prepare for the certification exam with mock questions

## Additional Resources

- [GitHub Copilot Enterprise Documentation](https://docs.github.com/en/copilot/github-copilot-enterprise)
- [Advanced Prompt Engineering Guide](../study-materials/02-prompt-engineering.md)
- [Security Best Practices](../study-materials/08-privacy-fundamentals.md)
- [Performance Optimization Patterns](../code-examples/prompt-patterns.md)
