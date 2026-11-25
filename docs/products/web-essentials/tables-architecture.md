---
type: Product Architecture
title: Responsive Table Architecture
description: Static, table-specific responsive profiles implemented with Container Queries and AI-assisted authoring.
status: draft
---
# Responsive Table Architecture

This draft replaces automatic column collapsing with an explicit, static responsive design. Each table is treated as a separate component because tables can have different fields, minimum widths, text behavior, actions, and useful presentation priorities.

A responsive table declares a finite number of container profiles. Each profile has:

* an exact table-container width interval;
* an exact list of visible columns;
* table-specific widths and text treatment;
* the visibility of the `Actions` column;
* the required filter and paging controls.

CSS implements that declaration with static Container Queries. JavaScript handles data, filtering, paging, and interaction state. The table does not read or interpret its authoring configuration at runtime. JavaScript also does not measure the table, infer which columns fit, or switch responsive classes.

## Draft screen and container model

The initial product baseline uses three screen profiles. A screen profile describes the expected width of the table container, not the physical device or the viewport.

| Profile | Table-container width `w` | Example use | Default intent |
| --- | --- | --- | --- |
| Compact | `0rem <= w < 40rem` | Narrow page region or small screen | Show the identity field and `Actions`. |
| Medium | `40rem <= w < 72rem` | Tablet or constrained desktop region | Show selected high-value columns and `Actions`. |
| Wide | `72rem <= w` | Full desktop content region | Show the columns explicitly assigned to the wide profile. |

The page shell owns the available space. The table host must occupy the width assigned to it by that shell and expose that width as an inline-size query container.

These three thresholds are a first-draft baseline, not a claim that every table fits them. A table-specific design may declare a different profile count or different widths before implementation. That declaration is static and requires review. It must not be calculated or changed in the browser.

## Table-specific profile matrix

Every table needs a profile matrix before HTML and CSS are generated. The following example uses a track record with selected fields:

| Column | Compact | Medium | Wide |
| --- | --- | --- | --- |
| `article_number` | Visible | Visible | Visible |
| `scale` | Hidden | Visible | Visible |
| `section_type` | Hidden | Visible | Visible |
| `scale_ratio` | Hidden | Hidden | Visible |
| `material_code` | Hidden | Hidden | Visible |
| `angle_degrees` | Hidden | Hidden | Visible |
| `length_mm` | Hidden | Hidden | Visible |
| `Actions` | Visible | Visible | Hidden only if no fields are hidden |

The visibility matrix is not inferred from runtime JSON property order or field values. Configuration record order defines logical column order. The first configured field remains the row identifier. The matrix defines responsive presentation.

## Shared contract and table-specific design

The following concerns can be predefined once for the product:

* the `table`, `caption`, `thead`, `tbody`, `th`, and `td` semantic structure;
* the filter form and paging control structure;
* the flat JSON record contract;
* field-label generation rules;
* the `Actions` column label;
* the native popover or dialog structure for row details;
* accessibility requirements;
* Cascade Layer names;
* the rule that Container Queries control responsive visibility;
* the rule that JavaScript does not detect table width.

The following concerns belong to each table and are created or revised with AI assistance:

* the authoring-time column configuration;
* the number and exact width of container profiles;
* the column visibility matrix;
* widths, wrapping, truncation, alignment, and numeric formatting;
* the filter type for each field;
* the set and meaning of row actions;
* the order and grouping of values in the details view;
* the record formatter for values that cannot use their raw JSON form;
* the default page size and the data-loading strategy.

AI is an authoring aid for these table-specific artifacts. It has no runtime role.

## Authoring-time column configuration

Each table has a separate configuration JSON file. The file contains one record per column and is consumed by AI during code generation only. The browser application does not fetch, parse, or interpret this file.

The three required fields are:

* `label`: the final visible column label;
* `type`: the column category, either `text` or `numeric`;
* `field`: the property name in the runtime data record.

```json
[
  {
    "label": "Article Number",
    "type": "text",
    "field": "article_number"
  },
  {
    "label": "Scale",
    "type": "text",
    "field": "scale"
  },
  {
    "label": "Section Type",
    "type": "text",
    "field": "section_type"
  },
  {
    "label": "Length MM",
    "type": "numeric",
    "field": "length_mm"
  }
]
```

Record order defines the logical generated column order. The configuration may omit a runtime property that the table should not present. AI converts the configuration into fixed HTML classes, static CSS, and the minimum data-loading JavaScript. A configuration change requires regeneration and review.

Type `numeric` guides generated alignment, tabular numerals, filter controls, and value formatting. Type `text` guides wrapping and text-filter behavior. These values do not cause runtime type inference.

## AI-assisted authoring contract

AI receives:

* the column-configuration JSON file;
* the reusable table template;
* one or more representative JSON records;
* the list of page shells and their expected table-container widths;
* the requested number of responsive profiles, or approval to use the three-profile baseline;
* required fields, actions, filters, formatting rules, and accessibility constraints;
* the maximum accepted text or number widths for each field, when known.

AI produces:

* a table-specific configuration review;
* the proposed profile table;
* a column visibility matrix;
* a table-specific HTML template;
* a static Cascade Layer and Container Query stylesheet;
* a focused test matrix for profile boundaries;
* an explicit list of assumptions that require human review.

AI must not:

* infer hidden-column decisions from sample values alone;
* add runtime width measurement;
* generate JavaScript that toggles column visibility classes;
* alter the JSON contract without approval;
* invent fields, actions, filters, or labels;
* replace accessibility review or visual review.

## AI generation prompt

The project provides this prompt template to transform the reusable table template into one static table implementation. Values inside braces are replaced before the prompt is sent:

```text
Generate the final implementation of a static responsive table.

Use the reusable HTML, CSS, and JavaScript table template supplied below.
Use the column configuration JSON as authoring input only. Do not make the
application fetch or parse the configuration at runtime.

Required outputs:
1. Complete table-specific HTML.
2. Static Cascade Layer and Container Query CSS.
3. The minimum JavaScript needed to validate runtime data, load the supplied
   data source, render rows and details, filter, and page.
4. A profile matrix and boundary test checklist.
5. A list of assumptions and unresolved decisions.

Constraints:
- The configuration contains one record per column with `label`, `type`
  (`text` or `numeric`), and `field`.
- Preserve configuration order as logical column order.
- Do not add runtime width measurement, `ResizeObserver`, or runtime-generated
  Container Queries.
- Keep column visibility fixed per approved profile.
- Keep responsive behavior inside each profile through fluid widths, wrapping,
  alignment, truncation, and text flow.
- Preserve semantic markup, keyboard access, accessible names, `Actions`,
  paging, and filter behavior.
- Use native HTML before JavaScript.
- Do not invent fields, actions, filters, or data.
- Do not introduce a framework.

Approved container profiles:
{containerProfiles}

Column configuration JSON:
{columnConfiguration}

Representative runtime JSON records:
{runtimeRecords}

Runtime data source and loading requirements:
{dataSource}

Required filters, actions, details behavior, page size, and paging mode:
{interactionRequirements}

Reusable table template:
{tableTemplate}
```

This prompt generates the final static implementation. It does not authorize a runtime AI dependency.

## JSON and labels

The JSON document remains an array of flat record objects:

```json
[
  {
    "article_number": "20224",
    "scale": "H0",
    "scale_ratio": "1:87",
    "section_type": "curve",
    "material_code": "C",
    "angle_degrees": 24.3,
    "length_mm": 185.55
  }
]
```

All records in one table contain the properties mapped by the configuration. Runtime object property order is irrelevant. The first configured field is the row identifier. A record that does not contain every required mapped property is invalid.

The displayed label is derived from a property name by replacing underscores with spaces and capitalizing regular words. The measurement units `mm`, `cm`, `dm`, and `m` become `MM`, `CM`, `DM`, and `M`.

Examples:

* `article_number` becomes `Article Number`;
* `scale_ratio` becomes `Scale Ratio`;
* `length_mm` becomes `Length MM`;
* `width_cm` becomes `Width CM`;
* `height_dm` becomes `Height DM`;
* `distance_m` becomes `Distance M`.

## Container and HTML structure

The table host is a named inline-size container. Its name must be unique enough to avoid matching a parent or sibling table.

```html
<section class="tracks-table-region">
  <search class="table-filters">
    <label>
      Section Type
      <input name="section_type" type="search">
    </label>
    <button type="reset">Reset filters</button>
  </search>

  <table class="data-table tracks-table">
    <caption>Tracks</caption>
    <thead>
      <tr>
        <th scope="col" class="column--article-number">Article Number</th>
        <th scope="col" class="column--scale">Scale</th>
        <th scope="col" class="column--scale-ratio">Scale Ratio</th>
        <th scope="col" class="column--section-type">Section Type</th>
        <th scope="col" class="column--material-code">Material Code</th>
        <th scope="col" class="column--angle column--numeric">Angle Degrees</th>
        <th scope="col" class="column--length column--numeric">Length MM</th>
        <th scope="col" class="column--actions">Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row" class="column--article-number">20224</th>
        <td class="column--scale">H0</td>
        <td class="column--scale-ratio">1:87</td>
        <td class="column--section-type">Curve</td>
        <td class="column--material-code">C</td>
        <td class="column--angle column--numeric">24.3</td>
        <td class="column--length column--numeric">185.55</td>
        <td class="column--actions">
          <button
            type="button"
            popovertarget="details-20224"
            aria-label="Show details for article 20224"
          >
            Show details
          </button>
        </td>
      </tr>
    </tbody>
  </table>

  <nav class="table-pagination" aria-label="Table pages">
    <button type="button" data-page="previous">Previous</button>
    <output aria-live="polite">Page 1 of 4 - 96 records</output>
    <button type="button" data-page="next">Next</button>
  </nav>
</section>
```

Every column class appears on the matching heading and body cells. This makes each table's static profile map explicit and reviewable.

## Static Container Query implementation

The compact profile is the base state. Medium and wide rules reveal only the columns declared by the table's profile matrix.

```css
@layer components.table-base, components.table-instance, components.table-details;

@layer components.table-base {
  .tracks-table-region {
    container: tracks-table / inline-size;
    inline-size: 100%;
  }

  .tracks-table {
    inline-size: 100%;
    table-layout: fixed;
  }

  .tracks-table .column--numeric {
    text-align: end;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
  }
}

@layer components.table-instance {
  .tracks-table .column--scale,
  .tracks-table .column--scale-ratio,
  .tracks-table .column--section-type,
  .tracks-table .column--material-code,
  .tracks-table .column--angle,
  .tracks-table .column--length {
    display: none;
  }

  .tracks-table .column--article-number {
    inline-size: auto;
  }

  .tracks-table .column--actions {
    display: table-cell;
    inline-size: 6rem;
  }

  @container tracks-table (min-width: 40rem) {
    .tracks-table .column--scale {
      display: table-cell;
      inline-size: 5rem;
    }

    .tracks-table .column--section-type {
      display: table-cell;
      inline-size: 10rem;
      overflow-wrap: anywhere;
    }
  }

  @container tracks-table (min-width: 72rem) {
    .tracks-table .column--scale-ratio,
    .tracks-table .column--material-code,
    .tracks-table .column--angle,
    .tracks-table .column--length {
      display: table-cell;
    }

    .tracks-table .column--scale-ratio {
      inline-size: 7rem;
    }

    .tracks-table .column--material-code {
      inline-size: 8rem;
    }

    .tracks-table .column--angle,
    .tracks-table .column--length {
      inline-size: 8rem;
    }

    .tracks-table .column--actions {
      display: none;
    }
  }
}
```

This example intentionally contains repeated table-specific selectors. That repetition is a design record: reviewers can verify exactly which fields appear at each width without tracing generic priority logic.

If a wide profile still hides any field, the wide rule leaves the `Actions` column visible. It is hidden only when the wide matrix contains no hidden fields.

## Row details

When a profile hides any field, the row's `Actions` column provides access to a native popover or dialog containing every field in logical order:

```html
<section id="details-20224" popover aria-labelledby="details-20224-title">
  <h2 id="details-20224-title">Article Number 20224</h2>
  <dl>
    <div>
      <dt>Article Number</dt>
      <dd>20224</dd>
    </div>
    <div>
      <dt>Scale</dt>
      <dd>H0</dd>
    </div>
    <div>
      <dt>Scale Ratio</dt>
      <dd>1:87</dd>
    </div>
    <div>
      <dt>Section Type</dt>
      <dd>Curve</dd>
    </div>
    <div>
      <dt>Material Code</dt>
      <dd>C</dd>
    </div>
    <div>
      <dt>Angle Degrees</dt>
      <dd>24.3</dd>
    </div>
    <div>
      <dt>Length MM</dt>
      <dd>185.55</dd>
    </div>
  </dl>
  <button
    type="button"
    popovertarget="details-20224"
    popovertargetaction="hide"
  >
    Close
  </button>
</section>
```

A popover is suitable for non-modal details. A `<dialog>` is required when the interaction blocks the page, edits data, or requires a decision.

## Filtering and paging

Container Queries choose the presentation. JavaScript remains responsible for data behavior:

* validate the record schema;
* derive labels;
* render rows and details;
* apply per-column filters;
* calculate a page of records;
* update paging controls and status text;
* manage an interaction when a native HTML API is not sufficient.

JavaScript must keep one authoritative copy of records, filters, the page index, and the configured `pageSize`. It must not decide column visibility from container width.

A table initialized only from JSON requires JavaScript to render data. If the product requires a no-JavaScript data fallback, the application must server-render at least the initial page and the related details.

## Validation strategy

Each table definition is tested at:

* a width immediately below and exactly at every profile boundary;
* the expected minimum and maximum widths of each page shell;
* increased text size and browser zoom;
* the longest representative value in every column;
* keyboard and screen-reader use;
* filtered and empty result states;
* first, middle, and final pages.

The tests verify the declared matrix. They do not attempt to prove that one universal table layout works for arbitrary content.

See also the [responsive table specifications](tables-specs.md).
