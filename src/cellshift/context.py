#src/cellshift/context.py
from __future__ import annotations
from pathlib import Path
from dworshak_config import DworshakConfig

APP_NAME = "cellshift"
APP_DIR = Path.home() / f".{APP_NAME}"
APP_DIR.mkdir(parents=True,exist_ok=True)

config_mngr = DworshakConfig(path = APP_DIR / "config.json")
config_mngr.set(service=APP_NAME, item="dummy",value="null",overwrite=False)

CAST_DEFINITION_DIR = APP_DIR / "casts"
DEFAULT_CAST_DEFINITION_FILE = "formcast_YYYY_to_YYYY_template.json"
SAMPLE_CAST_DEFINITION_FILE = "formcast_2025_to_2026_CityOfMemphis_contracts.json" # these can be generated with an AI, which can be fed with an accurate set of two XLSX files relative to each other and then an accurate formcast JSON file that describes the relationship between the two. These first three files simply teach the AI what formcast is and how the mapping works. And then, you can give the AI two additional XLSX files, for a new casting, like a known 2026 and a manually converted 2027, and from that it can generated an accurate JSON forcast file describing that relationship. Now using that new formcast file, all 2026 files can be cast into 2027, not manually.

CAST_DEFINITION_DIR.mkdir(parents=True, exist_ok= True)

config_mngr.set(service=APP_NAME,item="cast_definition_dir",value=str(CAST_DEFINITION_DIR), overwrite=False)
cast_definition_dir = Path(config_mngr.get(service=APP_NAME,item="cast_definition_dir")).expanduser().resolve()
if not cast_definition_dir.exists():
    cast_definition_dir = CAST_DEFINITION_DIR

# ---

config_mngr.set(service=APP_NAME,item="cast_definition_file", value= DEFAULT_CAST_DEFINITION_FILE, overwrite= False)

cast_definition_filename = str(config_mngr.get(service=APP_NAME,item="cast_definition_file"))

cast_definition_filepath = cast_definition_dir / cast_definition_filename
if not cast_definition_filepath.exists():
    cast_definition_filepath = CAST_DEFINITION_DIR / DEFAULT_CAST_DEFINITION_FILE
