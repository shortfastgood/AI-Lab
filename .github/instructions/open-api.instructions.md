
---
description: 'Guidelines for building OpenAPI specifications'
applyTo: '**/*.yml, **/*.yaml'
---

# OpenAPI  Development

## OpenAPI API Code Style (*.yml, *.yaml files)
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