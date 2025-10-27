# Portal Architecture Explanation

## Overview

The Portal is a comprehensive wealth management web application built on ASP.NET Core MVC, designed to provide investment professionals and clients with a robust platform for portfolio management, reporting, and client communication. This document explains the architectural decisions, design patterns, and development practices that shape the application.

### Application Purpose and Context

Portal serves as the primary web interface for the wealth management platform, enabling:
- Client portfolio viewing and analysis
- Document management and secure messaging
- Investment performance tracking
- Risk profiling and reporting
- Administrative functions for investment advisors

### Technology Stack

- **Framework**: ASP.NET Core 8.0 MVC
- **Language**: C# with .NET 8.0
- **Frontend**: Razor views with Knockout.js for dynamic interactions
- **Database**: SQL Server with Entity Framework Core
- **Authentication**: ASP.NET Core Identity with SAML 2.0 support
- **Asset Management**: WebOptimizer for bundling and minification
- **Reverse Proxy**: YARP for API routing and static content serving
- **Monitoring**: Prometheus metrics and health checks
- **Container Support**: Docker with Linux-specific configurations

## Project Structure and Organization

The solution follows a modular architecture with clear separation of concerns across multiple projects:

### Solution Layout

```
Portal.sln
├── Portal/                 # Main web application
├── Portal.Services/        # Business logic services
├── Portal.Shared/          # Shared components and utilities
├── Portal.Tests/          # Unit and integration tests
├── map-invest/             # Legacy mapping interface
└── map-invest-ts/          # TypeScript-based mapping interface
```

### Main Application Structure (Portal)

The main web application follows ASP.NET Core MVC conventions with additional organizational patterns:

```
Portal/
├── Areas/                          # Feature-based organization
│   ├── Api/                        # API controllers
│   └── Public/                     # Public-facing pages
├── Controllers/                    # MVC controllers
├── Views/                          # Razor views
│   ├── Core/                       # Feature-specific views
│   └── Shared/                     # Layout and partial views
├── wwwroot/                        # Static assets
│   ├── css/                        # Stylesheets
│   ├── js/                         # JavaScript files
│   └── lib/                        # Third-party libraries
├── Models/                         # View models
├── Infrastructure/                 # Infrastructure concerns
└── Core/                           # Core application logic
```

### Areas Organization

The application uses ASP.NET Core Areas to organize features:

- **Public Area**: Handles authentication, login, and public-facing functionality
- **Api Area**: Provides RESTful API endpoints for client applications
- **Core Controllers**: Main application features (Dashboard, Holdings, Reports, etc.)

### Shared Components (Portal.Shared)

Contains reusable components across the application:

```
Portal.Shared/
├── Controllers/                    # Base controllers
├── Models/                         # Shared data models
├── DTOs/                           # Data transfer objects
├── Interfaces/                     # Service contracts
├── Managers/                       # Business logic managers
├── Extensions/                     # Extension methods
├── Attributes/                     # Custom attributes
├── TagHelpers/                     # Razor tag helpers
├── Mappings/                       # AutoMapper configurations
└── Security/                       # Security-related utilities
```

## Core Application Framework

### ASP.NET Core MVC Setup

The application bootstraps through the standard ASP.NET Core pattern:

**Program.cs**: Entry point that creates the host and configures web server defaults
**Startup.cs**: Main configuration class handling services, middleware, and routing

### Dependency Injection and Service Registration

Services are registered in `Startup.ConfigureServices()` following these patterns:

```csharp
// Infrastructure services
services.AddDbContext<DataProtectionKeysContext>(options =>
    options.UseSqlServer(sessionConnectionString));

// Business services
PortalDependencies.Configure(services);

// Framework services
services.AddControllersWithViews(options => {
    // MVC configuration
});
```

### Middleware Pipeline

The request processing pipeline is configured in `Startup.Configure()`:

1. **Exception Handling**: Custom error pages and status code handling
2. **Security Headers**: HSTS, CSP, referrer policy
3. **Static Files**: Asset serving with CORS in development
4. **Authentication/Authorization**: Identity and SAML middleware
5. **Session Management**: Distributed SQL Server sessions
6. **Routing**: MVC and API endpoint mapping
7. **Response Processing**: Custom headers and logging

## Security and Authentication

### Identity Management

The application uses ASP.NET Core Identity extended with custom features:

- **User Management**: Extended user profiles with agency relationships
- **Password Policies**: Custom validators for complexity requirements
- **Session Security**: Distributed cache with data protection keys

### SAML 2.0 Integration

External authentication via SAML 2.0 for enterprise integration:

```csharp
if (saml2Enabled) {
    services.AddSaml2AuthenticationForInvest(
        ExternalLoginConfigurationHelper.GenerateSaml2ConfigurationOptions(_investConfiguration),
        loggerAdapter);
}
```

### Security Middleware

Multiple security layers protect the application:

- **CSRF Protection**: Anti-forgery tokens on forms
- **Content Security Policy**: XSS prevention headers
- **HSTS**: HTTPS enforcement
- **Session Security**: Secure cookie configuration
- **Browser Support**: Redirect unsupported browsers

## Data Layer and Services

### Database Configuration

Multi-tenant SQL Server setup with Entity Framework:

```csharp
services.AddDbContext<DataProtectionKeysContext>(options =>
    options.UseSqlServer(sessionConnectionString));
```

### Service Layer Architecture

Business logic is organized in service classes:

**Portal.Services**: Core business services
**Portal.Shared.Managers**: Domain-specific managers
**Portal.Shared.Interfaces**: Service contracts for dependency injection

### External API Integrations

The application integrates with multiple external systems:

- **Market Data**: Real-time and historical market information
- **Document Storage**: Secure document management
- **Secure Messaging**: Encrypted client communication
- **Notification Services**: Email and SMS notifications
- **Third-party APIs**: Various financial data providers

## Frontend Architecture

### View Organization

Razor views follow a hierarchical structure:

```
Views/
├── Shared/                         # Layout and common partials
│   ├── _Layout.cshtml             # Main layout
│   ├── _ViewImports.cshtml        # Common using statements
│   └── _ViewStart.cshtml          # Default layout specification
└── Core/                          # Feature-specific views
    ├── Dashboard/
    ├── Holdings/
    ├── Reports/
    └── ...
```

### Asset Bundling and Optimization

WebOptimizer manages static assets:

**bundleconfig.json**: Defines CSS and JavaScript bundles
**Startup.cs**: Configures WebOptimizer with minification and caching

```csharp
services.AddWebOptimizer(pipeline => {
    List<Bundle> bundles = BundleHelper.GetBundles("bundleconfig.json");
    foreach (Bundle bundle in bundles) {
        // Bundle configuration
    }
});
```

### JavaScript and CSS Organization

Assets are organized by feature and shared components:

```
wwwroot/
├── css/
│   ├── portal.css                 # Main stylesheet
│   ├── core/                      # Feature-specific styles
│   └── core/specifics/            # Component-specific styles
└── js/
    ├── portal.js                  # Main JavaScript
    └── core/                      # Feature-specific scripts
```

## Adding New Pages and Components

### Controller Creation Patterns

New controllers inherit from `PortalController` and follow established patterns:

```csharp
public class NewFeatureController : PortalController
{
    public NewFeatureController(IAuditManager auditor, ILogRepository logger)
        : base(auditor, logger)
    {
    }

    public IActionResult Index()
    {
        // Action implementation
        return View();
    }
}
```

### View Development Guidelines

1. **Location**: Place views in appropriate feature directories under `Views/Core/`
2. **Layout**: Use `_ViewStart.cshtml` for consistent layout inheritance
3. **Partials**: Create reusable components in `Views/Shared/`
4. **Models**: Strongly-typed views with dedicated view models

### Service Integration Approaches

1. **Dependency Injection**: Register services in `Startup.ConfigureServices()`
2. **Interface Segregation**: Define interfaces in `Portal.Shared.Interfaces`
3. **Manager Pattern**: Implement business logic in manager classes
4. **Repository Pattern**: Data access through repository interfaces

### Asset Management for New Features

1. **CSS**: Add feature-specific stylesheets to `bundleconfig.json`
2. **JavaScript**: Include scripts in appropriate bundles
3. **Minification**: Configure minification settings for production
4. **Caching**: Leverage WebOptimizer caching for performance

### Step-by-Step: Adding a New Page

1. **Create Controller**:
   ```csharp
   // Controllers/NewFeatureController.cs
   public class NewFeatureController : PortalController
   {
       public IActionResult Index() => View();
   }
   ```

2. **Create View**:
   ```html
   <!-- Views/Core/NewFeature/Index.cshtml -->
   @model NewFeatureViewModel
   @{
       ViewData["Title"] = "New Feature";
   }
   <h1>New Feature</h1>
   ```

3. **Add Routing** (if needed):
   ```csharp
   // Startup.cs or PortalRouter.cs
   endpoints.MapControllerRoute(
       name: "newfeature",
       pattern: "NewFeature/{action=Index}/{id?}",
       defaults: new { controller = "NewFeature" });
   ```

4. **Add Assets**:
   ```json
   // bundleconfig.json
   {
     "outputFileName": "/css/core/newfeature.min.css",
     "inputFiles": ["css/core/newfeature.css"],
     "minify": { "enabled": true }
   }
   ```

5. **Update Navigation**: Add menu items and routing links

## Development Workflow and Best Practices

### Code Organization Principles

- **Single Responsibility**: Each class has one reason to change
- **Dependency Inversion**: Depend on abstractions, not concretions
- **DRY Principle**: Avoid code duplication
- **SOLID Principles**: Applied throughout the architecture

### Testing Structure

Tests mirror the application structure:

```
Portal.Tests/
├── Controllers/                   # Controller tests
├── Managers/                      # Manager tests
├── Extensions/                    # Extension method tests
├── Integration/                   # Integration tests
└── BaseTests.cs                   # Test base classes
```

### Development Environment

- **Local Development**: IIS Express or Kestrel
- **Debug Configuration**: Runtime compilation and detailed errors
- **Reverse Proxy**: Local API routing for development
- **Container Support**: Docker development environment

### Deployment Considerations

- **Containerization**: Docker images for consistent deployment
- **Configuration Management**: Environment-specific settings
- **Asset Optimization**: Production minification and bundling
- **Health Checks**: Application monitoring endpoints
- **Metrics**: Prometheus integration for observability

### Performance Optimization

- **Caching**: Distributed SQL Server cache
- **Asset Bundling**: WebOptimizer for reduced HTTP requests
- **Database Optimization**: Efficient queries and indexing
- **CDN Integration**: Static asset delivery optimization

This architecture provides a solid foundation for a scalable, maintainable wealth management platform while following industry best practices and .NET Core conventions.
