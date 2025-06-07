# Node.js REST API with GitHub Copilot

This project template demonstrates building a comprehensive REST API using Node.js, Express, and TypeScript with GitHub Copilot assistance.

## 🎯 Learning Objectives

- Master API development patterns with Copilot
- Implement authentication and authorization
- Design database models and relationships
- Create comprehensive error handling
- Write API tests and documentation
- Deploy and monitor APIs

## 🚀 Features

- **RESTful API Design**: CRUD operations for multiple resources
- **TypeScript**: Type-safe development
- **Authentication**: JWT-based auth with role management
- **Database**: PostgreSQL with Prisma ORM
- **Validation**: Request validation with Joi
- **Testing**: Unit and integration tests
- **Documentation**: Auto-generated API docs
- **Monitoring**: Logging and health checks

## 📋 Prerequisites

- Node.js 18+ and npm
- PostgreSQL database
- GitHub Copilot extension
- Basic knowledge of REST APIs

## 🛠️ Setup Instructions

### 1. Install Dependencies
```bash
npm install
npm install -D typescript @types/node ts-node nodemon
```

### 2. Environment Configuration
```bash
cp .env.example .env
# Edit .env with your database credentials
```

### 3. Database Setup
```bash
npx prisma migrate dev
npx prisma generate
npx prisma db seed
```

### 4. Start Development Server
```bash
npm run dev
```

## 📚 Copilot Practice Exercises

### Exercise 1: User Management API
Create user registration, login, and profile management endpoints.

**Copilot Prompts to Try:**
- "Create a user registration endpoint with email validation"
- "Implement JWT authentication middleware"
- "Add password hashing with bcrypt"

### Exercise 2: Product Catalog API
Build a product management system with categories and inventory.

**Copilot Prompts to Try:**
- "Create product CRUD operations with category relationships"
- "Add inventory tracking with low stock alerts"
- "Implement product search with filters"

### Exercise 3: Order Processing API
Develop order management with payment integration.

**Copilot Prompts to Try:**
- "Create order placement endpoint with inventory checking"
- "Implement order status tracking"
- "Add payment processing with Stripe integration"

### Exercise 4: API Security
Implement comprehensive security measures.

**Copilot Prompts to Try:**
- "Add rate limiting to prevent abuse"
- "Implement role-based access control"
- "Add input sanitization and SQL injection prevention"

### Exercise 5: Testing and Documentation
Create thorough tests and documentation.

**Copilot Prompts to Try:**
- "Generate unit tests for user service"
- "Create integration tests for API endpoints"
- "Generate OpenAPI documentation"

## 🏗️ Project Structure

```
src/
├── controllers/          # Route handlers
├── middleware/          # Custom middleware
├── models/             # Database models
├── routes/             # API routes
├── services/           # Business logic
├── utils/              # Helper functions
├── types/              # TypeScript types
└── tests/              # Test files

prisma/
├── schema.prisma       # Database schema
├── migrations/         # Database migrations
└── seed.ts            # Database seeding

docs/
├── api-spec.yml       # OpenAPI specification
└── README.md          # API documentation
```

## 🔧 Available Scripts

```json
{
  "dev": "nodemon src/server.ts",
  "build": "tsc",
  "start": "node dist/server.js",
  "test": "jest",
  "test:watch": "jest --watch",
  "test:coverage": "jest --coverage",
  "db:migrate": "prisma migrate dev",
  "db:generate": "prisma generate",
  "db:seed": "prisma db seed",
  "docs:generate": "swagger-jsdoc -d swaggerDef.js src/routes/*.ts -o docs/api-spec.yml"
}
```

## 📖 API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/refresh` - Refresh token
- `POST /api/auth/logout` - User logout

### Users
- `GET /api/users/profile` - Get user profile
- `PUT /api/users/profile` - Update user profile
- `DELETE /api/users/profile` - Delete user account

### Products
- `GET /api/products` - List products with pagination
- `GET /api/products/:id` - Get product details
- `POST /api/products` - Create product (admin only)
- `PUT /api/products/:id` - Update product (admin only)
- `DELETE /api/products/:id` - Delete product (admin only)

### Orders
- `GET /api/orders` - List user orders
- `GET /api/orders/:id` - Get order details
- `POST /api/orders` - Create new order
- `PUT /api/orders/:id/status` - Update order status (admin only)

## 🧪 Testing Strategy

### Unit Tests
- Service layer functions
- Utility functions
- Middleware components

### Integration Tests
- API endpoint testing
- Database operations
- Authentication flows

### Example Test with Copilot
```typescript
// Prompt: "Create comprehensive tests for user registration endpoint"
describe('POST /api/auth/register', () => {
  // Copilot will generate complete test suite
});
```

## 📊 Monitoring and Logging

### Health Checks
- Database connectivity
- External service status
- Memory and CPU usage

### Logging
- Request/response logging
- Error tracking
- Performance metrics

## 🚀 Deployment

### Docker
```dockerfile
# Prompt: "Create Dockerfile for Node.js API with multi-stage build"
FROM node:18-alpine
# Copilot will complete the Dockerfile
```

### Environment Variables
```env
NODE_ENV=production
PORT=3000
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
JWT_SECRET=your-secret-key
REDIS_URL=redis://localhost:6379
```

## 🎓 Advanced Copilot Techniques

### 1. Context-Aware Development
Use descriptive comments to guide Copilot:
```typescript
// Create middleware to authenticate JWT tokens and attach user to request
export const authenticateToken = (req: Request, res: Response, next: NextFunction) => {
  // Copilot will suggest complete implementation
};
```

### 2. Error Handling Patterns
```typescript
// Implement global error handler with proper HTTP status codes and logging
class ApiError extends Error {
  // Copilot will suggest error class implementation
}
```

### 3. Database Operations
```typescript
// Create user service with CRUD operations and business logic validation
class UserService {
  // Copilot will suggest service methods
}
```

## 🔗 Learning Resources

- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)
- [REST API Design Guidelines](https://restfulapi.net/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Prisma Documentation](https://www.prisma.io/docs/)

## 🎯 Certification Tips

1. **Use descriptive prompts** - Be specific about requirements
2. **Iterate on suggestions** - Refine prompts based on initial results
3. **Understand generated code** - Always review and comprehend suggestions
4. **Test thoroughly** - Use Copilot to generate comprehensive tests
5. **Follow best practices** - Ensure suggestions align with industry standards

## 🤝 Contributing

Practice contributing to this template:
1. Add new API endpoints
2. Implement additional security measures
3. Create more comprehensive tests
4. Improve documentation

## 📝 License

This project template is provided for educational purposes as part of GitHub Copilot certification preparation.
