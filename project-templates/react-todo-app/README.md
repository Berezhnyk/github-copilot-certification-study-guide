# React Todo App - Copilot Practice Project

This is a practice project for learning GitHub Copilot with React. Follow the prompts and let Copilot help you build a feature-rich todo application.

## Setup Instructions

1. Navigate to this directory
2. Install dependencies: `npm install`
3. Start development server: `npm start`

## Learning Objectives

- Practice component-driven development with Copilot
- Learn to write effective prompts for React patterns
- Understand state management suggestions
- Practice with modern React hooks

## Features to Implement

### Phase 1: Basic Todo
- [ ] Add new todos
- [ ] Mark todos as complete
- [ ] Delete todos
- [ ] Display todo list

### Phase 2: Enhanced Features
- [ ] Edit existing todos
- [ ] Filter todos (all, active, completed)
- [ ] Clear all completed todos
- [ ] Todo counter

### Phase 3: Advanced Features
- [ ] Local storage persistence
- [ ] Drag and drop reordering
- [ ] Categories/tags
- [ ] Due dates

## Copilot Practice Tips

1. Start each component with a clear comment describing its purpose
2. Use TypeScript interfaces to help Copilot understand your data structure
3. Write function signatures first, then let Copilot implement
4. Use descriptive prop names and component names

## Example Prompts to Try

```typescript
// Todo item component that displays a single todo
// Props: todo object with id, text, completed, and optional dueDate
// Should handle toggle completion and delete actions
// Use modern React hooks and TypeScript
interface TodoItemProps {
  // Let Copilot suggest the interface
}

export const TodoItem: React.FC<TodoItemProps> = ({
  // Let Copilot implement the component
```

```typescript
// Custom hook for managing todo state with local storage
// Should handle add, delete, toggle, and edit operations
// Persist data to localStorage and load on mount
// Return todos array and action functions
export const useTodos = () => {
  // Let Copilot implement the hook
```
