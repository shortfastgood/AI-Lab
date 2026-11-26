---
type: Product Specification
title: Design Tokens and Architecture
description: Architecture for maintainable pure-CSS pages using design tokens and Cascade Layers.
status: draft
---
# Design Tokens and Architecture

## Layer Architecture and Initialization

The page initializes the Cascade Layer order before defining any rule:

```css
/* Cascade Layer Architecture */
@layer reset, tokens, base, layout, components, utilities;
```

This first declaration is the layer contract. The layers are listed from the broadest foundation to the most specific overrides:

* `reset` normalizes browser defaults and box sizing.
* `tokens` defines reusable custom properties for color, typography, spacing, radius, elevation, dimensions, and motion.
* `base` defines document defaults and shared interaction states such as focus.
* `layout` defines the application shell and the responsive page structure.
* `components` defines reusable UI components.
* `utilities` defines narrow, intentional overrides used across components.

The declaration must precede all layer blocks. It fixes the precedence order before later declarations can depend on it. A normal declaration in a later layer has higher precedence than a normal declaration in an earlier layer, which keeps overrides predictable without `!important` or increasing selector specificity. Separate layers also let a component use semantic selectors while tokens and layout remain independent.

The page is initialized at runtime only for behavior that CSS and native HTML cannot provide. Its JavaScript block runs at the end of the document, after the relevant navigation, title, toast, and button elements have been parsed. It therefore has the following reasons and order:

1. Capture the page-title, navigation, toast, and timer state once.
2. Bind navigation clicks and the new-plan action after their elements exist.
3. Read `window.location.hash` and select a valid initial section.
4. Reuse the same `setActiveSection` function for initial state and later interactions.
5. Use a short-lived toast only for feedback that changes during interaction.

This placement avoids an unnecessary `DOMContentLoaded` listener because the script is loaded after the markup it initializes. It also keeps startup deterministic: known URL state is applied once, while later navigation actions update the same state without reloading the page.

## Reset Layer

The `reset` layer initializes a small, deliberate set of browser defaults before tokens, base styles, layout, and components are applied:

```css
@layer reset {
  *,
  *::before,
  *::after {
    box-sizing: border-box;
  }

  body,
  h1,
  h2,
  h3,
  p {
    margin: 0;
  }

  button,
  input {
    font: inherit;
  }

  a {
    color: inherit;
    text-decoration: none;
  }
}
```

Each initialization has a specific purpose:

* `box-sizing: border-box` makes declared widths include padding and borders. This produces predictable grid tracks, cards, controls, and container widths.
* Removing margins from `body`, headings, and paragraphs prevents user-agent spacing from competing with the page's explicit spacing tokens.
* `font: inherit` makes buttons and inputs participate in the typography defined by `body` and their local component instead of preserving browser-specific form-control typography.
* Inherited link color prevents browser blue from entering a design-token color system. Removing the default underline establishes a neutral starting point for component-specific link states.

The reset is intentionally limited. It does not remove list structure, focus indicators, semantic defaults, or browser form behavior that the page still needs. Later layers add those concerns explicitly, so the reset normalizes only the defaults that would otherwise affect layout, typography, or component consistency.

Pseudo-elements are included in the `box-sizing` initialization because generated content must follow the same sizing model as real elements. The `reset` layer has the lowest explicit precedence, which means later layers can change any rule when the component design requires it without using `!important`.

## Standardizing CSS Variables

A maintenable pure CSS page requires a clear design token architecture. A stylesheet using native CSS @layer directives establish strict precedence without relying on !important or high-specificity selector chains.

```css
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

## Collapsible Sidebar via `:has()`

With the CSS :has() relational pseudo-class, state management can be driven purely by DOM state (such as checked checkboxes or data attributes).

```css
@layer layout {
  /* When the toggle button or input inside header is in active state */
  .app-shell:has(.sidebar-toggle[aria-expanded="false"]) {
    grid-template-columns: var(--sidebar-collapsed-width) 1fr;
  }

  /* Collapse label visibility smoothly when sidebar is collapsed */
  .app-shell:has(.sidebar-toggle[aria-expanded="false"]) .nav-label {
    opacity: 0;
    pointer-events: none;
    transform: translateX(-10px);
    display: none;
  }

  .nav-item {
    display: flex;
    align-items: center;
    gap: var(--space-md);
    padding: var(--space-md) var(--space-lg);
    color: var(--color-text-secondary);
    text-decoration: none;
    border-left: 3px solid transparent;
    transition: all var(--transition-speed) var(--transition-easing);
  }

  .nav-item:hover,
  .nav-item.active {
    background-color: var(--color-brand-light);
    color: var(--color-brand-primary);
    border-left-color: var(--color-brand-primary);
  }
}
```
