---
type: Product Specification
title: Responsive Table Specifications
description: Requirements for static, table-specific Container Query profiles and AI-assisted authoring.
status: draft
---
# Responsive Table Specifications

These specifications define the initial behavior of a statically responsive table that conforms to the [proposed architecture](tables-architecture.md). The terms `MUST`, `SHOULD`, and `MAY` describe mandatory, recommended, and optional requirements.

## Design model

* The responsive unit `MUST` be a table instance, not an application-wide generic table rule.
* A table instance `MUST` declare a finite profile count `N`.
* The first-draft baseline `MUST` use three profiles unless the table definition documents an approved alternative count.
* A profile `MUST` define an exact container-width interval, visible columns, hidden columns, the `Actions` column state, and table-specific column treatment.
* The table host `MUST` be the measured Container Query container.
* The profile width `MUST` refer to the table container's inline size, not to a physical device category or global viewport.
* The profile ranges `MUST` be ordered, non-overlapping, and complete for all expected table-container widths.
* The first profile `MUST` cover all expected widths below the first threshold.
* The final profile `MUST` have no upper bound.
* Profile thresholds `SHOULD` use `rem`.

## Draft baseline profiles

The default three-profile model is:

| Profile | Width interval |
| --- | --- |
| Compact | `0rem <= w < 40rem` |
| Medium | `40rem <= w < 72rem` |
| Wide | `72rem <= w` |

A table-specific definition `MAY` replace these widths before implementation. It `MUST` explain why the replacement widths are derived from the target page shells and field dimensions.

## Static responsive behavior

* Responsive column visibility `MUST` be implemented with Container Queries.
* A table `MUST` use a named inline-size container.
* A table `MUST` keep the same HTML columns in every profile.
* Hidden columns `MUST` be controlled by static CSS selectors.
* JavaScript `MUST NOT` measure the table or viewport to decide which columns are visible.
* JavaScript `MUST NOT` toggle responsive column classes.
* The implementation `MUST NOT` use `ResizeObserver` for responsive column selection.
* JSON values `MUST NOT` dynamically create breakpoints or visibility rules.
* Property order `MUST NOT` automatically determine responsive visibility.
* The compact profile `MUST` show at least the first configured field and the `Actions` column when other fields are hidden.
* The medium and wide visibility sets `MUST` follow the table-specific profile matrix.
* The `Actions` column `MUST` be hidden only when the active profile exposes every field needed for that table.
* Expected widths `MUST NOT` depend on horizontal scrolling to expose normal columns.
* Horizontal scrolling `MAY` be retained only as protection for unsupported widths below the minimum expected width.
* Each profile `MUST` retain fluid behavior within its interval through percentage, fraction, `min()`, `max()`, `clamp()`, wrapping, truncation, or equivalent CSS.
* A static visibility decision `MUST NOT` imply fixed pixel sizing for the complete table.

## Reusable product contract

The shared table foundation `MUST` provide:

* semantic `table`, `caption`, `thead`, `tbody`, `th`, and `td` markup;
* a filter form using native controls;
* previous and next paging controls;
* a named inline-size container;
* Cascade Layers for base, instance, and details styling;
* an `Actions` column;
* a native popover or dialog pattern;
* label generation;
* focus and announcement rules;
* loading, error, empty-result, and no-more-pages behavior.

The shared foundation `MUST NOT` assume one universal list of visible columns or one universal set of column widths.

## Table-specific declaration

Before implementation, each table `MUST` declare:

1. its column-configuration JSON file;
2. its runtime record schema;
3. the source of runtime JSON data;
4. `N` and every profile width boundary;
5. the page shells that supply those widths;
6. the visible and hidden configured columns in every profile;
7. the width and text policy for each column;
8. the filter control for each filterable field;
9. every row action;
10. the details-panel grouping and order;
11. the default `pageSize`;
12. the client-side or server-side paging strategy.

A declaration that does not map every configured column to a profile `MUST` be rejected as incomplete.

## Column-configuration JSON

The column configuration is an authoring-time input to AI. It `MUST NOT` be interpreted by the generated application at runtime.

* The configuration root `MUST` be a JSON array.
* Each array item `MUST` describe one generated column.
* Each column record `MUST` contain `label`, `type`, and `field`.
* `label` `MUST` be the final visible label.
* `type` `MUST` be either `text` or `numeric`.
* `field` `MUST` name a property read from the runtime data record.
* The configuration record order `MUST` define logical column order.
* The generated HTML, CSS, and JavaScript `MUST NOT` fetch or parse the configuration file.
* A configuration change `MUST` require regeneration and revalidation.
* A `numeric` column `SHOULD` use end alignment, tabular numerals, numeric filtering, or documented formatting.
* A `text` column `SHOULD` use wrapping, truncation, and text filtering according to the table declaration.
* AI `MUST NOT` infer a column from runtime values when that column is absent from the configuration.

## JSON data

* The widget `MUST` accept a top-level JSON array of flat record objects.
* Every record `MUST` contain the properties mapped by the column configuration.
* The first configured field `MUST` provide the stable, human-meaningful row identifier.
* The widget `MUST` read values by mapped property name.
* Runtime JSON property order `MUST NOT` affect column order or column visibility.
* A record missing a required mapped property `MUST` be rejected as invalid table data.
* The widget `MUST NOT` require `label`, `key`, `fields`, or wrapper metadata in a record.
* Configuration order `MUST` define logical column order, and the profile matrix `MUST` define visibility.
* Raw property values `MUST` not be treated as trusted HTML.
* A JSON update error `MUST NOT` replace valid data that is already displayed.

## Label rules

* Underscores `MUST` be replaced with spaces.
* Regular words `MUST` use an uppercase initial letter.
* `mm`, `cm`, `dm`, and `m` `MUST` render as `MM`, `CM`, `DM`, and `M`.
* `article_number` `MUST` produce `Article Number`.
* `length_mm` `MUST` produce `Length MM`.
* `width_cm` `MUST` produce `Width CM`.
* `height_dm` `MUST` produce `Height DM`.
* `distance_m` `MUST` produce `Distance M`.
* The icon column label `MUST` be `Actions`.
* Each icon in the `Actions` column `MUST` have an accessible action-specific name.

## Column treatment

* Each column `MUST` have a table-specific width policy or a documented `auto` policy.
* A column with short codes `SHOULD` prevent unnecessary wrapping.
* A numeric column `SHOULD` use end alignment, tabular numerals, and an explicit minimum width.
* A text column `MUST` choose and document wrap, truncate, or word-break behavior.
* Truncation `MUST NOT` be the only access to important hidden text.
* The table definition `MUST` test the longest expected value in each displayed column.
* Column widths `MUST` be authored from content requirements; they `MUST NOT` be inferred during rendering.

## Filters

* A table `MUST` declare the fields that are filterable.
* Each filter `MUST` use an appropriate native control and identify its field.
* The filter value `MUST` not be confused with a missing record value.
* Multiple filters `MUST` combine with logical conjunction unless the table declaration states another rule.
* Filter changes `MUST` recalculate the filtered count and return to the first page.
* Resetting filters `MUST NOT` modify source records.
* The interface `MUST` distinguish no matches from a loading failure.

## Paging

* The widget `MUST` accept a positive-integer `pageSize`.
* Filters `MUST` be applied before paging.
* Every page, except the final page, `MUST` contain at most `pageSize` rows.
* The widget `MUST` show the current page, total page count, and filtered record count.
* Previous and next controls `MUST` be disabled when no destination exists.
* Changing pages `MUST NOT` change the record order or responsive profile.
* Changing pages `SHOULD` preserve or restore focus on the control used.
* A data update that invalidates the current page `MUST` select a valid page.

## Details view

* The details view `MUST` contain every field in logical order.
* The `Actions` column `MUST` be visible only in a profile with hidden fields.
* The details view `MUST` use a description list or equivalent semantics.
* The details view `MUST` have a title identifying the row.
* A popover `MAY` be used for non-modal details.
* A dialog `SHOULD` be used for blocking actions, editing, confirmation, or explicit decision flows.
* The user `MUST` be able to open and close the view with a keyboard.
* Closing the view `MUST` restore focus to the originating action.

## JavaScript responsibility

JavaScript `MAY`:

* validate JSON;
* render rows and details;
* apply filters and calculate pages;
* update paging and result status;
* supplement a native interaction when required;
* restore focus for complex state.

JavaScript `MUST NOT`:

* infer profile widths from rendered content;
* decide whether a column fits;
* move columns at runtime;
* create or replace Container Query rules at runtime;
* depend on a reactive framework for this component.

If a no-JavaScript data fallback is required, the application `MUST` server-render the initial page and the related details. A JSON-only initialization path does not by itself provide that fallback.

## AI authoring controls

* AI `MAY` transform the configuration JSON and reusable template into profile definitions, static HTML, table-specific CSS, and minimum data-loading JavaScript.
* The generated application `MUST NOT` fetch, parse, or interpret the column-configuration JSON.
* AI `MUST` report missing screen or container information as an assumption.
* AI `MUST` use the three-profile draft baseline when no alternative is approved.
* AI-generated responsive decisions `MUST` be reviewed before they become implementation artifacts.
* A reviewer `MUST` verify every profile against representative data.
* A reviewer `MUST` test every boundary immediately below and at the threshold.
* AI `MUST NOT` be required by the delivered table at runtime.

## Acceptance criteria

1. The table definition lists `N`, every width boundary, and every visible column for each profile.
2. At a container width immediately below and at each boundary, the rendered columns exactly match the profile matrix.
3. At a compact width, the first field remains visible and `Actions` is available if fields are hidden.
4. At wide width, `Actions` is hidden only when the profile exposes every field.
5. No JavaScript or `ResizeObserver` code changes responsive column visibility.
6. Long representative values do not overlap adjacent columns at expected widths.
7. The table remains usable at browser zoom and with increased text size.
8. A JSON record missing a required configured field is rejected.
9. `article_number` renders as `Article Number`, and `length_mm` renders as `Length MM`.
10. With 60 records and `pageSize: 20`, the widget displays three pages.
11. A filter that returns seven records displays one page with seven rows.
12. The details panel displays all row fields and restores focus after closing.
13. The table contains no dependency on runtime AI.
14. The delivered application contains no fetch or parse operation for the column-configuration JSON.
15. Numeric and text columns use their generated type-specific treatments.
16. Changing the configuration and rerunning the approved prompt changes the static implementation after review.

## Open draft decisions

* confirm the three-profile count and the `40rem` and `72rem` baseline thresholds;
* inventory the actual page shells that will contain the table;
* decide the default `pageSize`;
* choose popover or dialog per table use case;
* define capitalization for non-unit acronyms;
* decide whether paging is client-side, server-side, or supports both;
* decide whether to store a generated-table manifest for traceability without loading it at runtime;
