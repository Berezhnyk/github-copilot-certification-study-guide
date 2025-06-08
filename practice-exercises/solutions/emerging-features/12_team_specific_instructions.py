"""
Team-Specific Custom Instructions - Frontend and Backend Guidelines
TODO: Create comprehensive custom instructions for different team roles and contexts
This exercise demonstrates optimizing Copilot behavior through targeted instructions
"""

# TODO: Ask Copilot to help optimize these instructions for maximum effectiveness

# Frontend Team Custom Instructions
FRONTEND_INSTRUCTIONS = """
# Frontend Development Guidelines for GitHub Copilot

## Core Principles
- Always prioritize user experience and accessibility
- Follow mobile-first responsive design principles
- Implement progressive enhancement strategies
- Ensure cross-browser compatibility
- Focus on performance optimization

## React Development Patterns
### Component Architecture
- Use functional components with hooks exclusively
- Implement proper component composition over inheritance
- Follow atomic design principles (atoms, molecules, organisms, templates, pages)
- Create reusable, single-responsibility components
- Use TypeScript for all React components with proper typing

### State Management
- Use React Query (TanStack Query) for server state management
- Use Zustand for client-side state management
- Implement optimistic updates for better UX
- Avoid prop drilling by using context or state management appropriately
- Use useCallback and useMemo for performance optimization

### Error Handling
- Implement Error Boundaries for graceful error handling
- Use React Hook Form for form validation and error states
- Provide meaningful error messages to users
- Log errors to monitoring service (Sentry, LogRocket)
- Implement fallback UI components

## Styling Guidelines
### CSS Architecture
- Use Tailwind CSS utility classes as primary styling method
- Follow mobile-first responsive design with Tailwind breakpoints
- Implement CSS-in-JS sparingly, only for dynamic styles
- Use CSS custom properties for theme management
- Implement dark mode support with CSS variables

### Design System
- Follow established design tokens and spacing scale
- Use consistent typography scale and font weights
- Implement consistent color palette with semantic naming
- Use standardized component variants and sizes
- Maintain visual hierarchy through typography and spacing

## Testing Standards
### Component Testing
- Write React Testing Library tests for all components
- Focus on testing user interactions, not implementation details
- Aim for 80% code coverage minimum for components
- Test accessibility features and ARIA attributes
- Mock external dependencies and API calls

### Test Structure
- Use describe blocks to group related tests
- Write descriptive test names that explain the expected behavior
- Follow Arrange-Act-Assert pattern in test implementation
- Use data-testid attributes sparingly, prefer accessible queries
- Implement visual regression tests for critical UI components

## Performance Optimization
### Bundle Optimization
- Implement code splitting with React.lazy and Suspense
- Use dynamic imports for non-critical dependencies
- Optimize bundle size with tree shaking
- Implement proper image optimization and lazy loading
- Use service workers for caching strategies

### Runtime Performance
- Use React.memo for expensive components
- Implement virtualization for large lists
- Optimize re-renders with useCallback and useMemo
- Monitor and optimize Core Web Vitals
- Implement proper loading states and skeleton screens

## Accessibility Requirements
### WCAG Compliance
- Ensure WCAG 2.1 AA compliance for all components
- Implement proper semantic HTML structure
- Use ARIA attributes appropriately for complex interactions
- Ensure keyboard navigation for all interactive elements
- Test with screen readers and accessibility tools

### Inclusive Design
- Implement proper color contrast ratios
- Support reduced motion preferences
- Provide alternative text for images and icons
- Ensure forms are properly labeled and validated
- Support high contrast mode and zoom up to 200%

## Code Quality Standards
### TypeScript Usage
- Use strict TypeScript configuration
- Define proper interfaces for all props and state
- Use discriminated unions for complex state management
- Implement proper error handling with Result types
- Use generic types for reusable components

### Code Organization
- Follow consistent file and folder naming conventions
- Group related components in feature folders
- Separate business logic from presentation components
- Use custom hooks for reusable stateful logic
- Implement proper barrel exports for clean imports

## When writing code, always:
1. Consider mobile users first in your implementation
2. Implement proper loading and error states
3. Add TypeScript types for all props and state
4. Include accessibility attributes (ARIA labels, roles)
5. Write accompanying tests for new components
6. Optimize for performance and bundle size
7. Follow established design system patterns
8. Document complex logic with clear comments
"""

# Backend Team Custom Instructions  
BACKEND_INSTRUCTIONS = """
# Backend Development Guidelines for GitHub Copilot

## Core Principles
- Design APIs with consistency and developer experience in mind
- Implement comprehensive error handling and logging
- Prioritize security in all implementation decisions
- Follow database best practices and optimization strategies
- Build scalable and maintainable system architecture

## API Design Standards
### RESTful Conventions
- Follow REST principles consistently across all endpoints
- Use appropriate HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Implement proper HTTP status codes for all responses
- Use consistent URL patterns and resource naming
- Version APIs appropriately (/v1/, /v2/) for backward compatibility

### Request/Response Format
- Use JSON for all API communications
- Implement consistent response envelope structure
- Include pagination metadata for list endpoints
- Use snake_case for JSON field names
- Implement proper content-type headers

### OpenAPI Documentation
- Document all endpoints with OpenAPI/Swagger specifications
- Include request/response examples for all endpoints
- Document error responses and status codes
- Provide clear parameter descriptions and constraints
- Maintain up-to-date API documentation

## Database Management
### Schema Design
- Follow database normalization principles (3NF minimum)
- Use appropriate data types for optimal storage
- Implement proper indexing strategies for query performance
- Design for data integrity with constraints and foreign keys
- Use UUID primary keys for distributed systems

### Query Optimization
- Use parameterized queries to prevent SQL injection
- Implement proper connection pooling
- Use database migrations for schema changes
- Monitor and optimize slow queries
- Implement proper database backup and recovery strategies

### ORM Best Practices
- Use eager loading to prevent N+1 query problems
- Implement proper transaction management
- Use database-specific optimizations when appropriate
- Monitor ORM-generated queries for performance
- Implement proper data validation at the application layer

## Security Implementation
### Authentication & Authorization
- Implement proper JWT token handling and validation
- Use bcrypt or similar for password hashing
- Implement role-based access control (RBAC)
- Use secure session management practices
- Implement proper logout and token revocation

### Input Validation
- Validate and sanitize all user inputs
- Use schema validation libraries (Joi, Yup, Zod)
- Implement rate limiting for API endpoints
- Sanitize data before database operations
- Use HTTPS for all communications

### Data Protection
- Encrypt sensitive data at rest and in transit
- Implement proper key management strategies
- Follow GDPR and data privacy regulations
- Use secure environment variable management
- Implement audit logging for sensitive operations

## Error Handling & Logging
### Structured Error Responses
- Use consistent error response format across all endpoints
- Implement proper error codes and messages
- Include correlation IDs for request tracing
- Provide helpful error messages for client developers
- Log errors with appropriate severity levels

### Monitoring & Observability
- Implement structured logging with JSON format
- Use correlation IDs for distributed tracing
- Monitor application performance and metrics
- Set up proper alerting for critical errors
- Implement health check endpoints

## Performance & Scalability
### Caching Strategies
- Implement appropriate caching layers (Redis, Memcached)
- Use cache invalidation strategies
- Implement proper cache key naming conventions
- Monitor cache hit rates and performance
- Use CDN for static content delivery

### Asynchronous Processing
- Use message queues for long-running operations
- Implement proper job queue management
- Use background workers for intensive tasks
- Implement proper retry mechanisms with exponential backoff
- Monitor queue depth and processing times

## Code Quality Standards
### Testing Strategy
- Write unit tests for all business logic
- Implement integration tests for API endpoints
- Use test doubles (mocks, stubs) appropriately
- Achieve minimum 80% test coverage
- Implement contract testing for external APIs

### Code Organization
- Follow clean architecture principles
- Implement proper separation of concerns
- Use dependency injection for loose coupling
- Follow SOLID principles in class design
- Implement proper configuration management

## When writing code, always:
1. Validate all inputs at the API boundary
2. Implement proper error handling with meaningful messages
3. Use parameterized queries for all database operations
4. Add comprehensive logging for debugging and monitoring
5. Include unit tests for all business logic
6. Follow security best practices for authentication and authorization
7. Implement proper configuration management
8. Document complex business logic with clear comments
9. Use appropriate design patterns for the problem domain
10. Consider scalability and performance implications
"""

# Machine Learning Project Instructions
ML_PROJECT_INSTRUCTIONS = """
# Machine Learning Project Guidelines for GitHub Copilot

## Data Science Workflow
### Exploratory Data Analysis
- Use Jupyter notebooks for initial data exploration
- Implement comprehensive data profiling and quality checks
- Create visualizations to understand data distributions
- Document data assumptions and limitations
- Follow reproducible research practices

### Data Pipeline Development
- Implement robust data validation and cleaning procedures
- Use version control for datasets and model artifacts
- Create reproducible data preprocessing pipelines
- Implement proper train/validation/test splits
- Document data lineage and transformation steps

## Model Development Standards
### Experimentation Framework
- Start with simple baseline models before complex approaches
- Use cross-validation for robust model evaluation
- Track experiments with MLflow or similar tools
- Implement proper hyperparameter tuning strategies
- Version control model code and configurations

### Feature Engineering
- Implement feature validation and monitoring
- Use feature stores for reusable feature definitions
- Document feature engineering decisions and rationale
- Implement proper feature scaling and normalization
- Monitor for feature drift in production

## Model Deployment & Monitoring
### Production Readiness
- Implement model versioning and rollback strategies
- Use containerization for consistent deployment environments
- Implement proper model monitoring and alerting
- Create A/B testing frameworks for model comparison
- Document model performance expectations and SLAs

### MLOps Best Practices
- Implement CI/CD pipelines for model deployment
- Use infrastructure as code for ML environments
- Implement automated model retraining pipelines
- Monitor model performance and data drift
- Implement proper governance and compliance procedures

## Code Quality for ML
### Python Best Practices
- Follow PEP 8 coding standards consistently
- Use type hints for all function signatures
- Implement comprehensive docstrings with examples
- Write unit tests for data processing and model logic
- Use virtual environments and requirements management

### Documentation Standards
- Document model assumptions and limitations
- Create clear README files for project setup
- Document model architecture and training procedures
- Include performance metrics and evaluation criteria
- Provide clear instructions for model usage and deployment

## When writing ML code, always:
1. Validate data quality and handle missing values appropriately
2. Implement proper train/validation/test splits
3. Use cross-validation for model evaluation
4. Document model assumptions and limitations
5. Include comprehensive error handling
6. Implement proper logging for debugging
7. Use version control for code, data, and models
8. Write tests for data processing and model logic
9. Monitor for data and model drift
10. Follow responsible AI practices and bias detection
"""

# Security-Focused Project Instructions
SECURITY_INSTRUCTIONS = """
# Security-Focused Development Guidelines for GitHub Copilot

## Security-First Mindset
### Threat Modeling
- Identify potential attack vectors for all features
- Implement defense in depth strategies
- Follow principle of least privilege
- Assume breach mentality in system design
- Regular security assessments and penetration testing

### Secure Coding Practices
- Validate and sanitize all inputs
- Use parameterized queries for database operations
- Implement proper output encoding
- Use secure random number generation
- Follow OWASP Top 10 security guidelines

## Authentication & Authorization
### Identity Management
- Implement strong password policies
- Use multi-factor authentication (MFA)
- Implement proper session management
- Use secure token storage and handling
- Implement account lockout policies

### Access Control
- Implement role-based access control (RBAC)
- Use attribute-based access control (ABAC) when appropriate
- Implement proper authorization checks at all levels
- Use JWT tokens with proper validation
- Implement API key management and rotation

## Data Protection & Privacy
### Encryption Standards
- Use AES-256 for data at rest encryption
- Implement TLS 1.3 for data in transit
- Use proper key management and rotation
- Implement certificate pinning for mobile apps
- Use hardware security modules (HSM) for sensitive operations

### Privacy Compliance
- Implement GDPR compliance requirements
- Use data minimization principles
- Implement proper consent management
- Provide data export and deletion capabilities
- Implement audit logging for data access

## When writing security-sensitive code, always:
1. Validate all inputs at every boundary
2. Use principle of least privilege
3. Implement proper error handling without information leakage
4. Use secure coding patterns and libraries
5. Include security tests in your test suite
6. Document security decisions and trade-offs
7. Implement comprehensive logging for security events
8. Follow secure configuration management
9. Use static code analysis tools
10. Conduct regular security reviews
"""

# TODO: Project-Specific Adaptations
class CustomInstructionsManager:
    """Manage context-specific custom instructions for Copilot"""
    
    def __init__(self):
        self.instructions = {
            'frontend': FRONTEND_INSTRUCTIONS,
            'backend': BACKEND_INSTRUCTIONS,
            'ml': ML_PROJECT_INSTRUCTIONS,
            'security': SECURITY_INSTRUCTIONS
        }
        
    def get_instructions_for_context(self, project_type: str, files: list = None) -> str:
        """Get appropriate instructions based on project context"""
        # TODO: Ask Copilot to implement intelligent context detection
        
        # Analyze file types and project structure
        context_indicators = self.analyze_project_context(files or [])
        
        # Combine relevant instructions
        relevant_instructions = []
        
        if context_indicators.get('frontend_heavy'):
            relevant_instructions.append(self.instructions['frontend'])
            
        if context_indicators.get('backend_heavy'):
            relevant_instructions.append(self.instructions['backend'])
            
        if context_indicators.get('ml_project'):
            relevant_instructions.append(self.instructions['ml'])
            
        if context_indicators.get('security_sensitive'):
            relevant_instructions.append(self.instructions['security'])
        
        return "\n\n---\n\n".join(relevant_instructions)
    
    def analyze_project_context(self, files: list) -> dict:
        """Analyze project files to determine context"""
        # TODO: Implement intelligent project type detection
        indicators = {
            'frontend_heavy': False,
            'backend_heavy': False,
            'ml_project': False,
            'security_sensitive': False
        }
        
        # Check file extensions and patterns
        for file_path in files:
            if any(file_path.endswith(ext) for ext in ['.tsx', '.jsx', '.css', '.scss']):
                indicators['frontend_heavy'] = True
            
            if any(file_path.endswith(ext) for ext in ['.py', '.js', '.go', '.java']) and 'api' in file_path:
                indicators['backend_heavy'] = True
                
            if any(keyword in file_path.lower() for keyword in ['model', 'train', 'dataset', 'ml']):
                indicators['ml_project'] = True
                
            if any(keyword in file_path.lower() for keyword in ['auth', 'security', 'crypto', 'encrypt']):
                indicators['security_sensitive'] = True
        
        return indicators

# TODO: Usage examples and effectiveness measurement
effectiveness_checklist = """
# Custom Instructions Effectiveness Checklist

## Measure Copilot Response Quality
- [ ] Suggestions follow established patterns consistently
- [ ] Code includes appropriate error handling
- [ ] Security best practices are automatically included
- [ ] Performance considerations are addressed
- [ ] Testing patterns are suggested
- [ ] Documentation is comprehensive
- [ ] Accessibility features are included (frontend)
- [ ] Database queries are optimized (backend)

## Team Adoption Metrics
- [ ] Reduced code review feedback on style issues
- [ ] Increased consistency across team contributions
- [ ] Faster onboarding for new team members
- [ ] Improved security posture in generated code
- [ ] Better test coverage in suggestions
- [ ] More appropriate architectural patterns

## Continuous Improvement
- [ ] Regular review and updates of instructions
- [ ] Team feedback on instruction effectiveness
- [ ] A/B testing of different instruction variants
- [ ] Integration with team coding standards documentation
- [ ] Automated validation of instruction compliance
"""

# Expected Copilot behaviors with custom instructions:
# - Should consistently follow team-specific patterns and conventions
# - Should automatically include appropriate security measures
# - Should suggest relevant testing patterns for the project type
# - Should prioritize performance and accessibility considerations
# - Should generate code that follows established architectural patterns
# - Should include proper error handling and logging automatically
