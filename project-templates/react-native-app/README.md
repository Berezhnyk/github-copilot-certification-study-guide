# React Native Mobile App Template

## Overview
A comprehensive React Native mobile application template designed for GitHub Copilot certification practice. This template demonstrates mobile development patterns, cross-platform considerations, and modern React Native practices.

## Learning Objectives
- Practice mobile app development with GitHub Copilot
- Understand cross-platform development patterns
- Learn navigation, state management, and native integrations
- Explore mobile-specific UI/UX patterns
- Practice with React Native ecosystem tools

## Project Structure
```
react-native-app/
├── src/
│   ├── components/           # Reusable UI components
│   ├── screens/             # Application screens
│   ├── navigation/          # Navigation configuration
│   ├── hooks/               # Custom React hooks
│   ├── services/            # API and external services
│   ├── utils/               # Utility functions
│   ├── types/               # TypeScript type definitions
│   └── constants/           # App constants and config
├── __tests__/               # Test files
├── android/                 # Android-specific code
├── ios/                     # iOS-specific code
├── assets/                  # Images, fonts, etc.
└── docs/                    # Documentation
```

## Getting Started

### Prerequisites
- Node.js 18+ and npm/yarn
- React Native CLI or Expo CLI
- Android Studio (for Android development)
- Xcode (for iOS development, macOS only)
- iOS Simulator or Android Emulator

### Installation
```bash
# Clone the template
npx react-native init MyMobileApp --template typescript

# Navigate to project
cd MyMobileApp

# Install dependencies
npm install

# Install additional packages for this template
npm install @react-navigation/native @react-navigation/bottom-tabs @react-navigation/stack
npm install react-native-screens react-native-safe-area-context
npm install @reduxjs/toolkit react-redux
npm install react-native-vector-icons
npm install @react-native-async-storage/async-storage
npm install react-native-permissions
npm install react-native-camera react-native-image-picker

# iOS specific (macOS only)
cd ios && pod install && cd ..

# Start Metro bundler
npx react-native start

# Run on Android
npx react-native run-android

# Run on iOS (macOS only)
npx react-native run-ios
```

## GitHub Copilot Practice Exercises

### Exercise 1: Component Development
Use Copilot to create mobile-optimized components:

```typescript
// Create a custom TouchableCard component
// Should handle press events, loading states, and accessibility
// Include proper TypeScript types and React Native styling
interface TouchableCardProps {
  title: string;
  subtitle?: string;
  onPress: () => void;
  disabled?: boolean;
  loading?: boolean;
}

export const TouchableCard: React.FC<TouchableCardProps> = () => {
  // Let Copilot complete this component
};
```

### Exercise 2: Navigation Setup
Use Copilot to set up React Navigation:

```typescript
// Create a tab navigator with stack navigators
// Include: Home, Profile, Settings, and Search tabs
// Each tab should have its own stack with multiple screens
// Include proper TypeScript types for navigation

type RootTabParamList = {
  HomeTab: undefined;
  ProfileTab: undefined;
  SettingsTab: undefined;
  SearchTab: undefined;
};

// Let Copilot help create the navigation structure
```

### Exercise 3: Custom Hooks
Create mobile-specific custom hooks:

```typescript
// Create a useLocationPermission hook
// Should handle permission requests and location tracking
// Include error handling and loading states
// Work with both iOS and Android permission systems

export const useLocationPermission = () => {
  // Let Copilot implement this hook
};

// Create a useNetworkStatus hook
// Should monitor network connectivity
// Return connection type and status

export const useNetworkStatus = () => {
  // Let Copilot implement this hook
};
```

### Exercise 4: API Integration
Implement mobile API patterns:

```typescript
// Create a service for handling API calls with retry logic
// Include network error handling and offline support
// Implement request queuing for offline scenarios
// Add authentication token management

class MobileApiService {
  private baseURL = 'https://api.example.com';
  private retryAttempts = 3;
  
  // Let Copilot implement methods for:
  // - fetchUserProfile
  // - updateUserProfile  
  // - uploadImage
  // - handleOfflineQueue
}
```

### Exercise 5: State Management
Set up Redux with mobile-specific considerations:

```typescript
// Create Redux slices for mobile app state
// Include: user, app settings, offline data, camera
// Handle background app state and data persistence

interface AppState {
  user: UserState;
  settings: SettingsState;
  offline: OfflineState;
  camera: CameraState;
}

// Let Copilot create the Redux store and slices
```

### Exercise 6: Native Integrations
Implement native functionality:

```typescript
// Create a camera service that handles:
// - Photo capture with compression
// - Permission handling
// - Gallery access
// - Image editing capabilities

export class CameraService {
  // Let Copilot implement methods for:
  // - requestCameraPermission
  // - capturePhoto
  // - selectFromGallery
  // - compressImage
}
```

### Exercise 7: Testing Mobile Components
Write tests for mobile components:

```typescript
// Test TouchableCard component with:
// - Press events
// - Loading states  
// - Accessibility
// - Different screen sizes

import { render, fireEvent } from '@testing-library/react-native';
import { TouchableCard } from '../TouchableCard';

describe('TouchableCard', () => {
  // Let Copilot generate comprehensive tests
});
```

### Exercise 8: Performance Optimization
Implement mobile performance patterns:

```typescript
// Create a performance monitoring service
// Track: render times, memory usage, network calls
// Implement lazy loading for large lists
// Add image caching and optimization

export class PerformanceMonitor {
  // Let Copilot implement performance tracking methods
}

// Create optimized list component with virtualization
export const OptimizedList = () => {
  // Let Copilot implement FlatList with performance optimizations
};
```

## Copilot Prompt Templates

### Component Generation
```
// Create a React Native component for [component name]
// Requirements: TypeScript, proper styling, accessibility
// Include: [specific features]
// Handle: [edge cases]
// Follow: React Native best practices
```

### Screen Development
```
// Create a React Native screen for [screen purpose]
// Include: navigation header, loading states, error handling
// Layout: [describe layout requirements]
// Interactions: [describe user interactions]
// Data: [describe data requirements]
```

### API Integration
```
// Create an API service method for [functionality]
// Handle: network errors, retries, offline scenarios
// Include: TypeScript types, error boundaries
// Return: [expected return format]
// Authentication: [auth requirements]
```

## Best Practices for Copilot

### 1. Context-Rich Comments
```typescript
// React Native Login Screen
// Features: Email/password auth, biometric login, remember me
// Navigation: Navigate to Dashboard on success, Register on signup
// Validation: Real-time email/password validation
// Security: Hash passwords, secure storage, rate limiting
// Accessibility: Screen reader support, high contrast mode
// Platform: Cross-platform with platform-specific adaptations

export const LoginScreen = () => {
```

### 2. Platform-Specific Code
```typescript
// Handle platform differences in comments
// iOS: Use native navigation gestures
// Android: Use Material Design patterns
// Both: Ensure consistent user experience

import { Platform } from 'react-native';

const styles = StyleSheet.create({
  container: {
    // Let Copilot suggest platform-specific styles
    ...Platform.select({
      ios: {
        // iOS-specific styles
      },
      android: {
        // Android-specific styles
      },
    }),
  },
});
```

### 3. Performance Considerations
```typescript
// Large list optimization
// Handle: 1000+ items, smooth scrolling, memory efficiency
// Include: pull-to-refresh, infinite scroll, search filtering
// Performance: Use FlatList, optimize renderItem, keyExtractor

export const ProductList = () => {
  // Let Copilot optimize for performance
};
```

## Common Mobile Patterns

### Loading States
```typescript
// Universal loading component with animation
// Support: skeleton loading, shimmer effects
// Customizable: size, color, animation type
```

### Error Boundaries
```typescript
// React Native error boundary
// Handle: JS errors, network errors, permission errors
// Include: retry mechanisms, error reporting
```

### Offline Support
```typescript
// Offline data management
// Sync: background sync, conflict resolution
// Storage: AsyncStorage, SQLite integration
```

## Advanced Challenges

### Challenge 1: Real-time Features
Implement real-time chat or live updates using WebSockets

### Challenge 2: Complex Animations
Create custom animations with Reanimated

### Challenge 3: Native Module Integration
Integrate custom native modules

### Challenge 4: App Store Deployment
Prepare app for production deployment

## Resources for Further Learning
- React Native Documentation
- React Navigation Guide
- Redux Toolkit Documentation
- React Native Testing Library
- Flipper for Debugging
- Fastlane for CI/CD

## Success Metrics
- [ ] All components render correctly on both platforms
- [ ] Navigation flows work smoothly
- [ ] API integration handles all edge cases
- [ ] Tests achieve 80%+ coverage
- [ ] Performance metrics meet mobile standards
- [ ] Accessibility compliance achieved
- [ ] Code follows React Native best practices

Remember: Mobile development has unique constraints and opportunities. Use Copilot to explore platform-specific solutions while maintaining cross-platform compatibility.
