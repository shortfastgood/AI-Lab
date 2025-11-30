# Migration Planning: Portal/Views/Core to React/Redux

## Initial Assessment

### Current Architecture
The Portal/Views/Core directory contains Razor views (.cshtml) that serve as the primary UI layer for features such as Dashboard, Holdings, Profile, and Transactions. These views are built using:

- **Server-Side Rendering:** ASP.NET Core Razor for HTML generation with C# model binding
- **Client-Side Interactivity:** Knockout.js (KO) for data binding, templating, and dynamic updates
- **JavaScript Organization:** Modular JS files in `wwwroot/js/core/` (e.g., `dashboard.js`) using KO view models, pub/sub patterns, and component loading
- **Styling:** SCSS-based stylesheets in `wwwroot/css/core/` with mixins, variables, and theme support
- **Backend Integration:** C# controllers (e.g., `DashboardController.cs`) providing data via managers and APIs
- **Custom Components:** Reusable elements like `<xxx-card>`, `<xxx-tooltip>` with KO bindings

Key observations:
- Heavy reliance on KO for state management and UI updates
- Pub/sub system for component communication
- Partial views and templates for modularity
- Server-rendered HTML with client-side enhancements
- No TypeScript currently used; all JS is vanilla

### Challenges
- Migrating from server-side Razor to client-side React requires rethinking data flow
- KO's MVVM pattern differs significantly from React's component-based architecture
- Existing JS code (e.g., 956 lines in `dashboard.js`) needs refactoring
- State scattered across KO view models needs consolidation in Redux
- Custom KO components must be rebuilt as React components
- Potential performance impact during transition (server vs. client rendering)

### Opportunities
- React's component reusability can simplify UI development
- Redux provides centralized, predictable state management
- TypeScript can improve code maintainability and reduce errors
- Modern tooling (e.g., hooks, context) for better developer experience
- Potential for better performance with client-side routing and lazy loading

## Architecture Design

### Proposed Architecture
- **Frontend Framework:** React 18+ with TypeScript for type safety
- **State Management:** Redux Toolkit for simplified Redux setup
- **Routing:** React Router for client-side navigation
- **Styling:** Maintain SCSS with CSS Modules or styled-components for component-scoping
- **API Layer:** Axios or Fetch for HTTP requests to existing C# controllers
- **Build Tool:** Webpack or Vite integrated with existing ASP.NET Core pipeline
- **Testing:** Jest and React Testing Library for unit/component tests

### Component Structure
Mirror the Views/Core directory structure:
```
src/components/
├── Dashboard/
│   ├── Dashboard.tsx
│   ├── TotalWealth.tsx
│   ├── TotalCash.tsx
│   └── ...
├── Holdings/
│   ├── Holdings.tsx
│   └── ...
├── Profile/
│   ├── Profile.tsx
│   └── ...
└── Shared/
    ├── Card.tsx
    ├── Tooltip.tsx
    └── ...
```

### Redux Store Design
Centralize state from KO view models:
```
store/
├── slices/
│   ├── dashboardSlice.ts
│   ├── holdingsSlice.ts
│   ├── profileSlice.ts
│   └── ...
├── api/
│   ├── dashboardApi.ts
│   ├── holdingsApi.ts
│   └── ...
└── store.ts
```

### Data Flow
1. React components dispatch actions to Redux
2. Redux thunks/async actions call C# API endpoints
3. API responses update Redux state
4. Updated state triggers React re-renders

### Integration Points
- Keep existing C# controllers as REST APIs
- Use existing authentication/session management
- Maintain SCSS theming and custom components
- Preserve accessibility features and ARIA attributes

## Migration Roadmap

### Phase 1: Foundation (2-4 weeks)
- [ ] Set up React/Redux project structure
- [ ] Configure TypeScript and build pipeline
- [ ] Create basic Redux store and API layer
- [ ] Migrate shared components (Card, Tooltip, etc.)
- [ ] Set up testing framework
- [ ] Create proof-of-concept component (e.g., simple Dashboard card)

### Phase 2: Feature Migration (6-8 weeks)
- [ ] Migrate Dashboard feature (highest priority)
  - [ ] Convert Index.cshtml to Dashboard.tsx
  - [ ] Implement Redux slice for dashboard state
  - [ ] Migrate dashboard.js logic to React hooks
  - [ ] Adapt SCSS styles
- [ ] Migrate Holdings feature
- [ ] Migrate Profile feature
- [ ] Migrate remaining features incrementally
- [ ] Update routing and navigation

### Phase 3: Optimization & Testing (2-3 weeks)
- [ ] Performance optimization (code splitting, lazy loading)
- [ ] Comprehensive testing (unit, integration, E2E)
- [ ] Accessibility audit and fixes
- [ ] Documentation updates
- [ ] User acceptance testing

### Phase 4: Deployment & Monitoring (1-2 weeks)
- [ ] Gradual rollout with feature flags
- [ ] Monitor performance and error rates
- [ ] Gather user feedback
- [ ] Final cleanup of legacy code

### Success Metrics
- Page load times maintained or improved
- Zero critical bugs in migrated features
- Developer productivity increase (measured by velocity)
- User satisfaction scores unchanged or improved

### Risks & Mitigations
- **Risk:** Performance regression during migration
  - **Mitigation:** Implement feature flags for gradual rollout
- **Risk:** Breaking changes in C# APIs
  - **Mitigation:** Version APIs and maintain backward compatibility
- **Risk:** Developer learning curve
  - **Mitigation:** Provide training and pair programming sessions
- **Risk:** Increased bundle size
  - **Mitigation:** Use code splitting and tree shaking

### Dependencies
- React 18+
- Redux Toolkit
- TypeScript 4.9+
- Axios for API calls
- Jest + React Testing Library
- Existing ASP.NET Core 6+ setup

This roadmap provides a structured approach to migrating from Razor/Knockout.js to React/Redux while minimizing disruption to the existing C# backend and maintaining code quality.
