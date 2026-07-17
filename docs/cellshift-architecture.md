 so the goal is to use a JSON static map to map and transfer data from a single page Excel file to another but we keep the engine  ‘dumb’ so it isn’t actually aware of the data?
Correct
Excellent assessment 
What we should also have is an empty target XLSX that already has the empty fields and basic formatting.

So we don't need to cast the descriptions like "Company Name _____ " or "Date _____ "; those already exist in the unfilled 2026 template XLSX. 

That blank target file can be configured in ~/.formcast/config.json, managed by dworshak-config.

The selected formcast_2025_to_2026_CityOfMemphis_contracts.json file can also be indicated in ~/.formcast/config.json

```python
#src/forecast/context.py
APP_NAME = 'formcast'
APP_DIR = Path.home() / f".{APP_NAME}"
APP_DIR.mkdir(parents=True,exist_ok=True)
```
~/.formcast/config.json
This config.json file is generated and populated and managed by dworshak-config. Default values will populated the config.json on the first run, overwrite = false. In this was users can edit directly the file as lightweight interface, and their manual edits will be accessed.

config_mngr.get() calls should generically leverage Python type suggestions. In this case, and string that represents a path should be immediately cast to a Path type using 

```python target_unfilled_template_path = Path(config_mngr.get(service=APP_NAME,item="target_unfilled_template"). expanduser().resolve()
```
And then we check if that path exists, and if not, we use 

```python
target_unfilled_template_path = DEFAULT_TARGET_UNFILLED_TEMPLATE_PATH
```
project name is up for debate  

Any idea other than "formcast" ?
dworshak works like this:

```python
# src/formcast/context.py
from dworshak_config import DworshakConfig
from pathlib import Path

from .context import
 APP_DIR, APP_NAME

config_mngr = DworshakConfig(path=APP_DIR / "config.json") 
```

Then you can say

```python

config_mngr.set(service=APP_NAME, item="target_unfilled_template", DEFAULT_TARGET_UNFILLED_TEMPLATE_PATH, overwrite=False)
```


---

This hasn't much yet mentioned the central use of a JSON file that defines relative casting. We can call it formcast_2025_to_2026_CityOfMemphis_contracts.json, and it can live in ~/.formcast/casts/, aka, 

`CAST_DEFINITION_DIR = APP_DIR / "casts"`

This can be identified using 
```python
CAST_DEFINITION_DIR = APP_DIR / "casts"
DEFAULT_CAST_DEFINITION_FILE = "formcast_YYYY_to_YYYY_template.json"

SAMPLE_CAST_DEFINITION_FILE = "formcast_2025_to_2026_CityOfMemphis_contracts.json" # these can be generated with an AI, which can be fed with an accurate set of two XLSX files relative to each other and then an accurate formcast JSON file that describes the relationship between the two. These first three files simply teach the AI what formcast is and how the mapping works. And then, you can give the AI two additional XLSX files, for a new casting, like a known 2026 and a manually converted 2027, and from that it can generated an accurate JSON forcast file describing that relationship. Now using that new formcast file, all 2026 files can be cast into 2027, not manually.

CAST_DEFINITION_DIR.mkdir(parents=True, exist_okay= True)

ensure_as

config_mngr.set(service=APP_NAME,item="cast_definition_dir",str(CAST_DEFINITION_DIR), overwrite=False)
cast_definition_dir = Path(config_mngr.get(service=APP_NAME,item="cast_definition_dir").expanduser().resolve()
if not cast_definition_dir.exists():
    cast_definition_dir = CAST_DEFINITION_DIR

# ---

config_mngr.set(service=APP_NAME,item="cast_definition_file", DEFAULT_CAST_DEFINITION_FILE, overwrite= False)

cast_definition_filename = str(config_mngr.get(service=APP_NAME,item="cast_definition_file"))

cast_definition_filepath = cast_definition_dir / cast_definition_filename
if not cast_definition_filepath.exists():
    cast_definition_filepath = CAST_DEFINITION_DIR / DEFAULT_CAST_DEFINITION_FILE
```

This doesn't include the code to ensure that the default and the sample exist and are in the right place.