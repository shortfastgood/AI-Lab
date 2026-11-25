# Product Update Log

## 2026-11-25
* **Added table generation contract**: Added authoring-time column configuration JSON and an AI prompt template to [Responsive Table Architecture](tables-architecture.md) and [Responsive Table Specifications](tables-specs.md). Runtime code does not interpret the configuration, and static profiles retain fluid CSS behavior.
* **Revised responsive table model**: Replaced generic automatic column collapse with static, table-specific Container Query profiles in [Responsive Table Architecture](tables-architecture.md) and [Responsive Table Specifications](tables-specs.md). Defined a three-profile draft baseline and separated reusable behavior from AI-assisted per-table authoring.

## 2026-11-24
* **Defined action column label**: Set the responsive table icon-column label to `Actions` in [Responsive Table Architecture](tables-architecture.md) and [Responsive Table Specifications](tables-specs.md).
* **Defined measurement units**: Limited uppercase measurement-unit labels to `mm`, `cm`, `dm`, and `m` in [Responsive Table Architecture](tables-architecture.md) and [Responsive Table Specifications](tables-specs.md).
* **Added unit label rule**: Updated [Responsive Table Architecture](tables-architecture.md) and [Responsive Table Specifications](tables-specs.md) so recognized measurement units such as `mm` and `cm` are rendered as `MM` and `CM`.
* **Simplified table JSON contract**: Aligned [Responsive Table Architecture](tables-architecture.md) and [Responsive Table Specifications](tables-specs.md) with flat JSON record objects and labels derived from property names.
* **Translated table concepts**: Formulated [Responsive Table Architecture](tables-architecture.md) and [Responsive Table Specifications](tables-specs.md) in English.
* **Updated responsive tables**: Added ordered JSON fields, per-column filtering, configurable page size, paging behavior, and acceptance criteria to [Responsive Table Architecture](tables-architecture.md) and [Responsive Table Specifications](tables-specs.md).
* **Added drafts**: Added [Responsive Table Architecture](tables-architecture.md) and [Responsive Table Specifications](tables-specs.md) for adaptive tables with hidden-column detail access and optional incremental loading.

## 2026-11-22
* **Added section**: Added the `CSS Grid grid-template-areas` application-shell section to [Design Tokens and Architecture](design-tokens-and-architecture.md).
* **Added example**: Added the Cascade Layer and CSS custom-property architecture example to [Design Tokens and Architecture](design-tokens-and-architecture.md).
* **Added concept**: Added [Design Tokens and Architecture](design-tokens-and-architecture.md) for design token organization and Cascade Layer precedence.
* **Updated overview**: Defined native CSS Grid, Container Queries, `:has()`, Cascade Layers, and CSS custom properties as the primary implementation approach in [Web Essentials](index.md).
