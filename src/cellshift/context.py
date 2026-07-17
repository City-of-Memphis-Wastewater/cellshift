#
from __future__ import annotations
from pathlib import Path
from dworshak_config import DworshakConfig

APP_NAME = "cellshift"
APP_DIR = Path.home() / f".{APP_NAME}"

config_mngr = DworshakConfig(path = APP_DIR / "config.json")
config_mngr.set(service=APP_NAME, item="dummy","null",overwrite=False)
