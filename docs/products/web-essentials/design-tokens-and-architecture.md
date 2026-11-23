---
type: Product Specification
title: Design Tokens and Architecture
description: Architecture for maintainable pure-CSS pages using design tokens and Cascade Layers.
status: draft
---
# Design Tokens and Architecture

## Standardizing CSS Variables

A maintenable pure CSS page requires a clear design token architecture. A stylesheet using native CSS @layer directives establish strict precedence without relying on !important or high-specificity selector chains.

```css
/* Cascade Layer Architecture */
@layer reset, tokens, base, layout, components, utilities;

@layer tokens {
  :root {
    /* Color Palette - Light & Dark Adaptive Values */
    --color-bg-app: #f8fafc;
    --color-bg-surface: #ffffff;
    --color-bg-subtle: #f1f5f9;
    --color-border: #e2e8f0;

    --color-text-primary: #0f172a;
    --color-text-secondary: #475569;
    --color-text-muted: #94a3b8;

    --color-brand-primary: #2563eb;
    --color-brand-light: #eff6ff;
    --color-success: #16a34a;
    --color-warning: #d97706;
    --color-danger: #dc2626;

    /* Typography & Spacing Scale */
    --font-sans: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: ui-monospace, 'Cascadia Code', 'Fira Code', monospace;

    --space-xs: 0.25rem;  /* 4px */
    --space-sm: 0.5rem;   /* 8px */
    --space-md: 1rem;     /* 16px */
    --space-lg: 1.5rem;   /* 24px */
    --space-xl: 2rem;     /* 32px */

    /* Elevation & Radius */
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 16px;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);

    /* Layout Dimensions */
    --sidebar-width: 260px;
    --sidebar-collapsed-width: 72px;
    --header-height: 64px;
    --transition-speed: 0.25s;
    --transition-easing: cubic-bezier(0.4, 0, 0.2, 1);
  }
}
```

## CSS Grid grid-template-areas

The foundation of any pages layout is in its mani application shell. For a dashboard can be header, navigation sidebar, main content body and sticky subpanels. CSS Grid provides a declarative way to structure this app shell using named grid areas.

### HTML Structure (Dashboard Example)

```html
<div class="app-shell">
  <header class="app-header">
    <div class="header-brand">
      <button class="sidebar-toggle" aria-label="Toggle Sidebar">
        <span class="icon-menu"></span>
      </button>
      <h1 class="app-logo">MetricsHub</h1>
    </div>
    <div class="header-actions">
      <input type="search" placeholder="Search analytics..." class="search-input" />
      <button class="user-profile-btn">
        <img src="avatar.jpg" alt="User avatar" class="avatar" />
      </button>
    </div>
  </header>

  <aside class="app-sidebar">
    <nav class="nav-menu">
      <a href="#overview" class="nav-item active">
        <span class="nav-icon">📊</span>
        <span class="nav-label">Overview</span>
      </a>
      <a href="#analytics" class="nav-item">
        <span class="nav-icon">📈</span>
        <span class="nav-label">Analytics</span>
      </a>
      <a href="#orders" class="nav-item">
        <span class="nav-icon">📦</span>
        <span class="nav-label">Orders</span>
      </a>
      <a href="#settings" class="nav-item">
        <span class="nav-icon">⚙️</span>
        <span class="nav-label">Settings</span>
      </a>
    </nav>
  </aside>

  <main class="app-main">
    <!-- Dashboard Cards & Data Section -->
  </main>
</div>
```

### CSS Layout

```css
@layer layout {
  .app-shell {
    display: grid;
    grid-template-rows: var(--header-height) 1fr;
    grid-template-columns: var(--sidebar-width) 1fr;
    grid-template-areas:
      "header header"
      "sidebar main";
    min-height: 100vh;
    background-color: var(--color-bg-app);
    color: var(--color-text-primary);
    font-family: var(--font-sans);
    transition: grid-template-columns var(--transition-speed) var(--transition-easing);
  }

  .app-header {
    grid-area: header;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 var(--space-lg);
    background-color: var(--color-bg-surface);
    border-bottom: 1px solid var(--color-border);
    position: sticky;
    top: 0;
    z-index: 100;
  }

  .app-sidebar {
    grid-area: sidebar;
    background-color: var(--color-bg-surface);
    border-right: 1px solid var(--color-border);
    padding: var(--space-md) 0;
    overflow-y: auto;
    overflow-x: hidden;
  }

  .app-main {
    grid-area: main;
    padding: var(--space-xl);
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-xl);
  }

  /* Responsive Viewport Layout Adjustments */
  @media (max-width: 768px) {
    .app-shell {
      grid-template-columns: 0 1fr;
      grid-template-areas:
        "header header"
        "main main";
    }
  }
}
```
