# AI Assisted Reverse Engineering 

This directory contains a collection of use cases demonstrating AI-assisted reverse engineering techniques.

The environment used for the use case consists in the Visual Source Code with GitHub Copilot, for more information follow this **[link](../../setup/README.md)**

## Use Case 01

**Description**: Reverse engineering of an ASP.NET Core MVC application with Razor views and Knockout.js frontend.

The initial step in understanding a project is to obtain a comprehensive overview of its architecture and components. This was accomplished by utilizing the prompt **[01_documentation-writer.prompt.md](use-case-01/01_documentation-writer.prompt.md)**, which led to the creation of the **[architetture-overview.md](use-case-01/architecture-overview.md)** document. This overview serves as a foundational reference, providing a high-level architectural vision that supports subsequent analysis and development activities.


The next step involves generating an initial draft for the migration process using the **[01_build_custom_tag_list.prompt.md](use-case-01/01_build_custom_tag_list.prompt.md)** prompt. This prompt initiates a conversation, the details of which are documented in **[migration-planning-chat.md](use-case-01/migration-planning-chat.md)**. The first tangible outcome of this process is the creation of a preliminary migration plan, captured in **[migration-planning.md](use-case-01/migration-planning.md)**. This plan provides a structured approach for migrating application components, serving as a foundation for further refinement and implementation.

