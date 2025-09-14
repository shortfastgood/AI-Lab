
---
description: 'Guidelines for building Plant UML diagrams'
applyTo: '**/*.puml'
---

# Plant UML Development

## Project Component Diagram
- The component diagram is located in the `architecture/uml` directory
- The diagram is defined in PlantUML format
- Labels containing whitespaces should be enclosed in double quotes
- Use the `@startuml` and `@enduml` tags to define the diagram
- Use `!theme spacelab` for a simple and clean theme
- Use `package` for grouping components
- Use `note` for comments or explanations
- Use `skinparam defaultFontSize 12` for consistent font size
- Use `skinparam defaultFontName "Arial"` for consistent font
- A database component should be represented as a `database` stereotype
- Use `component` for other components

## Database Schema Diagram
- The database schema is located in the `implementation-plan/uml` directory
- The schema is defined in PlantUML format
- Labels containing whitespaces should be enclosed in double quotes
- Use the `@startuml` and `@enduml` tags to define the schema
- Use `!theme toy` for a simple and clean theme
- Use `entity` for database tables
- Use `note` for comments or explanations
- Use `skinparam defaultFontSize 12` for consistent font size
- Use `skinparam defaultFontName "Arial"` for consistent font

## Implementation Flow Diagram
- The implementation flow diagram is located in the `implementation-plan/uml` directory
- The diagram is defined in PlantUML format
- Labels containing whitespaces should be enclosed in double quotes
- Use the `@startuml` and `@enduml` tags to define the diagram
- Use `!theme spacelab` for a simple and clean theme
- Use `start` and `stop` for the flow definition
- Use `if`, `else`, and `endif` for conditional branches
- Use `partition` if a deeper structure is needed
- Use `repeat` for loops
- Use `note` for comments or explanations
