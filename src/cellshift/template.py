from pathlib import Path
import json

from .context import CAST_DEFINITION_DIR
DEFAULT_TEMPLATE_DIR = CAST_DEFINITION_DIR


def excel_column_name(col_num: int) -> str:
    """
    Convert a 1-based column number to an Excel column name.

    1 -> A
    26 -> Z
    27 -> AA
    52 -> AZ
    53 -> BA
    """
    name = ""
    while col_num:
        col_num, remainder = divmod(col_num - 1, 26)
        name = chr(65 + remainder) + name
    return name


def generate_cast_template(
    source: str | None,
    target: str | None,
    rows: int,
    cols: int,
    output_path: str | Path | None = None,
) -> Path:
    """
    Generate an identity cell mapping template.

    Args:
        source: Source workbook/version name.
        target: Target workbook/version name.
        rows: Number of rows.
        cols: Number of columns.
        output_path: Optional JSON output path. If None,
                     assets/{source}_to_{target}_template.json is used.

    Returns:
        Path to the generated JSON file.
    """
    if rows < 1 or cols < 1:
        raise ValueError("rows and cols must both be >= 1")

    cellmap = {}

    for col in range(1, cols + 1):
        col_name = excel_column_name(col)
        for row in range(1, rows + 1):
            cell = f"{col_name}{row}"
            cellmap[cell] = cell

    data = {
        "metadata": {
            "source": source,
            "target": target,
            "description": "Template mapping",
        },
        "cellmap": cellmap,
    }

    if output_path is None:
        output_path = DEFAULT_TEMPLATE_DIR / f"{source}_to_{target}_template.json"
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return output_path
