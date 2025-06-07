# Emerging Features Practice Exercises

## Overview
Advanced practice exercises specifically designed to test proficiency with GitHub Copilot's newest features introduced in 2024-2025. These exercises complement the main advanced exercises and focus on cutting-edge capabilities.

## Table of Contents
1. [Copilot Spaces Mastery](#copilot-spaces-mastery)
2. [Coding Agent Integration](#coding-agent-integration)
3. [Extension Development](#extension-development)
4. [MCP Server Implementation](#mcp-server-implementation)
5. [Custom Instructions Optimization](#custom-instructions-optimization)
6. [Multi-Model Workflows](#multi-model-workflows)

---

## Copilot Spaces Mastery

### Exercise 1: Microservices Space Setup

**Scenario**: Create a comprehensive Copilot Space for a distributed e-commerce platform with 5 microservices.

**Requirements**:
- User Authentication Service (Node.js)
- Product Catalog Service (Python)
- Order Management Service (Java)
- Payment Processing Service (Go)
- Notification Service (TypeScript)

**Tasks**:
1. Set up Copilot Space with all repositories
2. Implement cross-service API calls
3. Create shared type definitions
4. Test context awareness across services

**Starting Configuration**:
```yaml
# copilot-space.yml
name: "ecommerce-platform"
description: "Distributed e-commerce microservices"
repositories:
  - auth-service
  - product-catalog
  - order-management
  - payment-processing
  - notification-service
shared_context:
  - api-contracts/
  - shared-types/
  - documentation/
```

**Expected Outcomes**:
- Copilot suggests consistent API patterns across services
- Cross-service type safety maintained
- Shared error handling patterns emerge
- Documentation stays synchronized

### Exercise 2: Space-Wide Refactoring

**Challenge**: Use Copilot Spaces to perform a major architectural change across multiple repositories.

**Scenario**: Migrate from REST to GraphQL across all services while maintaining backward compatibility.

**Implementation Guide**:
```typescript
// Task: Create GraphQL schema that unifies all services
// Copilot should understand service boundaries and suggest appropriate resolvers

// auth-service/schema.graphql
type User {
  id: ID!
  email: String!
  profile: UserProfile
  orders: [Order!]! # Should suggest connection to order-service
}

// order-service/schema.graphql  
type Order {
  id: ID!
  user: User! # Should understand auth-service User type
  items: [OrderItem!]!
  payment: Payment # Should connect to payment-service
}

// Let Copilot generate resolvers that respect service boundaries
```

---

## Coding Agent Integration

### Exercise 3: Agent-Driven Feature Development

**Scenario**: Use the Copilot Coding Agent to implement a complete user wishlist feature.

**Setup**:
1. Create GitHub issue with detailed requirements
2. Assign issue to @copilot
3. Monitor and guide the implementation process
4. Review and refine the generated code

**Issue Template**:
```markdown
# User Wishlist Feature Implementation

## Requirements
- Users can add/remove products to/from wishlist
- Wishlist is persistent across sessions
- Share wishlist functionality
- Email notifications for price drops
- Mobile-responsive UI

## Acceptance Criteria
- [ ] Database schema for wishlists
- [ ] RESTful API endpoints
- [ ] Frontend React components
- [ ] Unit and integration tests
- [ ] Documentation updated

## Technical Constraints
- Use existing authentication system
- Follow current API patterns
- Maintain 80%+ test coverage
- Mobile-first responsive design

@copilot please implement this feature
```

**Agent Monitoring Checklist**:
- [ ] Agent understood requirements correctly
- [ ] Implementation follows project patterns
- [ ] Tests are comprehensive
- [ ] Code quality meets standards
- [ ] Documentation is complete

### Exercise 4: Automated Bug Resolution

**Challenge**: Configure the Coding Agent to automatically handle specific types of bugs.

**Configuration**:
```yaml
# .github/copilot-agent-config.yml
automation:
  auto_fix:
    enabled: true
    labels: ["bug", "automated-fix"]
    conditions:
      - test_failures: true
      - security_issues: false
      - breaking_changes: false
  
  review_requirements:
    human_approval: true
    reviewers: ["@senior-devs"]
    auto_merge: false
  
  testing:
    run_full_suite: true
    require_passing: true
    coverage_threshold: 80
```

**Test Scenarios**:
1. Create bugs that should be auto-fixed
2. Create bugs that require human intervention
3. Verify agent respects configuration limits
4. Test escalation procedures

---

## Extension Development

### Exercise 5: Company Knowledge Base Extension

**Objective**: Build a Copilot Extension that integrates your company's internal knowledge base.

**Architecture**:
```typescript
// src/extension.ts
import { CopilotExtension, ChatContext, ExtensionResponse } from '@github/copilot-sdk';

export class KnowledgeBaseExtension extends CopilotExtension {
  constructor(private knowledgeBaseAPI: KnowledgeBaseAPI) {
    super({
      name: "company-kb",
      description: "Access company documentation and best practices",
      version: "1.0.0"
    });
  }

  async handleChat(message: string, context: ChatContext): Promise<ExtensionResponse> {
    // Parse intent from message
    const intent = await this.parseIntent(message);
    
    switch (intent.type) {
      case 'search':
        return await this.searchKnowledgeBase(intent.query);
      case 'policy':
        return await this.getPolicyInfo(intent.domain);
      case 'examples':
        return await this.getCodeExamples(intent.technology);
      default:
        return this.getHelpMessage();
    }
  }

  private async searchKnowledgeBase(query: string): Promise<ExtensionResponse> {
    const results = await this.knowledgeBaseAPI.search(query);
    
    return {
      type: 'markdown',
      content: this.formatSearchResults(results),
      actions: [
        {
          label: "Open Full Article",
          action: "open_url",
          url: results[0]?.url
        }
      ]
    };
  }
}
```

**Testing Framework**:
```typescript
// tests/extension.test.ts
describe('KnowledgeBase Extension', () => {
  let extension: KnowledgeBaseExtension;
  let mockAPI: jest.Mocked<KnowledgeBaseAPI>;

  beforeEach(() => {
    mockAPI = createMockKnowledgeBaseAPI();
    extension = new KnowledgeBaseExtension(mockAPI);
  });

  test('should search knowledge base', async () => {
    mockAPI.search.mockResolvedValue([
      { title: 'API Guidelines', url: 'https://internal/api-guidelines' }
    ]);

    const response = await extension.handleChat(
      'How should I structure REST APIs?',
      createMockContext()
    );

    expect(response.content).toContain('API Guidelines');
    expect(mockAPI.search).toHaveBeenCalledWith('REST APIs structure');
  });
});
```

### Exercise 6: Development Tools Integration

**Challenge**: Create an extension that integrates with your CI/CD pipeline and monitoring tools.

**Features to Implement**:
- Build status queries
- Deployment information
- Performance metrics
- Error tracking integration
- Log analysis

**Example Usage**:
```
@devtools show build status for feature-branch

@devtools deploy staging environment

@devtools check performance metrics for user-service

@devtools analyze recent errors in production
```

---

## MCP Server Implementation

### Exercise 7: Database Schema MCP Server

**Objective**: Create an MCP server that provides Copilot with access to your database schema and query capabilities.

**Implementation**:
```python
# database_mcp_server.py
import asyncio
from mcp import MCPServer, Resource, Tool
from sqlalchemy import create_engine, inspect

class DatabaseMCPServer(MCPServer):
    def __init__(self, connection_string: str):
        super().__init__("database-schema")
        self.engine = create_engine(connection_string)
        self.inspector = inspect(self.engine)
    
    async def list_resources(self) -> list[Resource]:
        """List all database tables as resources"""
        tables = self.inspector.get_table_names()
        return [
            Resource(
                uri=f"db://tables/{table}",
                name=f"Table: {table}",
                mimeType="application/json",
                description=f"Schema information for {table} table"
            )
            for table in tables
        ]
    
    async def read_resource(self, uri: str) -> str:
        """Read table schema information"""
        if uri.startswith("db://tables/"):
            table_name = uri.split("/")[-1]
            columns = self.inspector.get_columns(table_name)
            indexes = self.inspector.get_indexes(table_name)
            foreign_keys = self.inspector.get_foreign_keys(table_name)
            
            schema_info = {
                "table": table_name,
                "columns": columns,
                "indexes": indexes,
                "foreign_keys": foreign_keys
            }
            
            return json.dumps(schema_info, indent=2)
    
    async def call_tool(self, name: str, arguments: dict) -> str:
        """Execute database tools"""
        if name == "explain_query":
            return await self.explain_query(arguments["query"])
        elif name == "suggest_indexes":
            return await self.suggest_indexes(arguments["table"])
        elif name == "generate_migration":
            return await self.generate_migration(arguments["changes"])
    
    async def explain_query(self, query: str) -> str:
        """Explain query execution plan"""
        with self.engine.connect() as conn:
            result = conn.execute(f"EXPLAIN {query}")
            return "\n".join([str(row) for row in result])
```

**Usage Examples**:
```sql
-- Copilot can now understand your database schema
-- and suggest appropriate queries

-- Query suggestion based on schema
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name
HAVING COUNT(o.id) > 5;

-- Index suggestions
-- Copilot can suggest: "Consider adding index on orders(user_id, created_at)"
```

### Exercise 8: API Documentation MCP Server

**Challenge**: Build an MCP server that provides live API documentation and testing capabilities.

**Features**:
- OpenAPI/Swagger integration
- Live endpoint testing
- Response validation
- Code generation from schemas

---

## Custom Instructions Optimization

### Exercise 9: Team-Specific Instructions

**Scenario**: Create a comprehensive set of custom instructions for different team roles.

**Frontend Team Instructions**:
```markdown
# Frontend Development Guidelines

## React Patterns
- Use functional components with hooks
- Implement proper error boundaries
- Follow atomic design principles
- Use TypeScript for all components

## State Management
- Use React Query for server state
- Use Zustand for client state
- Avoid prop drilling
- Implement optimistic updates

## Styling
- Use Tailwind CSS utility classes
- Follow mobile-first responsive design
- Implement dark mode support
- Use CSS-in-JS sparingly

## Testing
- Write React Testing Library tests
- Aim for 80% component coverage
- Test user interactions, not implementation
- Mock external dependencies

## Performance
- Implement code splitting
- Use React.memo for expensive components
- Optimize bundle size
- Implement lazy loading
```

**Backend Team Instructions**:
```markdown
# Backend Development Guidelines

## API Design
- Follow RESTful conventions
- Use OpenAPI/Swagger documentation
- Implement proper HTTP status codes
- Version APIs appropriately

## Database
- Use migrations for schema changes
- Implement proper indexing
- Follow normalization principles
- Use connection pooling

## Security
- Validate all inputs
- Implement proper authentication
- Use parameterized queries
- Log security events

## Error Handling
- Use structured error responses
- Implement circuit breakers
- Add proper logging and monitoring
- Handle edge cases gracefully
```

### Exercise 10: Project-Specific Adaptations

**Challenge**: Create repository-specific instructions that adapt to different project types.

**Machine Learning Project**:
```markdown
# ML Project Guidelines

## Data Science Workflow
- Use Jupyter notebooks for exploration
- Implement reproducible pipelines
- Version control datasets
- Document model assumptions

## Model Development
- Start with baseline models
- Use cross-validation
- Track experiments with MLflow
- Implement model versioning

## Code Quality
- Follow PEP 8 for Python
- Use type hints
- Write comprehensive docstrings
- Implement unit tests for utilities
```

---

## Multi-Model Workflows

### Exercise 11: Model Selection Strategy

**Objective**: Design workflows that leverage different AI models for optimal results.

**Workflow Design**:
```typescript
// Model selection strategy
interface ModelWorkflow {
  task: 'generation' | 'analysis' | 'refactoring' | 'documentation';
  primaryModel: AIModel;
  fallbackModel?: AIModel;
  validationModel?: AIModel;
}

const workflows: ModelWorkflow[] = [
  {
    task: 'generation',
    primaryModel: 'codellama',
    fallbackModel: 'gpt-4',
    validationModel: 'claude-3'
  },
  {
    task: 'analysis',
    primaryModel: 'gpt-4',
    validationModel: 'claude-3'
  },
  {
    task: 'refactoring',
    primaryModel: 'claude-3',
    fallbackModel: 'gpt-4'
  },
  {
    task: 'documentation',
    primaryModel: 'claude-3',
    validationModel: 'gpt-4'
  }
];
```

**Implementation Example**:
```javascript
// Automated model selection based on task
async function processCodeRequest(request: CodeRequest): Promise<CodeResponse> {
  const workflow = selectWorkflow(request.type);
  
  try {
    // Primary model attempt
    const result = await invokeModel(workflow.primaryModel, request);
    
    // Validation if required
    if (workflow.validationModel) {
      const validation = await validateResult(workflow.validationModel, result);
      if (!validation.passed) {
        throw new Error('Validation failed');
      }
    }
    
    return result;
  } catch (error) {
    // Fallback model
    if (workflow.fallbackModel) {
      return await invokeModel(workflow.fallbackModel, request);
    }
    throw error;
  }
}
```

### Exercise 12: Performance Optimization Testing

**Challenge**: Test and measure the effectiveness of different model combinations for various coding tasks.

**Metrics to Track**:
- Code quality scores
- Execution time
- Memory usage
- Test coverage
- Security vulnerability detection
- Developer satisfaction ratings

---

## Assessment Criteria

### Emerging Features Mastery (100 points)

**Copilot Spaces (20 points)**
- Effective space organization and configuration
- Cross-repository context utilization
- Collaborative workflow implementation

**Coding Agent Integration (20 points)**
- Proper issue assignment and monitoring
- Configuration optimization
- Quality control processes

**Extension Development (20 points)**
- Functional extension implementation
- Proper integration testing
- User experience design

**MCP Server Implementation (20 points)**
- Server architecture and performance
- Resource and tool implementation
- Integration quality

**Custom Instructions (10 points)**
- Team-specific guideline creation
- Project adaptation strategies
- Instruction effectiveness

**Multi-Model Workflows (10 points)**
- Strategic model selection
- Performance optimization
- Quality measurement

### Certification Readiness Indicators

To demonstrate mastery of emerging features:

1. **Successfully configure and use Copilot Spaces** for complex projects
2. **Effectively leverage the Coding Agent** for automated development tasks
3. **Build functional Copilot Extensions** that integrate with existing tools
4. **Implement MCP servers** that enhance Copilot's capabilities
5. **Create comprehensive custom instructions** for different contexts
6. **Design multi-model workflows** for optimal performance

---

## Next Steps

1. Complete exercises in order of complexity
2. Document your implementation approaches
3. Test with real-world scenarios
4. Share learnings with your team
5. Contribute to the GitHub Copilot community
6. Stay updated with emerging features

---

*These exercises focus on the cutting-edge capabilities of GitHub Copilot as of 2025. Continue monitoring GitHub's official documentation for the latest feature updates.*

---
*Return to: [Advanced Exercises](./advanced-exercises.md) | [Study Materials](../study-materials/) | [README](../README.md)*
