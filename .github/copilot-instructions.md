# copilot-instructions.md

This file provides guidance to GitHub Copilot when working with code in this repository.

When writing code, you MUST follow these principles:
- Code should be easy to read and understand.
- Keep the code as simple as possible. Avoid unnecessary complexity.
- Use meaningful names for variables, functions, etc. Names should reveal intent.
- Functions should be small and do one thing well. They should not exceed a few lines.
- Function names should describe the action being performed.
- Prefer fewer arguments in functions. Ideally, aim for no more than two or  three.
- Only use comments when necessary, as they can become outdated. Instead, strive
  to make the code self-explanatory.
- When comments are used, they should add useful information that is not readily
  apparent from the code itself.
- Properly handle errors and exceptions to ensure the software's robustness.
- Use exceptions rather than error codes for handling errors.
- Consider security implications of the code. Implement security best practices
  to protect against vulnerabilities and attacks.

## Build Commands
- Build: `./gradlew build`
- Run: `./gradlew bootRun`
- Test all: `./gradlew test`
- Test single class: `./gradlew test --tests com.example.ClassName`
- Test single method: `./gradlew test --tests com.example.ClassName.methodName`
- Code coverage report: `./gradlew jacocoTestReport`

## Java Code Style
- Java 21 is used for this project
- Follow standard Spring Boot conventions
- Classes should be immutable when possible
- Use constructor injection for dependencies
- Prefer Java records for DTOs
- Follow package by feature organization
- Tests should follow given/when/then pattern
- Maintain minimum 80% test coverage
- Use meaningful exception messages with proper error handling
- Organize imports alphabetically, no wildcards
- Use consistent indentation (4 spaces)
- Variables used in a stream expression must be final
- Generate code for J2EE 9 or higher

## Java Code
The Java code is located in the following directories or in one of the subfolders:
- mini-tower-api/src/main/java/ch/clx/minitower/
- mini-tower-server/src/main/java/ch/clx/minitower/server
- mini-tower-server/src/test/java/ch/clx/minitower/server

## SQL Code
- mini-tover-server/main/sql/data
- mini-tower-server/main/sql/tables
- mini-tower-server/main/sql/updates

## OpenAI API Code Style (*.yml, *.yaml files)
- No empty server list
- Titles, names and summaries should not exceed 50 characters
- No inline schemas definition
- No missing examples
- No invalid examples
- At least one security scheme
- OperationId is required and should be unique
- No invalid OperationId
- 2xx response present for get operation
- At least one operation level tag
- Parameters should be in order
- Add description to the API components
- Add contact information
- Reuse components to avoid huge OpenAPI files
- A component file should contain description, type and properties
- The component type is 'object'
- The component properties should be in order
- The first component property should be the id, a 64-bit integer not nullable.
- The component should have two properties: createdAt and updatedAt, both of type string and format date-time.
- The component should have two more properties: createdBy and updatedBy, both of type string of max length 32.
- A path file should contain a get with a description, a summary, a tag, a unique operationId, parameters, a 200 response with a description and a schema reference to the component.
- Every method of a path file should have a request header called credentials that is required and of type string.