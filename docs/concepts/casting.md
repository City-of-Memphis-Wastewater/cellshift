# Casting

A cast transforms one Excel workbook into another by applying a predefined cell mapping.

Rather than editing a new year's spreadsheet manually, CellShift copies values from a source workbook into their corresponding locations in a target workbook according to a JSON cast definition.

The workflow is:

1. Start with an existing workbook (for example, a 2025 contract spreadsheet).
2. Generate a cast template that matches the workbook's dimensions.
3. Edit the generated JSON to define how cells should be transferred.
4. Run the cast operation.
5. CellShift creates a new workbook (for example, the 2026 contract spreadsheet) with values placed according to the mapping.

Each cast definition contains two parts:

- Metadata — describes the source year, target year, and worksheet dimensions.
- Cell map — specifies, for every destination cell, which source cell should be copied. Unmapped cells may be left unchanged or empty, depending on the cast definition.

Because the mapping is stored as JSON, it can be version-controlled, reviewed, shared, and reused. Once a cast definition has been created for a particular spreadsheet format, future workbooks with the same layout can be generated consistently with a single command.
